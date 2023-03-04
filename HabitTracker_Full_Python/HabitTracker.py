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
            cols = "name, password, created"
            vals = user_name + "," + user_password + "," + str(created)
            sqlite.insert_to_sqlite_table(path, "users", cols, vals, False)
            user = sqlite.get_sqlite_vals_by_columns_and_values(path, "users", cols, vals, False)
            print("Created user.")
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
        db=path
        test.show_all(db)
    elif settings_json["action"] == "ShowAllOfUser":
        test = test_project.TestHabitTracker(settings_json)
        user_id = settings_json["user"][0]["user_id"]
        db=path
        test.show_all_of_user(db, str(user_id))
    elif settings_json["action"] == "TestEverything":
        test = test_project.TestHabitTracker(settings_json)
        db=test_path
        test.test_everything(db)
    elif settings_json["action"] == "TestEverythingAutomatic":
        test = test_project.TestHabitTracker(settings_json)
        db=path
        test.test_everything(db)

    elif settings_json["action"] == "StartServer":
        from threading import Thread
        thread = Thread(target = system.start_server) #, args = (10, )
        thread.start()
        time.sleep(3)
        thread1 = Thread(target = system.open_browser)
        thread1.start()

    else:
        print("No action was given.")


if __name__ == '__main__':
    eli()
