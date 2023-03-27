import sqlite3
import pandas as pd

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
        return sqlite.get_sqlite_vals_by_columns_and_values(path, "Users", "name, password", name + ", " + pwd)


def to_csv(db_path):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table_name in tables:
        table_name = table_name[0]
        table = pd.read_sql_query("SELECT * from %s" % table_name, db)
        table.to_csv(table_name + '.csv', index_label='index')
    cursor.close()
    db.close()

import numpy
def create_tables(path):
    # Create a connection to the database
    conn = sqlite3.connect(path)

    # Create the Users table
    conn.execute('''
    CREATE TABLE Users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        usertype_id INTEGER NOT NULL,
        password TEXT NOT NULL,
        FOREIGN KEY (usertype_id) REFERENCES UserType(id)
    )
    ''')

    # Create the UserType table
    conn.execute('''
    CREATE TABLE UserType (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    ''')

    # Create the Comments table
    conn.execute('''
    CREATE TABLE Comments (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        place_id INTEGER NOT NULL,
        comment TEXT NOT NULL,
        created DATETIME NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(id),
        FOREIGN KEY (place_id) REFERENCES RentablePlaces(id)
    )
    ''')

    # Create the RentablePlaces table
    conn.execute('''
    CREATE TABLE RentablePlaces (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        zip_code TEXT NOT NULL,
        price REAL NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(id)
    )
    ''')

    # Create the GuestEvaluations table
    conn.execute('''
    CREATE TABLE GuestEvaluations (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        place_id INTEGER NOT NULL,
        rating INTEGER NOT NULL,
        comment TEXT NOT NULL,
        created DATETIME NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(id),
        FOREIGN KEY (place_id) REFERENCES RentablePlaces(id)
    )
    ''')

    # Create the PlaceEvaluations table
    conn.execute('''
    CREATE TABLE PlaceEvaluations (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        place_id INTEGER NOT NULL,
        rating INTEGER NOT NULL,
        comment TEXT NOT NULL,
        created DATETIME NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(id),
        FOREIGN KEY (place_id) REFERENCES RentablePlaces(id)
    )
    ''')

    # Create the Rentals table
    conn.execute('''
    CREATE TABLE Rentals (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        place_id INTEGER NOT NULL,
        start_date DATETIME NOT NULL,
        end_date DATETIME NOT NULL,
        FOREIGN KEY (place_id) REFERENCES RentablePlaces(id)
    )
    ''')

    # Create the Photos table
    conn.execute('''
    CREATE TABLE Photos (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        place_id INTEGER NULL,
        path DATETIME NOT NULL,
        created DATETIME NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(id)
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def insert_data():
    import random
    import datetime

    # create a list of user and place ids
    user_ids = place_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    base = datetime.datetime(2023, 3, 1)
    created = numpy.array([base + datetime.timedelta(hours=i) for i in range(24)])


    # Create a connection to the database
    conn = sqlite3.connect('airbnb.db')


    # Insert data into the Users table
    # Define the list of users to insert
    users = [
        ('Alexander', 'alexander@example.com', '555-1234', 1, 'password1'),
        ('Bob', 'bob@example.com', '555-5678', 2, 'password2'),
        ('Irgendwer', 'irgendwer@example.com', '555-9012', 2, 'password3'),
        ('David', 'david@example.com', '555-3456', 1, 'password4'),
        ('Paul', 'paul@example.com', '555-7890', 1, 'password5'),
        ('Frank', 'frank@example.com', '555-2345', 2, 'password6'),
        ('Bastian', 'bastian@example.com', '555-6789', 1, 'password7'),
        ('Batman', 'batman@example.com', '555-0123', 2, 'password8'),
        ('Goodman', 'goodman@example.com', '555-4567', 1, 'password9'),
        ('Blubb', 'blubb@example.com', '555-8901', 1, 'password10'),
        ('Karsten', 'karsten@example.com', '555-2345', 2, 'password11'),
        ('Larry', 'larry@example.com', '555-6789', 1, 'password12'),
        ('Mandy', 'mandy@example.com', '555-0123', 2, 'password13'),
        ('Joa', 'joa@example.com', '555-4567', 1, 'password14'),
        ('Dörte', 'doerte@example.com', '555-8901', 1, 'password15'),
        ('Peter', 'peter@example.com', '555-2345', 2, 'password16'),
        ('Alex', 'alex@example.com', '555-6789', 1, 'password17'),
        ('Robert', 'robert@example.com', '555-0123', 2, 'password18'),
        ('Sarah', 'sarah@example.com', '555-4567', 1, 'password19'),
        ('Tom', 'tom@example.com', '555-8901', 1, 'password20')
    ]

    # Insert the users into the database
    for user in users:
        conn.execute("""
            INSERT INTO Users (name, email, phone, usertype_id, password)
            VALUES (?, ?, ?, ?, ?)
        """, user)

        
    # Insert data into the UserType table
    conn.execute("INSERT INTO UserType (name) VALUES ('Guest')")
    conn.execute("INSERT INTO UserType (name) VALUES ('Host')")


    # create a list of possible comment texts
    comments = [
        "Great place to stay!",
        "The location was perfect.",
        "I loved the decor in this apartment.",
        "The host was very friendly and helpful.",
        "I would definitely stay here again.",
        "Clean and comfortable accommodations.",
        "The check-in process was very smooth.",
        "The view from the balcony was amazing.",
        "I appreciated the extra amenities provided.",
        "This place exceeded my expectations.",
        "The neighborhood was very lively and fun.",
        "I had a wonderful time staying here.",
        "The price was very reasonable for the quality.",
        "I highly recommend this rental.",
        "The pictures don't do it justice - it's even better in person!"
    ]

    # create a list of possible created dates


    # insert 15 entities into the Comments table
    for i in range(15):
        user_id = user_ids[i % len(user_ids)]  # use modulus to cycle through user ids
        place_id = place_ids[i % len(place_ids)]  # use modulus to cycle through place ids
        comment = comments[i % len(comments)]  # use modulus to cycle through comment texts
        created_date = created[i % len(created)]  # use modulus to cycle through created dates

        # insert the values into the Comments table
        conn.execute("INSERT INTO Comments (user_id, place_id, comment, created) VALUES (?, ?, ?, ?)", (user_id, place_id, comment, created_date))


    user_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    place_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # create a list of possible ratings and comments
    ratings = [1, 2, 3, 4, 5]
    guest_comments = ['Great host!', 'Terrible experience', 'I loved my stay here', 'Average host', 'Highly recommended host', 'Disappointing stay', 'Fantastic host', 'Not worth the price', 'Pleasant stay', 'Would book it again']
    host_comments = ['Great guest!', 'Terrible experience', 'Good guest', 'Average guest', 'Highly recommended guest', 'Never ever', 'Fantastic guest', 'Not worth the money', 'Use no toilet paper', 'this person have fleas']

    # insert 15 entities into the GuestEvaluations table
    for i in range(15):
        user_id = random.choice(user_ids)
        place_id = random.choice(place_ids)
        rating = random.choice(ratings)
        comment = random.choice(host_comments)
        created = datetime.datetime.now()

        # insert the values into the GuestEvaluations table
        conn.execute("INSERT INTO GuestEvaluations (user_id, place_id, rating, comment, created) VALUES (?, ?, ?, ?, ?)", (user_id, place_id, rating, comment, created))

        # insert 15 entities into the GuestEvaluations table
    for i in range(15):
        user_id = random.choice(user_ids)
        place_id = random.choice(place_ids)
        rating = random.choice(ratings)
        comment = random.choice(guest_comments)
        created = datetime.datetime.now()

        # insert the values into the GuestEvaluations table
        conn.execute("INSERT INTO PlaceEvaluations (user_id, place_id, rating, comment, created) VALUES (?, ?, ?, ?, ?)", (user_id, place_id, rating, comment, created))
    
        start_date = datetime.date(2023, 4, 1)  # April 1, 2023
        end_date = datetime.date(2023, 4, 30)  # April 30, 2023
        delta = datetime.timedelta(days=1)  # one day time delta
        # insert 15 entities into the Rentals table
        for i in range(15):
            place_id  = user_id = place_ids[i % len(place_ids)]  # use modulus to cycle through place ids
            rental_start_date = start_date + i * delta  # increment start date for each rental
            rental_end_date = rental_start_date + 6 * delta  # assume 7-day rentals

            # insert the values into the Rentals table
            conn.execute("INSERT INTO Rentals (user_id, place_id, start_date, end_date) VALUES (?, ?, ?, ?)", (user_id, place_id, rental_start_date, rental_end_date))


    # Define the list of rentable places to insert
    rentable_places = [
    ('Berlin Apartment', 'A cozy apartment in central Berlin', '123 Main St', 'Berlin', 'Berlin', '12345', 100, 1),
    ('Munich Loft', 'A spacious loft in downtown Munich', '456 First Ave', 'Munich', 'Bavaria', '67890', 150, 2),
    ('Hamburg House', 'A charming house in a quiet Hamburg neighborhood', '789 Second St', 'Hamburg', 'Hamburg', '23456', 200, 3),
    ('Frankfurt Studio', 'A modern studio in the heart of Frankfurt', '321 Third St', 'Frankfurt', 'Hesse', '34567', 75, 4),
    ('Cologne Condo', 'A stylish condo in Cologne', '654 Fourth St', 'Cologne', 'North Rhine-Westphalia', '45678', 125, 5),
    ('Dresden Duplex', 'A beautiful duplex in historic Dresden', '987 Fifth Ave', 'Dresden', 'Saxony', '56789', 175, 6),
    ('Stuttgart Suite', 'A luxurious suite in the heart of Stuttgart', '246 Eighth St', 'Stuttgart', 'Baden-Württemberg', '67890', 225, 7),
    ('Leipzig Loft', 'A stunning loft in trendy Leipzig', '135 Seventh Ave', 'Leipzig', 'Saxony', '78901', 200, 8),
    ('Düsseldorf Duplex', 'A spacious duplex in Düsseldorf', '864 Ninth St', 'Düsseldorf', 'North Rhine-Westphalia', '89012', 175, 9),
    ('Nuremberg Apartment', 'A cozy apartment in historic Nuremberg', '975 Tenth Ave', 'Nuremberg', 'Bavaria', '90123', 100, 10),
    ('Bremen Bungalow', 'A charming bungalow in a leafy Bremen suburb', '642 Eleventh St', 'Bremen', 'Bremen', '23456', 150, 11),
    ('Hannover House', 'A comfortable house in a quiet Hannover neighborhood', '753 Twelfth Ave', 'Hannover', 'Lower Saxony', '34567', 200, 12),
    ('Essen Estate', 'A grand estate in Essen', '246 Thirteenth St', 'Essen', 'North Rhine-Westphalia', '45678', 500, 13),
    ('Dortmund Duplex', 'A stylish duplex in Dortmund', '753 Fourteenth St', 'Dortmund', 'North Rhine-Westphalia', '56789', 175, 14),
    ('Bonn Bungalow', 'A cozy bungalow in Bonn', '642 Fifteenth Ave', 'Bonn', 'North Rhine-Westphalia', '67890', 150, 15),
    ('Augsburg Apartment', 'A spacious apartment in Augsburg', '975 Sixteenth St', 'Augsburg', 'Bavaria', '78901', 100, 16)
    ]

    # Insert the rentable places into the database
    for place in rentable_places:
        conn.execute("""
            INSERT INTO RentablePlaces (name, description, address, city, state, zip_code, price, user_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, place)

    for i in range(15):
        user_id = place_id = i
        path = str(i)+".jpg"
        created = datetime.datetime.now()
        conn.execute("""
            INSERT INTO Photos (user_id, place_id, path, created)
            VALUES (?, ?, ?, ?)
        """, (user_id, place_id, path, created))
    

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()


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

