import sqlite
import sys
import datetime
import time

import system
import globals
import files
import datamart
import settingsChanger

folder_separator = system.get_folder_separator()
current_path = str(globals.get_current_path())
db_path = current_path + folder_separator + "airbnb.db"
given_attributes = sys.argv
settings_json = globals.get_settings_json(folder_separator)

def eli():
    """
    Choose the way to handle next steps
    """

    global settings_json

    if len(given_attributes) > 1:
        settings_json = settingsChanger.set_new_settings(settings_json, given_attributes)
    else:
        print("You choosed no action.. Quitting the program.")
        quit()

    
    if not files.exist_file(current_path+folder_separator+"airbnb.db"):
        print("Found no database. Creating database and some entities..")
        sqlite.create_tables(db_path)
        sqlite.insert_data()
        print()

    #just for entertainment while waiting
    waiting_time = int(settings_json["runtime_settings"][0]["wait"])
    if waiting_time > 0:
        import time
        time.sleep(waiting_time)

    #choose action
    if settings_json["action"] == "LoginUser":
        rows = sqlite.get_user(db_path, settings_json)
        if len(rows) > 0:
            print("User logged in ("+str(rows[0][1])+"-"+str(rows[0][0])+")")
        else:
            print("Something where wrong")
    elif settings_json["action"] == "SignupUser":
        import json
        user_name = settings_json["user"][0]["user_name"]
        user_password = settings_json["user"][0]["user_password"]
        if user_name != "" and user_password != "":
            created = datetime.now()
            cols = "name, password, created"
            vals = user_name + "," + user_password + "," + str(created)
            sqlite.insert_to_sqlite_table(db_path, "users", cols, vals, False)
            user = sqlite.get_sqlite_vals_by_columns_and_values(db_path, "users", cols, vals, False)
            print("Created user.")
            return json.dumps(user)

    elif settings_json["action"] == "StartServer":
        from threading import Thread
        import time
        thread = Thread(target = system.start_server) #, args = (10, )
        thread.start()
        time.sleep(3)
        thread1 = Thread(target = system.open_browser)
        thread1.start()

    elif settings_json["action"] == "GetComments":
        datamart.get_comments_by_username_and_usertype("Alexander", "Guest")
    elif settings_json["action"] == "GetCommentsInDateRange":
        datamart.get_comments_of_places_rented_in_daterange("2023-02-28","2023-03-03")
    elif settings_json["action"] == "GetPhotosByUsertype":
        datamart.get_photos_by_usertype("Host")
    elif settings_json["action"] == "GetPhotosRatesHigherNumber":
        datamart.get_photos_with_rates_higher_number(3)
    elif settings_json["action"] == "PlacesEvaluatedByBothUsertypes":
        datamart.get_places_evaluated_by_both_usertypes()
    elif settings_json["action"] == "PlacesInCityAndTimespan":
        datamart.get_places_in_city_and_datespan("Munich", "2024-03-01", "2024-03-04")
    elif settings_json["action"] == "PlacesRentedByUsertype":
        datamart.get_places_that_was_rented_by_usertype("Guest")
    elif settings_json["action"] == "PlacesUnoccupiedNow":
        datamart.get_places_unoccupied_now()  
    elif settings_json["action"] == "TestEverything":
        datamart.get_comments_by_username_and_usertype("Alexander", "Guest")
        datamart.get_comments_of_places_rented_in_daterange("2023-03-01","2023-03-03")
        datamart.get_photos_by_usertype("Host")
        datamart.get_photos_with_rates_higher_number(3)
        datamart.get_places_evaluated_by_both_usertypes()
        datamart.get_places_in_city_and_datespan("Munich", "2023-03-01", "2023-03-04")
        datamart.get_places_that_was_rented_by_usertype("Guest")
        datamart.get_places_unoccupied_now()
    elif settings_json["action"] == "ShowAll":
        sqlite.get_all_from_table(db_path, "Users")
        sqlite.get_all_from_table(db_path, "UserType")
        sqlite.get_all_from_table(db_path, "Rentals")
        sqlite.get_all_from_table(db_path, "RentablePlaces")
        sqlite.get_all_from_table(db_path, "PlaceEvaluations")
        sqlite.get_all_from_table(db_path, "GuestEvaluations")
        sqlite.get_all_from_table(db_path, "Photos")
        sqlite.get_all_from_table(db_path, "Comments")


    else:
        print("No action was given.")
        

    #sqlite.to_csv()


if __name__ == '__main__':
    eli()
