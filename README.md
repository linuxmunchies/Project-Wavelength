# Project Wavelength

## Overview

Welcome to Project Wavelength, an immersive web experience where audio meets visual art in real-time. Designed by 'Ride the Wave', a passionate team from the University of Alabama at Birmingham, this project allows users to interact with visuals that are dynamically generated based on audio inputs, enhancing the user experience with personalized features.

## Soon-To-Be Future Project Structure

```
Project-Wavelength-main/
│
├── Main.Py                    # Main script for backend operations (if any)
├── database.db                # Database file for user and session management
├── static/                    # Contains all the static content like CSS and JS files
│   ├── css/                   # CSS files
│   ├── js/                    # JavaScript files
│   └── assets/                # Images, icons, and other media files
├── Templates/                 # HTML templates for the web interface
│   ├── index.html             # Main page with visual and audio interaction
│   └── login.html             # Login page for user authentication
│   └── logoutConfirmation.html # Logout page 
│   └── signup.html             # Signup Page
└── node_modules/              # Node.js modules (not used directly in project deployment)
```

## Features

- **Dynamic Visual Player**: Experience interactive visuals that react to either live audio inputs or pre-uploaded sound files.
- **Input Selection**: Choose your audio source to see visual effects tailored to the music or sounds you play.
- **User Authentication**: Manage your sessions with a simple login/logout system ensuring a personalized experience.

## Getting Started

To run Project Wavelength locally:

1. **Pre-requisites**:
   - Install Visual Studio Code.
   - Install the Live Server extension for VSCode.

2. **Open and Run**:
   - Open the project folder in VSCode.
   - Right-click on `index.html` from the `Templates` directory and select "Open with Live Server". (or whichever you want to see a live render of.)

This setup provides you with a quick way to see changes in real-time without needing a full backend server running, simplifying development and testing.

## Development Guidelines

- **Modifications**: When updating HTML, CSS, or JavaScript, ensure changes reflect across all relevant files to maintain consistency.
- **Testing**: Test new changes locally by reloading the Live Server session in VSCode to ensure all interactions and features perform as expected.

## Acknowledgments

Thank you to the CS499 Keystone course instructors at UAB for their continuous support, and to all team members and contributors who have dedicated time and effort to Project Wavelength.

---

This README is designed to provide a clear, updated description of your project with an emphasis on the new development setup and project structure. If there are any specific sections you want to expand upon or adjust, feel free to let me know!
