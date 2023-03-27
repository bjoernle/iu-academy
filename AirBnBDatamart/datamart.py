import sqlite3
import datetime

def get_comments_by_username_and_usertype(username, usertype):# Create a connection to the database

    conn = sqlite3.connect('airbnb.db')
    val = 0
    if usertype == "Host": val = 1
    else: val = 2

    # Execute the query
    results = conn.execute("""
    SELECT Comments.comment, RentablePlaces.name, Users.name
    FROM Comments
    JOIN RentablePlaces ON Comments.place_id = RentablePlaces.id
    JOIN Users ON RentablePlaces.user_id = Users.id
    WHERE Users.name = '"""+username+"""' AND Users.usertype_id = 2;
    """).fetchall()

    # Print the results
    print("Comments by username "+username+" and usertype "+usertype)
    for result in results:
        print(result)
    print()

def get_comments_of_places_rented_in_daterange(check_in_date, check_out_date):

    # Create a connection to the database
    conn = sqlite3.connect('airbnb.db')

    # Execute the query
    results = conn.execute("""
    SELECT Comments.comment
    FROM Comments
    JOIN RentablePlaces ON Comments.place_id = RentablePlaces.id
    JOIN Rentals ON RentablePlaces.id = Rentals.place_id
    WHERE Rentals.start_date >= '"""+check_in_date+"""' AND Rentals.end_date <= '"""+check_out_date+"""';
    """).fetchall()

    # Print the results
    print("Places that was commented in range from "+str(check_in_date)+" to "+str(check_out_date))
    for result in results:
        print(result[0])
    print()

def get_places_unoccupied_now():
    # get today's date
    today = datetime.date.today()

    # Create a connection to the database
    conn = sqlite3.connect('airbnb.db')
    c = conn.cursor()

    # execute the query to get all unoccupied places
    c.execute('''SELECT RentablePlaces.name
                FROM RentablePlaces
                WHERE RentablePlaces.id NOT IN 
                    (SELECT Rentals.place_id 
                    FROM Rentals 
                    WHERE Rentals.start_date <= ? AND Rentals.end_date >= ?)''', (today, today))

    # fetch the results
    results = c.fetchall()

    # print the results
    print("Now unoccupied places:")
    for row in results:
        print(row[0])
    print()

    # close the connection
    conn.close()

def get_places_evaluated_by_both_usertypes():
    # Create a connection to the database
    conn = sqlite3.connect('airbnb.db')

    # Execute the query
    results = conn.execute("""
    SELECT DISTINCT RentablePlaces.name
    FROM RentablePlaces
    JOIN GuestEvaluations ON RentablePlaces.id = GuestEvaluations.place_id
    JOIN PlaceEvaluations ON RentablePlaces.id = PlaceEvaluations.place_id
    WHERE GuestEvaluations.user_id <> PlaceEvaluations.user_id;
    """).fetchall()

    # Print the results
    print("Places evaluated by both usertypes")
    for result in results:
        print(result[0])
    print()

def get_places_in_city_and_datespan(city, start_date, end_date):
    # Define the time period we're interested in
    # start_date = '2023-04-01'
    # end_date = '2023-04-30'

    # Connect to the database
    conn = sqlite3.connect('airbnb.db')

    # Execute the query
    results = conn.execute("""
    SELECT RentablePlaces.name
    FROM RentablePlaces
    WHERE RentablePlaces.address LIKE '%"""+city+"""%'
    AND NOT EXISTS (
        SELECT 1
        FROM Rentals
        WHERE Rentals.place_id = RentablePlaces.id
        AND Rentals.start_date <= ?
        AND Rentals.end_date >= ?
    );
    """, (end_date, start_date)).fetchall()

    # Print the results
    if results:
        print("The following rentable places in Berlin are available during the specified time period:")
        for result in results:
            print(result[0])
    else:
        print("There are no rentable places available in Berlin during the specified time period.")
    print()

def get_photos_with_rates_higher_number(number):
    # Create a connection to the database
    conn = sqlite3.connect('airbnb.db')

    # Execute the query
    results = conn.execute("""
    SELECT Photos.path
    FROM Photos
    JOIN RentablePlaces ON Photos.place_id = RentablePlaces.id
    JOIN GuestEvaluations ON RentablePlaces.id = GuestEvaluations.place_id
    WHERE GuestEvaluations.rating >= """+str(number)+""";
    """).fetchall()

    # Print the results
    print("Photos with rates higher than "+str(number))
    for result in results:
        print(result[0])
    print()

def get_photos_by_usertype(usertype):
    # Create a connection to the database
    conn = sqlite3.connect('airbnb.db')
    
    val = 0
    if usertype == "Host": val = 1
    else: val = 2

    # Execute the query
    results = conn.execute("""
    SELECT DISTINCT Photos.path
    FROM Photos
    JOIN RentablePlaces ON Photos.place_id = RentablePlaces.id
    JOIN Comments ON RentablePlaces.id = Comments.place_id
    JOIN Users ON Comments.user_id = Users.id
    WHERE Users.usertype_id = '"""+str(val)+"""';
    """).fetchall()

    # Print the results
    print("Photos by usertype "+usertype)
    for result in results:
        print(result[0])
    print()

def get_places_that_was_rented_by_usertype(usertype):
    # Create a connection to the database
    conn = sqlite3.connect('airbnb.db')

    val = 0
    if usertype == "Host": val = 1
    else: val = 2

    # Execute the query
    results = conn.execute("""
    SELECT DISTINCT RentablePlaces.name
    FROM RentablePlaces
    JOIN Rentals ON RentablePlaces.id = Rentals.place_id
    JOIN Users ON Rentals.user_id = Users.id
    WHERE Users.usertype_id = '"""+str(val)+"""';
    """).fetchall()

    # Print the results
    print("Places that was rented by usertype '"+usertype+"'")
    for result in results:
        print(result[0])
    print()