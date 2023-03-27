# AirBnB Datamart

## What is it?
It's a datamart for the webpage airbnb.
You could run it directly by python, or you could use the Python server.

## Installation of Python

https://www.python.org/downloads/


## Installation of pip installer
    Linux
    ---shell
    sudo apt install python3-pip
    ---

    Windows
    ---shell
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    ---

## Installation of requirements

    ---shell
    pip install requirements.txt
    ---

## Usage by python server:
Start a commandshell:
    Windows:
    Windows key, then type "cmd" for A Commandshell.

    Linux: 
    Alt + "T"

Change the directory to the python path, for example:
    ---shell
    cd c:\pythonscripts\AirBnBDatamart\Python)
    ---
or
    ---shell
    cd /usr/YOURNAME/pythonscripts/AirBnBDatamart/
    ---

And start the server directly or by the AirBnBDatamart app
    ---shell
    python AirBnBDatamart.py action=StartServer
    ---

Follow instructions on screen


## Usage by python directly:

    ---shell
    python AirBnBDatamart.py action=YOURACTION ...........
    ---

for example a "test everything":

    ---shell
    python AirBnBDatamart.py action=TestEverything automatic_tests=True user_id=1
    ---


## Actions (and attributes)

first open commandline and change the directory to the python folder
The foldername you copied the project-folder into: 
	foldername="--FolderName--"
	
Windows
	Example:("cd --FolderName--/Python)
Linux
	Example:("cd --FolderName--\Python)

Now you're able to do something like this:
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=LoginUser user_name=USERNAME user_password=USERPASSWORD
        ---


### Actions
	
    LoginUser (string username, string password)
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=LoginUser user_name=USERNAME user_password=USERPASSWORD
        ---
    
    SignupUser (string username, string password)
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=SignupUser user_name=USERNAME user_password=USERPASSWORD
        ---
    
    TestEverything (string user_id)
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=TestEverything user_id=USER_ID
        ---
    
    TestEverythingAutomatic (string user_id, string automatic_tests="True")
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=TestEverythingAutomatic user_id=USER_ID automatic_tests="False"
        ---

    StartServer ()
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=StartServer
        ---

## Tests

it's necessary to create a user first, if you're not selecting the automatic full test
for analysing.
for normal analysing, it's necessary to create habits and actions before.

	---shell
	python AirBnBDatamart.py action=TestEverything automatic_tests=True user_id=1
	---
