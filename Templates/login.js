document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('username').value;

        // Store the logged-in user in session storage
        sessionStorage.setItem('loggedInUser', username);

        // Redirect back to the main page
        window.location.href = 'index.html';
    });
});
