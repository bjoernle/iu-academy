import system

import json
from datetime import datetime, date
from dateutil import relativedelta

class AnalyseData:
    analysed_data = {}
    path = ""
    settings_json = ""
    def __init__(self, path, settings_json):
        self.path = path
        self.settings_json = settings_json
        self.full_analyse_user_records_by_id()

    def give_all_same_period(self, period=""):
        all_data = self.analysed_data
        yearly_list = []
        monthly_list = []
        weekly_list = []
        daily_list = []
        for habit in all_data:
            habit_attributes = self.analysed_data[habit]
            if habit_attributes["given_attrs"]["timespan"]=="yearly":
                yearly_list.append(habit)
            elif habit_attributes["given_attrs"]["timespan"]=="monthly":   
                monthly_list.append(habit)
            elif habit_attributes["given_attrs"]["timespan"]=="weekly":   
                weekly_list.append(habit)
            elif habit_attributes["given_attrs"]["timespan"]=="daily":   
                daily_list.append(habit)
        print("Same period:")
        print("Yearly: ("+str(len(yearly_list))+")")
        for list_item in yearly_list:
            print(list_item)
        print("Monthly: ("+str(len(monthly_list))+")")
        for list_item in monthly_list:
            print(list_item)
        print("Weekly: ("+str(len(weekly_list))+")")
        for list_item in weekly_list:
            print(list_item)
        print("Daily: ("+str(len(daily_list))+")")
        for list_item in daily_list:
            print(list_item)

    #def give_longest_series(self):
        
    #    print()

    def give_longest_serie(self, habit_name=""):
        all_data = self.analysed_data
        #if habit_name != "":
        for habit in all_data:
            if habit_name != "":
                habit=habit_name
                print(habit)
            #print(self.analysed_data)
            timespan = self.analysed_data[habit]["given_attrs"]["timespan"]
            #self.analysed_data[habit]["analysed_data"]["dones"]

            print("Habit: "+habit)
            lst = []
            for last_done in dict(self.analysed_data[habit]["analysed_data"]["dones"]).items():
                lst.append(str(last_done[1]["from_time"]))

            new_lst = sorted(datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in lst)
            last_date=""
            counter=0
            series={}
            #series[counter]=[]
            for action_date in new_lst:
                if last_date =="":
                    last_date=action_date
                if not series:
                    series[counter]=[]
                    series[counter].append(action_date)
                #print(str(last_date)+" "+str(action_date))

                if timespan == "yearly":
                    #print(str((action_date.year - last_date.year)))
                    if last_date != "":
                        if action_date.year - last_date.year == 0:
                            pass
                        elif action_date.year - last_date.year == 1:
                            series[counter].append(action_date)
                        else:
                            #last_date=action_date
                            #print(str(relativedelta.relativedelta(action_date, last_date).years))
                            counter=counter+1
                            series[counter]=[]
                            series[counter].append(action_date)
                    else:
                        series[counter].append(action_date)
                elif timespan == "monthly":
                    if last_date !="" and relativedelta.relativedelta(action_date, last_date).months == 1:
                        series[counter].append(action_date)
                    else:
                        counter=counter+1
                        series[counter]=[]
                        series[counter].append(action_date)
                elif timespan == "weekly":
                    if last_date !="" and relativedelta.relativedelta(action_date, last_date).weeks == 1:
                        series[counter].append(action_date)
                    else:
                        counter=counter+1
                        series[counter]=[]
                        series[counter].append(action_date)
                elif timespan == "daily":
                    if last_date != "":
                        if last_date !="" and relativedelta.relativedelta(action_date, last_date).days == 0:
                            pass
                        elif last_date !="" and relativedelta.relativedelta(action_date, last_date).days == 1:
                            #print(str(relativedelta.relativedelta(action_date, last_date).days))
                            series[counter].append(action_date)
                        else:
                            counter=counter+1
                            series[counter]=[]
                            series[counter].append(action_date)
                #print(dates[0])
                last_date=action_date
            max_series=0
            max_series_from=""
            max_series_to=""
            min_series=0
            min_series_from=""
            min_series_to=""
            if len(series.items())>0:
                print("Count of series: "+str(len(series.items())))
                cnt=0
                for series_dates in series.items():
                    cnt=cnt+1
                    print(str(cnt)+". serie: "+str(len(list(series_dates[1]))))
                    if max_series < (len(list(series_dates[1]))):
                        max_entry=cnt-1
                        max_series = (len(list(series_dates[1])))
                        max_series_from = list(series_dates[1])[0]
                        max_series_to = list(series_dates[1])[len(list(series_dates[1]))-1]
                    if max_series > (len(list(series_dates[1]))):
                        min_entry=cnt-1
                        min_series = (len(list(series_dates[1])))
                        min_series_from = list(series_dates[1])[0]
                        min_series_to = list(series_dates[1])[len(list(series_dates[1]))-1]
                if(min_series>0):
                    print("Min repeats: "+str(min_series)+" times, on "+str(min_entry)+". attempt ("+str(min_series_from)+" to "+str(min_series_to)+")")
                print("Max repeats: "+str(max_series)+" times, on "+str(max_entry)+". attempt ("+str(max_series_from)+" to "+str(max_series_to)+")")
                print()
            else:
                print("currently no repeats")    
            
            if habit_name != "":
                break
            #print(str(start_date)+" to "+str(end_date))

        #print(lst)
    
    def give_summary(self):
        all_data = self.analysed_data

    def give_full_analyse(self):
        all_data = self.analysed_data

        for habit in all_data:
            habit_attributes = self.analysed_data[habit]
            print("Habit: "+habit)

            print()

            print(str(habit_attributes["analysed_data"]["days_since"]) + " days since startdate. (" + str(habit_attributes["given_attrs"]["start_date"]) + ")")
            print("days left: " + str(habit_attributes["analysed_data"]["days_left"]) + " to enddate. (" + str(habit_attributes["given_attrs"]["end_date"]) + ")")
            print("You have " + str(habit_attributes["analysed_data"]["actions_done"]) + " of " + str(
                habit_attributes["given_attrs"]["target_repeats"]) + " needed actions. (" + habit_attributes["analysed_data"]["actions_left"] + " left)")

            print()

            print("Given attributes:")
            for habit_attribute in habit_attributes["given_attrs"]:
                print(habit_attribute + " = " + str(habit_attributes["given_attrs"][habit_attribute]))

            print()

            print("Analysed data:")

            #print(dict(habit_attributes["analysed_data"]["dones"]))
            actions_counter = 0
            for habit_attribute in dict(habit_attributes["analysed_data"]["dones"]).items():
                actions_counter = actions_counter + 1
                print()
                print(str(actions_counter)+". action:")
                for attribute in dict(habit_attribute[1]).items():
                    print(str(attribute[0])+" = "+str(attribute[1]))

            for habit_attribute in habit_attributes["analysed_data"]:
                if habit_attribute != "dones":
                    print(habit_attribute + " = " + str(habit_attributes["analysed_data"][habit_attribute]))
                else:
                    print()
                    #for done_action in habit_attributes["analysed_data"][habit_attribute]:
                        #habit_attribute = habit_attribute
                        #print("blubb: " + str(type(done_action)))
                        #print(done_action)
                        #print(done_action[0]+" = "+done_action[1])
                # print(str(x) + ". of needed " + str(habit_attributes["given_attrs"]["target_repeats"]) + " entries, created: " + str(habit_attributes["given_attrs"]["dones"]["created"]) + "):")

            print()
            print("--------------------------------------------------")
            print()


    def full_analyse_user_records_by_id(self, return_json="True"):
        """
        Calculate the event of the counter

        :param path: path to database file
        :param settings_json: the new settings_json
        :param return_json: bool like "True"

        :return:
        """
        import sqlite
        from datetime import timedelta
        from datetime import datetime
        from datetime import date

        user_id = self.settings_json["user"][0]["user_id"]
        show_db_actions = self.settings_json["runtime_settings"][0]["show_db_actions"]
        user = sqlite.get_sqlite_vals_by_columns_and_values(self.path, "users", "id", user_id, show_db_actions)

        full_target_duration = timedelta()
        if len(user) != 0:
            name = user[0][1]
            #print()
            #print("user :" + name)
            habits = sqlite.get_sqlite_vals_by_columns_and_values(self.path, "habits", "user_id", user_id,
                                                                  show_db_actions)

            for habit in habits:

                habit_id = habit[0]
                habit_name = habit[2]

                habit_description = habit[3]
                habit_timespan = habit[4]

                self.analysed_data[habit_name] = {}
                self.analysed_data[habit_name]["given_attrs"] = {}
                self.analysed_data[habit_name]["given_attrs"]["dones"] = {}
                self.analysed_data[habit_name]["analysed_data"] = {}
                self.analysed_data[habit_name]["analysed_data"]["dones"] = {}
                # print(self.analysed_data)

                timespan = habit[4]
                self.analysed_data[habit_name]["given_attrs"]["timespan"] = timespan
                start_date = datetime.strptime(habit[5], '%Y-%m-%d')
                self.analysed_data[habit_name]["given_attrs"]["start_date"] = start_date
                end_date = datetime.strptime(habit[6], '%Y-%m-%d')
                self.analysed_data[habit_name]["given_attrs"]["end_date"] = end_date
                target_time_start = datetime.strptime(habit[7], '%H:%M').time()
                self.analysed_data[habit_name]["given_attrs"]["target_time_start"] = target_time_start
                target_time_end = datetime.strptime(habit[8], '%H:%M').time()
                self.analysed_data[habit_name]["given_attrs"]["target_time_end"] = target_time_end
                target_duration = ""
                try:
                    target_duration = datetime.strptime(habit[9], '%H:%M').time()
                except ValueError:
                    target_duration = datetime.strptime(habit[9], '%d:%H:%M').time()

                self.analysed_data[habit_name]["given_attrs"]["target_duration"] = target_duration
                target_repeats = int(habit[10])
                self.analysed_data[habit_name]["given_attrs"]["target_repeats"] = target_repeats



                #full_target_duration = timedelta()
                x = target_repeats
                while x != 0:
                    full_target_duration = full_target_duration + timedelta(hours=target_duration.hour, minutes=target_duration.minute)
                    x = x - 1

                #print()
                #print("Habit: " + habit_name+" ("+habit_description+")")
                #print("Habit done last times: ")
                habit_dones = sqlite.get_sqlite_vals_by_columns_and_values(self.path, "habits_lasttime", "habit_id",
                                                                           str(habit_id), show_db_actions)

                days_since = date.today() - datetime.date(start_date)
                self.analysed_data[habit_name]["analysed_data"]["days_since"] = days_since.days
                days_left = datetime.date(end_date) - date.today()
                self.analysed_data[habit_name]["analysed_data"]["days_left"] = days_left.days
                actions_done = len(habit_dones)
                self.analysed_data[habit_name]["analysed_data"]["actions_done"] = actions_done
                actions_left = str(target_repeats - actions_done)
                self.analysed_data[habit_name]["analysed_data"]["actions_left"] = actions_left

                counter = 0
                #self.analysed_data[habit_name]["given_attrs"]["dones"][counter] = []
                #self.analysed_data[habit_name]["given_attrs"]["dones"]["dates"] = []
                for done_habit in habit_dones:
                    full_done_duration = timedelta(microseconds=0)
                    done_habit_dict = {}

                    self.analysed_data[habit_name]["given_attrs"]["dones"][counter] = []
                    self.analysed_data[habit_name]["given_attrs"]["dones"][counter] = done_habit

                    #from_time = datetime.strptime(done_habit[2], '%Y-%m-%d %H:%M')
                    from_time = system.string_to_datetime(done_habit[2])

                    done_habit_dict["from_time"] = from_time
                    to_time = system.string_to_datetime(done_habit[3])
                    done_habit_dict["to_time"] = to_time
                    created = to_time
                    done_habit_dict["created"] = created

                    timespan_done_habit = to_time - from_time
                    done_habit_dict["timespan_done_habit"] = timespan_done_habit
                    difference_start = from_time - datetime.combine(from_time.date(), target_time_start)
                    done_habit_dict["difference_start"] = difference_start
                    difference_end = datetime.combine(to_time.date(), target_time_end) - to_time
                    done_habit_dict["difference_end"] = difference_end
                    target_duration_delta = timedelta(hours=target_duration.hour, minutes=target_duration.minute, seconds=target_duration.second, microseconds=target_duration.microsecond)
                    done_habit_dict["target_duration_delta"] = target_duration_delta
                    difference_duration = timespan_done_habit - target_duration_delta
                    done_habit_dict["difference_duration"] = difference_duration

                    self.analysed_data[habit_name]["analysed_data"]["dones"][counter] = done_habit_dict

                    full_done_duration += timespan_done_habit

                    counter = counter + 1

                    # [habit_name].append(done_habit)
                self.analysed_data[habit_name]["analysed_data"]["full_done_duration"] = full_done_duration
                self.analysed_data[habit_name]["analysed_data"]["full_target_duration"] = full_target_duration

                duration = datetime.combine(date.min, target_duration) - datetime.min

                if target_repeats <= actions_done and duration <= full_done_duration:
                    #print("target_rep: "+str(target_repeats)+" <= done: "+str(actions_done))
                    #print("dur: "+str(duration)+" <= full_dur: "+str(full_done_duration))
                    if sqlite.get_from_table_by_id(self.path, "habits", habit_id)[0][11] == 1:
                        print("Habit "+habit_name+" already done")
                    else:    
                        sqlite.edit_row_by_id(self.path, "habits", "completed", "1", habit_id)
                        self.analysed_data[habit_name]["analysed_data"]["completed"] = 1
                        print("Habit "+habit_name+" updated, it's done!")
                    #print("Habit '"+habit_name+"' completed")
                else:
                    self.analysed_data[habit_name]["analysed_data"]["completed"] = 0
            print()

        #if return_json:
        #    return json.dumps(rows)
        #else:
        #    for row in rows:
        #        print(row)

