import analyse
import sqlite
import globals
import settingsChanger
import system
import test_project
import actions


import sys
from datetime import datetime
import time
import json
import os
import platform
import subprocess

folder_separator = system.get_folder_separator()
current_path = str(globals.get_current_path())

path = current_path + folder_separator + "db.sqlite3"
test_path = current_path + folder_separator + "test.sqlite3"

settings_json = globals.get_settings_json(folder_separator)
given_attributes = sys.argv
def eli():
    """
    Choose the way to handle next steps
    """
    global settings_json

    if len(given_attributes) > 1:
        settings_json = settingsChanger.set_new_settings(settings_json, given_attributes)
    sqlite.create_tables_habittracker(path)

    #just for entertainment while waiting
    waiting_time = int(settings_json["runtime_settings"][0]["wait"])
    if waiting_time > 0:
        time.sleep(waiting_time)

    #choose action
    if settings_json["action"] == "LoginUser":
        rows = actions.get_user(path, settings_json)
        if len(rows) > 0:
            print("User logged in ("+str(rows[0][1])+"-"+str(rows[0][0])+")")
        else:
            print("Something where wrong")
    elif settings_json["action"] == "SignupUser":
        user_name = settings_json["user"][0]["user_name"]
        user_password = settings_json["user"][0]["user_password"]
        if user_name != "" and user_password != "":
            created = datetime.now()
            cols = "username, password, created"
            vals = user_name + "," + user_password + "," + created
            sqlite.insert_to_sqlite_table(path, "users", cols, vals, False)
            user = sqlite.get_sqlite_vals_by_columns_and_values(path, "users", cols, vals, False)
            return json.dumps(user)

    elif settings_json["action"] == "AddHabit":
        actions.add_habit(path, settings_json)
    elif settings_json["action"] == "AddAction":
        actions.add_action(path, settings_json)

    elif settings_json["action"] == "GetHabitsOfUser":
        json_stuff = actions.get_habits_of_user(path, settings_json)
        if settings_json["runtime_settings"][0]["return_json"]:
            return json_stuff
    elif settings_json["action"] == "GetDoneHabitsOfUser":
        actions.get_done_habits_of_user(path, settings_json)

    elif settings_json["action"] == "AnalyseData":
        analyse_class = analyse.AnalyseData(path, settings_json)
        analyse_class.give_full_analyse()
    elif settings_json["action"] == "GiveAllSamePeriod":
        analyse_class = analyse.AnalyseData(path, settings_json)
        analyse_class.give_all_same_period()
    elif settings_json["action"] == "GiveLongestSerie":
        analyse_class = analyse.AnalyseData(path, settings_json)
        analyse_class.give_longest_serie(settings_json["habit"][0]["name"])     
    elif settings_json["action"] == "AnalyseDataSummary":
        analyse_class = analyse.AnalyseData(path, settings_json)
        analyse_class.give_summary()

    elif settings_json["action"] == "ShowAll":
        test = test_project.TestHabitTracker(settings_json)
        test.show_all(path)
    elif settings_json["action"] == "ShowAllOfUser":
        test = test_project.TestHabitTracker(settings_json)
        user_id = settings_json["user"][0]["user_id"]
        test.show_all_of_user(test_path, str(user_id))
    elif settings_json["action"] == "TestEverything":
        test = test_project.TestHabitTracker(settings_json)
        test.test_everything(test_path)
    elif settings_json["action"] == "TestEverythingAutomatic":
        test = test_project.TestHabitTracker(settings_json)
        test.test_everything(test_path)

    elif settings_json["action"] == "StartServer":
        import webbrowser
        ip = str(system.get_own_ip_address())
        url = "http://"+ip+":5000"
        webbrowser.open(url, new=0, autoraise=True)
        if platform.system() == "Windows":
            os.system("start /wait cmd /c python webserver.py")
        if platform.system() == "Linux":
            os.system("gnome-terminal -e 'bash -c python webserver.py'")
    else:
        print("No action was given.")


if __name__ == '__main__':
    eli()
