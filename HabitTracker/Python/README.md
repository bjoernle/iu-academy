#My little habit tracker

## What is it?

It's an app for tracking your habits.
You could run it directly by python, or you could use something like XAMPP PHP server.

## Installation of Python

https://www.python.org/downloads/


## Installation of requirements

    ---shell
    pip install requirements.txt
    ---


## Installation of pip installer
    Linux
    ---shell
    sudo apt install python3-pip
    ---

    Windows
    ---shell
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    ---


## Installation of xampp (unnecessary)

https://www.apachefriends.org/


## Usage by php server:
Windows:
copy the HabitTracker folder to your XAMPP "htdocs" folder (C:\xampp\htdocs\).
Linux:
copy the HabitTracker folder to your LAMPP "html" folder (/var/www/html).
In the XAMPP folder, click on xampp_start.exe

open http://localhost/HabitTracker by your webbrowser with enabled javascript

Follow instructions on screen


## Usage by python directly:

    ---shell
    python HabitTracker.py action=YOURACTION ...........
    ---

for example a test everything:

    ---shell
    python HabitTracker.py action=TestEverything automatic_tests=True user_id=1
    ---


## Actions (and attributes)

first open commandline and change the directory to the python folder
The foldername you copied the project-folder into: 
	foldername="--FolderName--"
	
For XAMPP:
	Example:
	Windows:("cd C://xampp/htdocs/--FolderName--/Python)
For LAMPP:
	Example:
	Linux:("cd \var\www\html\--FolderName--\Python)

Now you're able to do something like this:
        Example: 
    
        ---shell
        python HabitTracker.py action=LoginUser user_name=USERNAME user_password=USERPASSWORD
        ---


### Attributes for each actions

	Bool-string show_messages
	Bool-string show_db_actions


### Attributes for some actions
    
	Bool-string return_json
        GetHabitsOfUser (string user_id, Bool-string return_json=false)


### Actions

every value with spaces you have to limit with the " char
	
    LoginUser (string username, string password)
        Example: 
    
        ---shell
        python HabitTracker.py action=LoginUser user_name=USERNAME user_password=USERPASSWORD
        ---
    
    SignupUser (string username, string password)
        Example: 
    
        ---shell
        python HabitTracker.py action=SignupUser user_name=USERNAME user_password=USERPASSWORD
        ---
    
    AddHabit (string user_id, string name, string description, string timespan, string date_start, string date_end, string target_time_start, string target_time_end, string target_duration, string target_repeats)
        Example: 
    
        ---shell
        python HabitTracker.py action=AddHabit user_id=USER_ID habit_name="HABIT_NAME" timespan="dayly"<-OR->timespan="weekly"<-OR->timespan="monthly"<-OR->timespan="yearly"
        date_start="2023-01-01" date_end="2023-12-31" target_time_start="07:00" target_time_end="08:00" target_duration="00:30" target_repeats="1"
        ---
    
    AddAction (string user_id, string habit_id, DateTime-string start_datetime, DateTime-string end_datetime, DateTime-string created)
        Example: 
    
        ---shell
        python HabitTracker.py action=AddAction user_id=USER_ID habit_id=HABIT_ID start_datetime="2023-01-01 07:21:21" end_datetime="2023-01-01 07:21" created="2022-12-25 09:12"
        ---
    
    
    GetHabitsOfUser (string user_id)
        Example: 
    
        ---shell
        python HabitTracker.py action=GetHabitsOfUser user_id=USER_ID
        ---
    
    GetDoneHabitsOfUser (string user_id, string habit_id)
        Example: 
    
        ---shell
        python HabitTracker.py action=GetDoneHabitsOfUser user_id=USER_ID habit_id=HABIT_ID
        ---
    
    ShowAll (string user_id)
        Example: 
    
        ---shell
        python HabitTracker.py action=ShowAll user_id=USER_ID
        ---
    
    ShowAllOfUser (string user_id)
        Example: 
    
        ---shell
        python HabitTracker.py action=ShowAllOfUser user_id=USER_ID
        ---
		
    AnalyseData (string user_id)
        Example: 
    
        ---shell
        python HabitTracker.py action=AnalyseData user_id=USER_ID
        ---		
    
    TestEverything (string user_id)
        Example: 
    
        ---shell
        python HabitTracker.py action=TestEverything user_id=USER_ID
        ---
    
    TestEverythingAutomatic (string user_id, string automatic_tests="True")
        Example: 
    
        ---shell
        python HabitTracker.py action=TestEverythingAutomatic user_id=USER_ID automatic_tests="False"
        ---

## Tests

it's necessary to create a user first, if you're not selecting the automatic full test
for analysing.
for normal analysing, it's necessary to create habits and actions before.

	---shell
	python HabitTracker.py action=TestEverything automatic_tests=True user_id=1
	---
