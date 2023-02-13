def set_new_settings(settings, parameters):
    """ get the given attributes and changes the settings_json

    :param parameters: parameters that was given
    :param settings: the original settings from textfiles

    :return: the new settings_json
    """

    count_of_values = 0
    count_of_onekey_parameter = 0
    onekey_parameters_string = ""
    # print("------------")
    messages = []
    for parameter in parameters:

        if parameter != "HabitTracker.py":

            key_val = parameter.split("=")

            if len(key_val) > 1:
                #print(key_val[0]+"="+key_val[1])
                if key_val[1] != "":
                    count_of_values = count_of_values+1

                    # get
                    if key_val[0] == "action":
                        messages.append("using-action:" + key_val[1])
                        settings["action"] = key_val[1]

                    elif key_val[0] == "habit_id":
                        messages.append("Using habit-id:" + key_val[1])
                        settings["habit_id"] = key_val[1]
                    elif key_val[0] == "user_name":
                        messages.append("user:" + key_val[1])
                        settings["user"][0]["user_name"] = key_val[1]
                    elif key_val[0] == "user_password":
                        # print("Password:" + key_val[1])
                        settings["user"][0]["user_password"] = key_val[1]
                    elif key_val[0] == "user_id":
                        messages.append("User ID:" + key_val[1])
                        settings["user"][0]["user_id"] = key_val[1]

                    elif key_val[0] == "habit_name":
                        key_val[1] = key_val[1].replace("³", " ")
                        messages.append("Habit Name:" + key_val[1])
                        settings["habit"][0]["name"] = key_val[1]
                    elif key_val[0] == "habit_description":
                        key_val[1] = key_val[1].replace("³", " ")
                        messages.append("Habit description:" + key_val[1])
                        settings["habit"][0]["description"] = key_val[1]
                    elif key_val[0] == "habit_timespan":
                        messages.append("Habit timespan:" + key_val[1])
                        settings["habit"][0]["timespan"] = key_val[1]

                    elif key_val[0] == "habit_date_start":
                        messages.append("Habit date start:" + key_val[1])
                        settings["habit"][0]["date_start"] = key_val[1]
                    elif key_val[0] == "habit_date_end":
                        messages.append("Habit date end:" + key_val[1])
                        settings["habit"][0]["date_end"] = key_val[1]

                    elif key_val[0] == "habit_target_time_start":
                        messages.append("Habit target time start:" + key_val[1])
                        settings["habit"][0]["target_time_start"] = key_val[1]
                    elif key_val[0] == "habit_target_time_end":
                        messages.append("Habit target time end:" + key_val[1])
                        settings["habit"][0]["target_time_end"] = key_val[1]
                    elif key_val[0] == "habit_target_duration":
                        messages.append("Habit target duration:" + key_val[1])
                        settings["habit"][0]["target_duration"] = key_val[1]
                    elif key_val[0] == "habit_target_repeats":
                        messages.append("Habit target repeats:" + key_val[1])
                        settings["habit"][0]["target_repeats"] = key_val[1]

                    elif key_val[0] == "habit_id":
                        messages.append("Habit ID:" + key_val[1])
                        settings["habit_lasttime"][0]["habit_id"] = key_val[1]
                    elif key_val[0] == "start_datetime":
                        messages.append("Habit start datetime:" + key_val[1])
                        settings["habit_lasttime"][0]["start_datetime"] = key_val[1]
                    elif key_val[0] == "end_datetime":
                        print("Habit start datetime:" + key_val[1])
                        settings["habit_lasttime"][0]["end_datetime"] = key_val[1]
                    elif key_val[0] == "created":
                        messages.append("Habit created:" + key_val[1])
                        settings["habit_lasttime"][0]["created"] = key_val[1]

                    elif key_val[0] == "wait":
                        messages.append("Wait seconds:" + key_val[1])
                        settings["runtime_settings"][0]["wait"] = key_val[1]
                    elif key_val[0] == "automatic_tests":
                        messages.append("Automatic tests: " + key_val[1])
                        settings["runtime_settings"][0]["automatic_tests"] = key_val[1]
                    elif key_val[0] == "show_messages":
                        messages.append("Show messages: " + key_val[1])
                        settings["runtime_settings"][0]["show_messages"] = key_val[1]
                    elif key_val[0] == "return_json":
                        messages.append("Return json (to website):" + key_val[1])
                        settings["runtime_settings"][0]["return_json"] = key_val[1]
                    else:
                        messages.append("A key wasn't known ("+key_val[0]+"..")

            elif len(key_val) == 1:
                count_of_onekey_parameter += 1
                onekey_parameters_string += "'"+key_val[0]+"', "

    show_messages = settings["runtime_settings"][0]["show_messages"]
    if show_messages == "true" or show_messages == "True":
        onekey_parameters_string = onekey_parameters_string[:-2]
        print(str(count_of_values) + " given key-value pairs for running this Job.")
        if count_of_onekey_parameter > 1:
            print(
                str(count_of_onekey_parameter) + " given values for running this Job. (" + onekey_parameters_string + ")")
            for message in messages:
                print(message)

        for message in messages:
            print(message)
    return settings
