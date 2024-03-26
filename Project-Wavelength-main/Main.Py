from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
import sqlite3 as sql
import os

app = Flask (__name__)
app.secret_key = "ASF2T3B97V-2V930"
app.static_folder = 'static'

USER_DATABASE_NAME = "database.db"

# Will create a new database if it already doesn't exist
connection = sql.connect(USER_DATABASE_NAME)
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL,
                    storedAudios TEXT
                )''')

connection.commit()
connection.close()


# Returns whether the given string could be an SQL injection
def CouldBeSQLInjection(s):
    return "'" in s or '"' in s or "$" in s or ";" in s or "=" in s

# Checks the database for a username that
def DoesUserNameExist(username):
    connection = sql.connect(USER_DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM users WHERE username = "{username}"')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return not (not result or not result[0])

# Returns whether the user is logged in
def isLoggedIn():
    if "user" in session:
        username = session["user"]
        isLoggedIn = True

        connection = sql.connect(USER_DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM users WHERE username = "{username}"')
        result = cursor.fetchall()
        if not result or not result[0]:
            isLoggedIn = False

        connection.commit()
        connection.close()
        return isLoggedIn





# User Upload file. Will be stored in user directory
@app.route('/upload_file', methods=["POST"])
def upload_file():
    file = request.files['file']
    file.save(f'Audios/{session["user"]}/' + file.filename)
    return ('', 204)


# User Sign Up
@app.route('/Home')
def user_home():
    if not isLoggedIn():
        return redirect(url_for('sign_in'))
    return render_template('index.html')



# User Sign Up
@app.route('/SignUp',methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        print(username)
        print(password)

        def loginError(errorMsg):
            return render_template("signup.html",
                errorMsg = errorMsg     
            )

        if len(username) < 3:
            return loginError("Username must be at least 3 characters")
        elif len(username) > 20:
            return loginError("Username must cannot be over 20 characters")
        elif len(password) < 8:
            return loginError("Password must be at least 8 character")
        elif len(password) > 20:
            return loginError("Password must be less than 20 characters")
        elif CouldBeSQLInjection(username) or CouldBeSQLInjection(password):
            return loginError("Invalid characters. Please try again")
        elif DoesUserNameExist(username):
            return loginError("This username has been taken")


        connection = sql.connect(USER_DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute(f'''INSERT INTO users (username, password, storedAudios) 
                            VALUES("{username}", "{password}", "")''')
        connection.commit()
        connection.close()

        # Create audio folder
        os.mkdir("./Audios/" + username)

        return render_template('login.html', errorMsg = "Account created!")
    else:
        return render_template('signup.html')

# User Sign Out
@app.route('/LogoutConfirmation')
def user_logout_confirmation():
    return render_template("logoutConfirmation.html")

# User Sign Out
@app.route('/UserLogout')
def user_logout():
    session.pop("user", None)
    return redirect(url_for("sign_in"))

# User Sign In
@app.route('/SignIn',methods=["POST", "GET"])
def sign_in():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        def loginError(errorMsg):
            return render_template("login.html",
                errorMsg = errorMsg     
            )

        print(username)
        print(password)

        if CouldBeSQLInjection(username) or CouldBeSQLInjection(password):
            return loginError("Invalid characters. Please try again")

        connection = sql.connect(USER_DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM users WHERE username = "{username}"')
        result = cursor.fetchall()
        if not result or not result[0]:
            connection.commit()
            connection.close()
            return loginError("Incorrect username!")
        cursor.execute(f'SELECT * FROM users WHERE username = "{username}" AND password = "{password}"')
        result = cursor.fetchall()
        if not result or not result[0]:
            connection.commit()
            connection.close()
            return loginError("Incorrect password!")

        connection.commit()
        connection.close()

        session["user"] = username
        return redirect(url_for('user_home'))
    else:
        if "user" in session:
            return redirect(url_for("user_logout_confirmation"))
        else:
            return render_template("login.html")


# Homepage
@app.route ('/')
def index():
    # If we ever wanted to add a home page for people not yet signed up, set it up here
    return redirect(url_for('user_home'))



if __name__ == '__main__':
    app.run(debug=True)

    