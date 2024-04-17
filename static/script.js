import { Wave } from "../../node_modules/@foobar404/wave";

document.addEventListener('DOMContentLoaded', function() {
    // Select the player window and fullscreen button elements
    const playerWindow = document.getElementById('playerWindow');
    const fullscreenButton = document.getElementById('fullscreenBtn');
    const liveInputRadio = document.getElementById('liveInput');
    const fileUploadRadio = document.getElementById('fileUpload');
    const fileInput = document.getElementById('fileInput');
    const uploadBtn = document.getElementById('uploadBtn');
    const loginBtn = document.getElementById('loginBtn');
    const userInfo = document.getElementById('userInfo');
    const usernameDisplay = document.getElementById('usernameDisplay');
    const logoutBtn = document.getElementById('logoutBtn');
    const submitFile = document.getElementById('submitFile');

    // Wave.js defines
    let audioInput = document.querySelector('audioInput');
    let visualizerWindow = document.querySelector('visualSpace');
    let wave = new Wave(audioInput, visualizerWindow);

    // Check if user is logged in
    const loggedInUser = sessionStorage.getItem('loggedInUser');
    if (loggedInUser) {
        usernameDisplay.textContent = loggedInUser;
        loginBtn.style.display = 'none';
        userInfo.style.display = 'block';
    }

    // Logout button event listener
    logoutBtn.addEventListener('click', function() {
        // Remove the logged-in user from session storage and refresh the page
        sessionStorage.removeItem('loggedInUser');
        window.location.reload();
    });
    
    // Function to toggle fullscreen mode
    function toggleFullScreen() {
        if (!document.fullscreenElement) {
            if (playerWindow.requestFullscreen) {
                playerWindow.requestFullscreen();
            } else if (playerWindow.webkitRequestFullscreen) { // Safari
                playerWindow.webkitRequestFullscreen();
            } else if (playerWindow.msRequestFullscreen) { // IE11
                playerWindow.msRequestFullscreen();
            }
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            } else if (document.webkitExitFullscreen) { // Safari
                document.webkitExitFullscreen();
            } else if (document.msExitFullscreen) { // IE11
                document.msExitFullscreen();
            }
        }
    }

    // Add event listener to the fullscreen button
    fullscreenButton.addEventListener('click', toggleFullScreen);

    // Event listeners for the radio buttons
    fileUploadRadio.addEventListener('change', function() {
        if (fileUploadRadio.checked) {
            uploadBtn.style.display = 'block';
        } else {
            uploadBtn.style.display = 'none';
        }
    });

    liveInputRadio.addEventListener('change', function() {
        if (liveInputRadio.checked) {
            uploadBtn.style.display = 'none';
        }
    });

    // Event listener for the 'Select File' button
    uploadBtn.addEventListener('click', function() {
        fileInput.click(); // Trigger the hidden file input click
    });

    // Event listener for the hidden file input
    fileInput.addEventListener('change', function(event) {
        if (event.target.files.length > 0) {
            const fileName = event.target.files[0].name;
            console.log('File selected:', fileName);
            // Add additional logic here if needed, e.g., displaying the file name somewhere on the page
        }
    });
    /*  TODO: add process to change audio input based on user choice */

    // Wave.js stuff
    /*  
    Available wave animations:
        Arcs, Circles, Cubes, Flower, Glob, Lines, Shine, Square, Turntable, Wave
    */
    wave.addAnimation(
        new wave.animations.Wave({
            lineColor: 'white',
            lineWidth: 8,
            fillColor: 'purple'
        }
    ));

});

function UploadFile() {
    let formData = new FormData();
    let file = document.getElementById('fileUploadButton').files[0];
    formData.append('file', file)

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload_file', true);
    xhr.send(formData);
}





