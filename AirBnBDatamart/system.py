import datetime
import os
import platform

def get_folder_separator():
    import os
    folder_separator = ""
    if os.name == 'nt':
        return "\\"
    else:
        return "/"


def intTryParse(value):
    try:
        return int(value)
    except ValueError:
        return value


def clear_screen():
    # import only system from os
    from os import system, name
    # import sleep to show output for some time period
    from time import sleep
    # define our clear function
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    # sleep for 4 seconds after printing output
    sleep(4)
    # now call function we defined above
    clear()
	
def create_windows_task_in_taskplan():
    import datetime
    import win32com.client

    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')
    task_def = scheduler.NewTask(0)

    # Create trigger
    start_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
    TASK_TRIGGER_TIME = 1
    trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)
    trigger.StartBoundary = start_time.isoformat()

    # Create action
    TASK_ACTION_EXEC = 0
    action = task_def.Actions.Create(TASK_ACTION_EXEC)
    action.ID = 'DO NOTHING'
    action.Path = 'cmd.exe'
    action.Arguments = '/c "exit"'

    # Set parameters
    task_def.RegistrationInfo.Description = 'Test Task'
    task_def.Settings.Enabled = True
    task_def.Settings.StopIfGoingOnBatteries = False

    # Register task
    # If task already exists, it will be updated
    TASK_CREATE_OR_UPDATE = 6
    TASK_LOGON_NONE = 0
    root_folder.RegisterTaskDefinition(
        'Test Task',  # Task name
        task_def,
        TASK_CREATE_OR_UPDATE,
        '',  # No user
        '',  # No password
        TASK_LOGON_NONE)

def open_browser():
    import webbrowser
    ip = str(get_own_ip_address())
    url = "http://"+ip+":5000"

    webbrowser.open(url, new=0, autoraise=True)

def start_server():
    if platform.system() == "Windows":
        os.system("start /wait cmd /c python server.py")
    if platform.system() == "Linux":
        os.system("gnome-terminal -e 'bash -c python server.py'")

def string_to_datetime(datestring):
    d=""
    try:
        d = datetime.datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S")
        
    except ValueError:
        try:
            d = datetime.datetime.strptime(datestring, "%Y-%m-%d %H:%M")
        except ValueError:
            try:
                d = datetime.datetime.strptime(datestring, "%Y-%m-%d")
            except:
                d="date not transformable"
    finally:
        return d
            
def get_own_ip_address():
    import socket
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    return IPAddr