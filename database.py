import sqlite3

DATABASE = "data/flights.db"


# ==========================================
# Create Database and Flights Table
# ==========================================

def create_database():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flights (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            origin TEXT,

            destination TEXT,

            airline TEXT,

            departure_date TEXT,

            price REAL,

            search_date TEXT

        )
    """)
# Bookings table  ← ADD HERE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            email TEXT,

            tickets INTEGER,

            booking_date TEXT

        )
    """)

    conn.commit()
    conn.close()



# ==========================================
# Insert Flight Search Record
# ==========================================

def insert_flight(origin, destination, airline, departure_date, price, search_date):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


    cursor.execute("""
        INSERT INTO flights
        (
            origin,
            destination,
            airline,
            departure_date,
            price,
            search_date
        )

        VALUES (?, ?, ?, ?, ?, ?)

    """,
    (
        origin,
        destination,
        airline,
        departure_date,
        price,
        search_date
    ))


    conn.commit()
    conn.close()



# ==========================================
# Get All Flight History
# ==========================================

def get_all_flights():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


    cursor.execute("""
        SELECT * FROM flights
    """)


    flights = cursor.fetchall()


    conn.close()


    return flights



# ==========================================
# Dashboard Statistics
# ==========================================

def get_statistics():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


    # Total searches
    cursor.execute("""
        SELECT COUNT(*) FROM flights
    """)

    total_searches = cursor.fetchone()[0]



    # Average fare
    cursor.execute("""
        SELECT AVG(price) FROM flights
    """)

    average_fare = cursor.fetchone()[0]



    # Lowest fare
    cursor.execute("""
        SELECT MIN(price) FROM flights
    """)

    lowest_fare = cursor.fetchone()[0]



    # Highest fare
    cursor.execute("""
        SELECT MAX(price) FROM flights
    """)

    highest_fare = cursor.fetchone()[0]
  
    # Total airlines
    cursor.execute("""
    SELECT COUNT(DISTINCT airline)
    FROM flights
     """)

    airlines = cursor.fetchone()[0]


    conn.close()



    # If database is empty
    if average_fare is None:
        average_fare = 0

    if lowest_fare is None:
        lowest_fare = 0

    if highest_fare is None:
        highest_fare = 0



    return {

        "total_searches": total_searches,

        "average_fare": average_fare,

        "lowest_fare": lowest_fare,

        "highest_fare": highest_fare,
         
         "airlines": airlines

    }
# ==========================================
# Export Flights to CSV
# ==========================================

def export_csv():

    import pandas as pd

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql_query(
        "SELECT * FROM flights",
        conn
    )

    df.to_csv(
        "data/fares.csv",
        index=False
    )

    conn.close()

# ==========================================
# Save Confirmed Booking
# ==========================================

def save_booking(name, email, tickets, booking_date):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


    cursor.execute("""
        INSERT INTO bookings
        (
            name,
            email,
            tickets,
            booking_date
        )

        VALUES (?, ?, ?, ?)

    """,
    (
        name,
        email,
        tickets,
        booking_date
    ))


    conn.commit()

    conn.close()



# ==========================================
# Get Confirmed Bookings
# ==========================================

def get_bookings():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


    cursor.execute("""
        SELECT * FROM bookings
    """)


    bookings = cursor.fetchall()


    conn.close()


    return bookings