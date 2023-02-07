import sqlite3


def create_connection(path):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param path: path to database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(path)
    except sqlite3.Error as e:
        print(e)

    return conn


def create_tables_habittracker(path):
    """ create the needed tables
    :param path: path to database file
    :return: None
    """
    sqlite_connection = create_connection(path)
    cursor = sqlite_connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    password TEXT,
    created DATETIME,
    modified CURRENT_TIMESTAMP
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    name TEXT,
    description TEXT,
    timespan TEXT,
    date_start DATE,
    date_end DATE,
    target_time_start TIME,
    target_time_end TIME,
    target_duration TIME,
    target_repeats INTEGER,
    completed INTEGER,
    created DATETIME,
    modified TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS habits_lasttime (
    id INTEGER PRIMARY KEY,
    habit_id INTEGER,
    start_datetime DATETIME,
    end_datetime DATETIME,
    created DATETIME,
    modified CURRENT_TIMESTAMP
    )""")

    sqlite_connection.commit()


def count_rows(path, table):
    """ count rows of table
    :param table: table of database
    :param path: path to database file
    :return: just text
    """
    sqlite_connection = create_connection(path)
    cursor = sqlite_connection.cursor()
    cursor.execute("select * from "+table)
    results = cursor.fetchall()
    print("Count of Rows: "+str(len(results)))


def delete_last_row(path, table, show_action=False):
    """ delete last row of table
    :param show_action: True if you want to see what's quered to database
    :param table: table of database
    :param path: path to database file
    :return: some text
    """
    try:
        sqlite_connection = create_connection(path)
        cursor = sqlite_connection.cursor()
        sql = "DELETE FROM "+table+" WHERE id = (SELECT MAX(id) FROM "+table+");"
        if show_action:
            print(sql)
        cursor.execute(sql)
        sqlite_connection.commit()
        print(cursor.rowcount, " SQLITE record(s) deleted.")
    except sqlite3.Error as error:
        print("Failed to delete from table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            if show_action:
                print("The SQLite connection is closed")


def delete_from_table_by_id(path, table, row_id, show_action=False):
    """ delete rows from table older a week
    :param show_action: True if you want to see the quered actions
    :param row_id: id of row
    :param table: table from database
    :param path: path to database file
    :return: None
    """
    try:
        sqlite_connection = create_connection(path)
        cursor = sqlite_connection.cursor()
        sql = "DELETE FROM "+table+" WHERE id = "+str(row_id)
        if show_action:
            print(sql)
        cursor.execute(sql)
        sqlite_connection.commit()
        if show_action:
            print(cursor.rowcount, " SQLITE record(s) deleted")
    except sqlite3.Error as error:
        print("Failed to delete from table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            if show_action:
                print("The SQLite connection is closed")

def delete_old_rows(path, table, datetime_column, show_action=False):
    """ delete rows from table older a week
    :param show_action: True if you want to see the quered actions
    :param datetime_column: datetime column of table
    :param table: table from database
    :param path: path to database file
    :return: None
    """
    try:
        sqlite_connection = create_connection(path)
        cursor = sqlite_connection.cursor()
        sql = "DELETE FROM "+table+" WHERE "+datetime_column+" <= time('now', '-7 days')"
        if show_action:
            print(sql)
        cursor.execute(sql)
        sqlite_connection.commit()
        if show_action:
            print(cursor.rowcount, " SQLITE record(s) deleted because it's older ")
    except sqlite3.Error as error:
        print("Failed to delete from table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            if show_action:
                print("The SQLite connection is closed")


def get_all_from_table(path, table, show_action=False):
    """ get all from table
    :param show_action: True if you want to see the quered actions
    :param table: table from database
    :param path: path to database file
    :return: Connection object or None
    """
    sqlite_connection = create_connection(path)
    cursor = sqlite_connection.cursor()
    sql = "SELECT * FROM " + table
    if show_action:
        print(sql)
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return rows


def get_from_table_by_id(path, table, id, show_action=False):
    """ get row from table by id
    :param show_action: True if you want to see the quered actions
    :param table: table from database
    :param path: path to database file
    :param id: id of row
    :return: Connection object or None
    """
    sqlite_connection = create_connection(path)
    cursor = sqlite_connection.cursor()
    #print(str(id))
    sql = "SELECT * FROM " + table + " WHERE id = '"+str(id)+"'"
    if show_action:
        print(sql)
    cursor.execute(sql)
    rows = cursor.fetchall()
    #for row in rows:
    #    print(row)
    return rows


def get_sqlite_vals_by_columns_and_values(path, table, column_name_csv, values_csv, show_action=False):
    """ get sqlite vals by column csv and values csv
    :param values_csv: a csv of values
    :param column_name_csv: a csv of column names
    :param show_action: True if you want to see the quered actions
    :param table: table from database
    :param path: path to database file
    :return: One or more rows
    """
    try:
        sqlite_connection = create_connection(path)
        cursor = sqlite_connection.cursor()
        # print("Connected to SQLite")

        cols = column_name_csv.split(", ")
        vals = values_csv.split(", ")
        if str(show_action).lower() == "true":
            print("cols: "+str(len(cols))+", vals: "+str(len(vals)))
        if len(cols) == len(vals):
            sql_adding = ""
            cnt = 0
            for col in cols:
                sql_adding += col+" like '"+vals[cnt]+"' AND "
                cnt = cnt+1
            sql_adding = "".join(sql_adding.rsplit(sql_adding[-5:], 1))
            sql = "SELECT * FROM "+table+" WHERE "+sql_adding
            if str(show_action).lower() == "true":
                print(sql)
            cursor.execute(sql)

            rows = cursor.fetchall()
            if str(show_action).lower() == "true":
                print("Found "+str(len(rows))+" rows (things that was found before).")
            # for row in rows:
                # print(row)
            return rows
        else:
            if str(show_action).lower() == "true":
                print("colsCnt != valsCnt")
        cursor.close()
        return []

    except sqlite3.Error as error:
        print("---")
        print("Failed getting data.", error)
        print("---")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            if str(show_action).lower() == "true":
                print("The SQLite connection is closed")


def insert_to_sqlite_table(path, table, column_name_csv, values_csv, show_action=False):
    """ insert to table by column csv and values csv
    :param values_csv: a csv of values
    :param column_name_csv: a csv of column names
    :param show_action: True if you want to see the quered actions
    :param table: table from database
    :param path: path to database file
    :return: id of inserted row
    """
    sqlite_connection = create_connection(path)
    cursor = sqlite_connection.cursor()

    vals_string = ""
    vals = values_csv.split(", ")
    if len(vals) == 0 or len(vals) == 1:
        vals = values_csv.split(",")
    for val in vals:
        vals_string = vals_string+"'"+val+"',"
    vals_string = "".join(vals_string.rsplit(vals_string[-1:], 1))
    sql = "INSERT INTO "+table+" ("+column_name_csv+") VALUES ("+vals_string+")"
    if show_action:
        print(sql)
    cursor.execute(sql)
    sqlite_connection.commit()
    if show_action:
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    last_row = cursor.lastrowid
    cursor.close()
    return last_row


def edit_row_by_id(path, table, col_name, update_value, id, show_action=False):
    """ edit rows by column csv and values csv
    :param update_values_csv: a csv of values
    :param update_column_name_csv: a csv of column names
    :param values_csv: a csv of values
    :param column_name_csv: a csv of column names
    :param show_action: True if you want to see the quered actions
    :param table: table from database
    :param path: path to database file
    :return: One or more rows
    """
    try:
        sqlite_connection = create_connection(path)
        cursor = sqlite_connection.cursor()
        # print("Connected to SQLite")

        sql_adding_set = ""
        sql_adding_find = ""

        sql = "UPDATE "+table+" SET "+col_name+"="+update_value+" WHERE 'id' = "+str(id)
        if show_action:
            print(sql)
        cursor.execute(sql)
        sqlite_connection.commit()
        print("Table '"+table+"' row "+col_name+" successfully updated")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            if show_action:
                print("The SQLite connection is closed")
def edit_row_by_columns_and_values(path, table, update_column_name_csv, update_values_csv, column_name_csv, values_csv, show_action=False):
    """ edit rows by column csv and values csv
    :param update_values_csv: a csv of values
    :param update_column_name_csv: a csv of column names
    :param values_csv: a csv of values
    :param column_name_csv: a csv of column names
    :param show_action: True if you want to see the quered actions
    :param table: table from database
    :param path: path to database file
    :return: One or more rows
    """
    try:
        sqlite_connection = create_connection(path)
        cursor = sqlite_connection.cursor()
        # print("Connected to SQLite")
        update_cols = update_column_name_csv.split(", ")
        update_vals = update_values_csv.split(", ")
        cols = column_name_csv.split(", ")
        vals = values_csv.split(", ")
        if show_action:
            print("cols: " + str(len(cols)) + ", vals: " + str(len(vals)))
        if len(update_cols) == len(update_vals) and len(cols) == len(vals):

            sql_adding_set = ""
            sql_adding_find = ""
            cnt = 0
            for update_col in update_cols:
                sql_adding_set += update_col+" = '"+update_vals[cnt]+"', "
                cnt = cnt+1
            sql_adding_set = "".join(sql_adding_set.rsplit(sql_adding_set[-2:], 1))
            cnt = 0
            for col in cols:
                sql_adding_find += col+" like '"+vals[cnt]+"' AND "
                cnt = cnt+1
            sql_adding_find = "".join(sql_adding_find.rsplit(sql_adding_find[-5:], 1))
            sql = "UPDATE "+table+" SET "+sql_adding_set+" WHERE "+sql_adding_find
            if show_action:
                print(sql)
            cursor.execute(sql)
            sqlite_connection.commit()
            print("Record Updated successfully ")
            cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            if show_action:
                print("The SQLite connection is closed")
