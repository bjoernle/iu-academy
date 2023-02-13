import datetime

import actions
import analyse
import files
import sqlite

inserted_habits = []


class TestHabitTracker:
    """ a class for testing
    """
    settings_json = ""
    show_db_actions = True
    automatic_tests = False

    def __init__(self, settings):
        """ add a user to table users

        :param settings: the new settings_json
        :return: no return, just some text
        """
        self.settings_json = settings
        # print(settings["action"])
        if settings["runtime_settings"][0]["show_db_actions"] == "True":
            self.show_db_actions = True
        else:
            self.show_db_actions = False

        if settings["runtime_settings"][0]["automatic_tests"] == "True":
            self.automatic_tests = True
        else:
            self.automatic_tests = False

    def test_everything(self, path):
        """ test all things you that you can test
        :param path: path to database file
        :return: no return, just some text output
        """
        if self.automatic_tests == "true" or self.automatic_tests == "True":
            print("--- AUTOMATIC TESTS ---")

        print("-------------------------------------")
        print("Test Database")
        print("-------------------------------------")
        print()
        self.test_database(path, self.show_db_actions)

        print("-------------------------------------")
        print("Test user related actions")
        print("(Signup, Login, Delete)")
        print("-------------------------------------")
        print()
        self.test_user_actions(path, self.settings_json)

        #print(self.settings_json["user"][0]["user_id"])
        print()
        print("-------------------------------------")
        print("Analyse all produced data of test-user")
        print("-------------------------------------")
        print()
        analyse_class = analyse.AnalyseData(path, self.settings_json)
        print()
        print("-------------------------------------")
        print("Give full analyse")
        print("-------------------------------------")
        print()
        analyse_class.give_full_analyse()
        print()
        print("-------------------------------------")
        print("Give all of same period")
        print("-------------------------------------")
        print()
        analyse_class.give_all_same_period()
        print()
        print("-------------------------------------")
        print("Give longest series")
        print("-------------------------------------")
        print()        
        analyse_class.give_longest_serie()
        print()
        print("-------------------------------------")
        print("Give serie 'tooth brushing' (habit_name=tooth³brushing)")
        print("-------------------------------------")
        print()
        analyse_class.give_longest_serie("tooth brushing")
        #analyse_class.give_summary()
        if self.settings_json["runtime_settings"][0]["automatic_tests"] == "True":
            files.delete_file(path)
            print("Test-database deleted.")
        else:
            print("Please press y (yes) and then enter if you want to delete the test database.")
            if input() == "y":
                files.delete_file(path)
            else:
                print("The test database file 'test.sqlite3' wasn't deleted.")

        print()
        print(":) :) :) Everything went well as possible!!! :) :) :)")

    def test_user_actions(self, path, settings_json):
        """ test all user actions
        :param path: path to database file, automatic: bool
        :return: no return, just some text
        """
        print("Create User 'TestUser'")
        settings_json["user"][0]["user_name"] = "TestUser"
        settings_json["user"][0]["user_password"] = "TestPassword12$%&"
        automatic = self.automatic_tests
        if not automatic:
            print("Please press enter for adding a user for login.")
            input()
        else:
            print("Add user for login.")
        actions.add_user(path, settings_json)
        print("Login")
        if not automatic:
            print("Please press enter for getting the user from database.")
            input()
        else:
            print("Add user for login.")
        user = actions.get_user(path, settings_json)
        #print(user[0])
        if len(user) > 0:
            print("User logged in.")
            print(user)

        else:
            print("Found no user.")
        print("user id for deleting: "+str(user[0][0]))
        sqlite.delete_from_table_by_id(path, "users", str(user[0][0]))
        print("Row with id " + str(user[0][0])+" deleted.")

    def test_database(self, path, show_db_action):
        """ test all things you that you can test from database
        :param path: path to database file, automatic: bool
        :return: no return, just some text
        """
        automatic = self.automatic_tests
        if automatic:
            print("Creating the table structure.")
        else:
            print("Please press enter for creating the table structure.")
            input()
        sqlite.create_tables_habittracker(path)
        print("Tables 'users', 'habits' and 'habits_lasttime' created in SQLite file.")
        print("Located at path: "+str(path))
        print()
        if not automatic:
            print("Please press enter for inserting user.")
            input()
        else:
            print("Inserting user.")
        user_id = self.insert_test_user(path)
        print()
        if not automatic:
            print("Please press enter for inserting 5 habits.")
            input()
        else:
            print("Inserting 5 habits")
        self.insert_test_habits(path, user_id)
        print()
        if not automatic:
            print("Please press enter for edit the first habit (name, description).")
            input()
        else:
            print("Edit the first habit (name, description)")
        # print(show_db_action)
        print("before:")
        sqlite.get_sqlite_vals_by_columns_and_values(path, "habits", "id", str(inserted_habits[0]))
        sqlite.edit_row_by_columns_and_values(path, "habits", "name, description",
                                              "tooth brushing, brush your teethes!", "id",
                                              str(inserted_habits[0]), show_db_action)
        print()
        if not automatic:
            print("Please press enter for inserting 6 done habits.")
            input()
        else:
            print("Inserting 6 done habits.")
        self.insert_test_done_habits(path)
        print()
        if not automatic:
            print("Please press y (yes) and then enter if you want to delete the last inserted row.")
            if input() == "y":
                sqlite.delete_last_row(path, "habits_lasttime", show_db_action)
                print()
        else:
            print("Don't deleted the database.")
        if not automatic:
            print("Please press enter for show inserted Data.")
            input()
        else:
            print("Show inserted Data.")
        self.show_all_of_user(path, str(user_id))

    def insert_test_user(self, path):
        """ insert a test user
        :param path: path to database file
        :return: no return, just some text
        """
        cols = "name, password, created"
        vals = "testUser,testPwd,1970-01-01"
        user_id = sqlite.insert_to_sqlite_table(path, "users", cols, vals, self.show_db_actions)
        print("ID of the new user: " + str(user_id))
        return str(user_id)

    def insert_test_habits(self, path, user_id):
        """ insert test habits
        :param path: path to database file, user_id: id in table users
        :return: no return, just some text
        """
        cols = """user_id, name, description, timespan, date_start, date_end, target_time_start, 
        target_time_end, target_duration, target_repeats, completed, created"""
        vals_array = []
        vals_array.append(str(user_id) + ", toot brushin, brush your toothes 3 minutes, daily, 2023-01-01, 2023-12-31, 06:00, 07:00, 00:03, 1, 0, 2023-01-01")
        vals_array.append(str(user_id) + ", read informatic articles, heise and so on, daily, 2023-01-01, 2023-12-31, 06:00, 07:00, 00:10, 1, 0, 2023-01-01")
        vals_array.append(str(user_id) + ", go jogging, something for your health!, weekly, 2023-01-01, 2023-12-31, 18:00, 19:00, 00:30, 2, 0, 2023-01-01")
        vals_array.append(str(user_id) + ", call your grandmother, for your family.., weekly, 2023-01-01, 2023-12-31, 17:00, 18:00, 00:15, 2, 0, 2023-01-01")
        vals_array.append(str(user_id) + ", go to gym, something for your health!, monthly, 2023-01-01, 2023-12-31, 18:00, 19:00, 01:30, 2, 0, 2023-01-01")

        inserted_id = 0
        for vals in vals_array:
            inserted_id = sqlite.insert_to_sqlite_table(path, "habits", cols, vals, self.show_db_actions)
            inserted_habits.append(inserted_id)
            print("ID of the new habit: " + str(inserted_id))


    def insert_test_done_habits(self, path):
        """ insert done habits
        :param path: path to database file
        :return: no return, just some text
        """
        cols = "habit_id, start_datetime, end_datetime, created, modified"
        datetime_now = datetime.datetime.now()

        #dt=datetime.datetime.strptime("2023-01-01 06:06", '%Y-%m-%d %H:%M')
        dt=datetime.datetime(2023, 1, 1, 6, 15)
        for habit_id in inserted_habits:
            dt_new= dt + datetime.timedelta(days=1)
            # print("Habit-ID: "+str(habit_id))
            vals = str(habit_id) + ", "+str(dt)+", "+str(dt_new)+", "+str(datetime_now)+", "+str(datetime_now)
            lasttime_id = sqlite.insert_to_sqlite_table(path, "habits_lasttime", cols, vals, self.show_db_actions)
            print("ID in database: " + str(lasttime_id))
        vals = str(inserted_habits[-1]) + ", 2023-01-02 06:15, 2023-01-02 07:00, "+str(datetime_now)+", "+str(datetime_now)
        lasttime_id = sqlite.insert_to_sqlite_table(path, "habits_lasttime", cols, vals, self.show_db_actions)
        print("ID in database: " + str(lasttime_id))

    def show_all(self, path):
        """ show everything from database
        :param path: path to database file
        :return: no return, just some text
        """
        import sqlite
        print("users :")
        sqlite.get_all_from_table(path, "users", self.show_db_actions)
        print()
        print("habits:")
        sqlite.get_all_from_table(path, "habits", self.show_db_actions)
        print()
        print("habit done:")
        sqlite.get_all_from_table(path, "habits_lasttime", self.show_db_actions)

    def show_all_of_user(self, path, user_id="0"):
        """ show everything from user
        :param path: path to database file, user_id: id in database table users
        :return: no return, just some text
        """
        import sqlite
        user = sqlite.get_sqlite_vals_by_columns_and_values(path, "users", "id", user_id, self.show_db_actions)
        print(len(user))
        if len(user) != 0:
            name = user[0][1]
            print()
            print("user :" + name)
            habits = sqlite.get_sqlite_vals_by_columns_and_values(path, "habits", "user_id", user_id,
                                                                  self.show_db_actions)
            print()
            print("habits:")
            for habit in habits:
                habit_id = habit[0]
                habit_name = habit[2]
                print()
                print("Name of Habit: " + habit_name)
                print("Habit done last: ")
                habit_dones = sqlite.get_sqlite_vals_by_columns_and_values(path, "habits_lasttime", "habit_id",
                                                                           str(habit_id), self.show_db_actions)
                for done_habit in habit_dones:
                    print(done_habit)
                print()
        else:
            if len(user_id) == 0:
                print("For showing everything of a user you have to give a user-id. For example..")
                print("python HabitTracker.py action=ShowAllOfUser user_id=1")
            else:
                print(
                    "There where no user with user-id=" + user_id +
                    " in the test database. Did you filled it? For example..")
                print("python HabitTracker.py action=TestEverything show_db_actions=False")
