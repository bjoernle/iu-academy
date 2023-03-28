# AirBnB Datamart

## What is it?
It's a datamart for fictional airbnb clone.
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
    python AirBnBDatamart.py action=TestEverything
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
        python AirBnBDatamart.py action=TestEverything
        ---

    StartServer ()
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=StartServer
        ---

    GetComments ()
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=GetComments
        ---

    GetCommentsInDateRange (string from, string to)
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=GetCommentsInDateRange from=YYYY-MM-DD to=YYYY-MM-DD
        ---

    GetPhotosByUsertype (string usertype)
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=GetPhotosByUsertype usertype=Host
        ---

    GetPhotosRatesHigherNumber (int number)
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=GetPhotosRatesHigherNumber number=3
        ---

    PlacesEvaluatedByBothUsertypes ()
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=PlacesEvaluatedByBothUsertypes
        ---
    
    PlacesInCityAndTimespan (string city, string from, string to)
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=PlacesInCityAndTimespan
        ---

    PlacesRentedByUsertype (string usertype)
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=PlacesRentedByUsertype usertype=Guest
        ---    
    
    PlacesUnoccupiedNow ()
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=PlacesUnoccupiedNow usertype=Guest
        ---    

    TestEverything ()
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=TestEverything
        ---  

    ShowAll ()
        Example: 
    
        ---shell
        python AirBnBDatamart.py action=ShowAll
        ---  


## Tests

	---shell
	python AirBnBDatamart.py action=TestEverything
	---
