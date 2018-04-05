# COMP2005 - Group L

MUN COMP2005 Winter 2018, Team L group project

_NOTE_: If you are not doing so already, you can read a preformatted version for this README on the project's repository: https://github.com/COMP2005-L/comp2005-l

## Installation
To install the provided package, use `pip install {distribution-file-name}`, where `{distribution-file-name}` is the name of the provided zip file, with the extension included.

## Running the App
Navigate to the folder where the package was installed (such that the `app.db` file is a direct child of the current directory), and run the following commands:
```
$ export FLASK_APP=app
$ flask run
```
The app should be running on `localhost:5000` by default. You can navigate to the app in your browser by going to `http://localhost:5000/` .

## Running Tests

To run the tests, navigate to the folder where the package was installed (such that the `app.db` file is a direct child of the current directory), and run `python -m unittest discover`

## Test data for User

For testing purposes, there's test data in the database for better functionality of the prototype. A username and password is provided. 
The username is "admin" and password is "password". To test registration, click on "Click here to register!"
