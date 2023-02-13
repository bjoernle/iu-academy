def add_user(path, settings_json):
    """ add a user to table users
    :param settings_json: the new settings_json
    :param path: path to database file
    :return: no return, just some text
    """
    import sqlite
    from datetime import datetime

    name = settings_json["user"][0]["user_name"]
    pwd = settings_json["user"][0]["user_password"]
    created = datetime.now()

    if name != "" and pwd != "":
        sqlite.insert_to_sqlite_table(path, "users", "name, password, created, modified", name + ", " + pwd + ", " + str(created) + ", " + str(created))


def get_user(path, settings_json):
    """ add a user to table users

    :param settings_json: the new settings_json
    :param path: path to database file
    :return: no return, just some text
    """
    import sqlite

    name = settings_json["user"][0]["user_name"]
    pwd = settings_json["user"][0]["user_password"]

    if name != "" and pwd != "":
        return sqlite.get_sqlite_vals_by_columns_and_values(path, "users", "name, password", name + ", " + pwd)


def add_habit(path, settings_json):
    """ add a habit to table habits

    :param settings_json: the new settings_json
    :param path: path to database file
    :return: no return, just some text
    """
    from datetime import datetime
    import sqlite

    user_id = settings_json["user"][0]["user_id"]
    print("..id:" + user_id)
    name = settings_json["habit"][0]["name"]
    description = settings_json["habit"][0]["description"]
    timespan = settings_json["habit"][0]["timespan"]
    date_start = settings_json["habit"][0]["date_start"]
    date_end = settings_json["habit"][0]["date_end"]
    target_time_start = settings_json["habit"][0]["target_time_start"]
    target_time_end = settings_json["habit"][0]["target_time_end"]
    target_duration = settings_json["habit"][0]["target_duration"]
    target_repeats = settings_json["habit"][0]["target_repeats"]
    created = str(datetime.now())

    if user_id != "" and name != "" and description != "" and timespan != "" and target_time_start != "" and target_time_end != "" and target_duration != "" and target_repeats != "":
        sqlite.insert_to_sqlite_table(path, "habits",
                                      "user_id, name, description, timespan, date_start, date_end, target_time_start, target_time_end, target_duration, target_repeats, created",
                                      user_id + "," + name + "," + description + "," + timespan + "," + date_start + "," + date_end + "," + target_time_start + "," + target_time_end + "," + target_duration + "," + target_repeats + "," + created)
    else:
        print("At least one value of habits isn't setted.")


def add_action(path, settings_json):
    """ add a action to table habits_lasttime

    :param settings_json: the new settings_json
    :param path: path to database file
    :return: no return, just some text
    """
    import sqlite
    habit_id = settings_json["habit_lasttime"][0]["habit_id"]
    start_datetime = settings_json["habit_lasttime"][0]["start_datetime"]
    end_datetime = settings_json["habit_lasttime"][0]["end_datetime"]
    created = settings_json["habit_lasttime"][0]["created"]

    if habit_id != "" and start_datetime != "" and end_datetime != "" and created != "":
        sqlite.insert_to_sqlite_table(path, "habits", "habit_id, start_datetime, end_datetime, created",
                                      habit_id + ", " + start_datetime + ", " + end_datetime + ", " + created)
    else:
        print("At least one value of habits-actions isn't setted.")


def get_habits_of_user(path, settings_json, return_json="True"):
    """ add a user to table users

    :param settings_json: the new settings_json
    :param path: path to database file
    :param return_json: bool like "True"
    :return: if wanted, json return of quered data
    """
    import sqlite

    user_id = settings_json["user"][0]["user_id"]
    show_db_actions = settings_json["runtime_settings"][0]["show_db_actions"]
    rows = sqlite.get_sqlite_vals_by_columns_and_values(path, "habits", "user_id", user_id, show_db_actions)
    if len(rows) > 0:
        if return_json == "True":
            print("return json")
            # return json.dumps(rows)
        else:
            for row in rows:
                print(row)


def get_done_habits_of_user(path, settings_json, return_json=True):
    """ add a user to table users

    :param settings_json: the new settings_json
    :param path: path to database file
    :param return_json: bool like "True"
    :return: if wanted, json return of quered data
    """
    import sqlite
    import json
    habit_id = settings_json["habit_id"]
    show_db_actions = settings_json["runtime_settings"][0]["show_db_actions"]
    rows = sqlite.get_sqlite_vals_by_columns_and_values(path, "habits_lasttime", "habit_id", habit_id, show_db_actions)
    if return_json:
        return json.dumps(rows)
    else:
        for row in rows:
            print(row)


def get_from_user_by_timespan(path, settings_json, return_json=True):
    """ add a user to table users

    :param settings_json: the new settings_json
    :param path: path to database file
    :param return_json: bool like "True"
    :return: if wanted, json return of quered data
    """
    import sqlite
    import json
    user_id = settings_json["user"][0]["user_id"]
    show_db_actions = settings_json["runtime_settings"][0]["show_db_actions"]
    rows = sqlite.get_sqlite_vals_by_columns_and_values(path, "habits", "habit_id", user_id, show_db_actions)
    if return_json:
        return json.dumps(rows)
    else:
        for row in rows:
            print(row)