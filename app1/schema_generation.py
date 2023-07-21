import sqlite3

# Connect to the database file
conn = sqlite3.connect('db/ticket.db')
cursor = conn.cursor()

# Create the users table
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    );
""")

# Create the venues table
cursor.execute("""
    CREATE TABLE venues (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        place TEXT NOT NULL,
        capacity INTEGER NOT NULL
    );
""")

# Create the shows table
cursor.execute("""
    CREATE TABLE shows (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        rating INTEGER NOT NULL,
        tags TEXT NOT NULL,
        ticket_price REAL NOT NULL,
        venue_id INTEGER NOT NULL,
        FOREIGN KEY (venue_id) REFERENCES venues(id)
    );
""")

# Create the bookings table
cursor.execute("""
    CREATE TABLE bookings (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        show_id INTEGER NOT NULL,
        FOREIGN KEY (show_id) REFERENCES shows(id)
    );
""")

# Commit the changes and close the connection
conn.commit()
conn.close()
