import system
import datetime

def set_new_settings(settings, parameters):
    """ get the given attributes and changes the settings_json

    :param parameters: parameters that was given
    :param settings: the original settings from textfiles

    :return: the new settings_json
    """

    count_of_values = 0
    count_of_onekey_parameter = 0
    onekey_parameters_string = ""
    messages = []
    for parameter in parameters:

        if parameter != "HabitTracker.py":

            key_val = parameter.split("=")

            if len(key_val) > 1:

                if key_val[1] != "":
                    count_of_values = count_of_values+1

                    if key_val[0] == "action":
                        messages.append("using-action:" + key_val[1])
                        settings["action"] = key_val[1]

                    #elif key_val[0] == "habit_id":
                    #    if key_val[1].isdigit():
                    #        messages.append("Using habit-id:" + key_val[1])
                    #        settings["habit_id"] = key_val[1]
                    #    else:
                    #        print("Habit-id is not a number.")
                            
                    elif key_val[0] == "user_name":
                        messages.append("user:" + key_val[1])
                        settings["user"][0]["user_name"] = key_val[1]
                    elif key_val[0] == "user_password":
                        settings["user"][0]["user_password"] = key_val[1]
                    elif key_val[0] == "user_id":
                        if key_val[1].isdigit():
                            messages.append("User ID:" + key_val[1])
                            settings["user"][0]["user_id"] = key_val[1]
                        else:
                            print("User-id is not a number.")

                    elif key_val[0] == "from":
                        if system.string_to_datetime(key_val[1])!="date not transformable":
                            messages.append("From:" + key_val[1])
                            settings["given_attrs"][0]["from"] = key_val[1]
                        else:
                            print("from is not a datetime.")
                    elif key_val[0] == "to":
                        if system.string_to_datetime(key_val[1])!="date not transformable":
                            messages.append("To:" + key_val[1])
                            settings["given_attrs"][0]["to"] = key_val[1]
                        else:
                            print("to is not a datetime.")
                    elif key_val[0] == "number":
                        if key_val[1].isdigit():
                            messages.append("Given number:" + key_val[1])
                            settings["given_attrs"][0]["number"] = key_val[1]
                        else:
                            print("User-id is not a number.")
                    elif key_val[0] == "city":
                            messages.append("User ID:" + key_val[1])
                            settings["given_attrs"][0]["city"] = key_val[1]
                    elif key_val[0] == "usertype":
                            messages.append("Usertype:" + key_val[1])
                            settings["given_attrs"][0]["usertype"] = key_val[1]
                    

                    elif key_val[0] == "wait":
                        if type(system.intTryParse(key_val[1])) == int:
                            messages.append("Wait seconds:" + key_val[1])
                            settings["runtime_settings"][0]["wait"] = key_val[1]
                        else:
                            print("The waiting time is not a number")
                            
                    elif key_val[0] == "automatic_tests":
                        if bool(key_val[1]) == True or bool(key_val[1]) == False:
                            messages.append("Automatic tests: " + key_val[1])
                            settings["runtime_settings"][0]["automatic_tests"] = key_val[1]
                        else: 
                            print("Automatic tests value have to be 'True' or 'False'")
                    elif key_val[0] == "show_messages":
                        if bool(key_val[1]) == True or bool(key_val[1]) == False:
                            messages.append("Show messages: " + key_val[1])
                            settings["runtime_settings"][0]["show_messages"] = key_val[1]
                        else: 
                            print("Show Messages value have to be 'True' or 'False'")
                    elif key_val[0] == "return_json":
                        if bool(key_val[1]) == True or bool(key_val[1]) == False:
                            messages.append("Return json (to website): " + key_val[1])
                            settings["runtime_settings"][0]["return_json"] = key_val[1]
                        else: 
                            print("Return json value have to be 'True' or 'False'")
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
