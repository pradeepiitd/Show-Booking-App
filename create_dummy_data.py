import sqlite3

# Connect to the database file
conn = sqlite3.connect('db/ticket.db')
cursor = conn.cursor()

# Insert some dummy data into the users table
cursor.execute("""
    INSERT INTO users (username, email, password, role) VALUES
    ('user0', 'admin@gmail.com', 'pass0', 'admin'),
    ('user1', 'user1@gmail.com', 'pass1', 'user'),
    ('user2', 'user2@gmail.com', 'pass2', 'user');
""")

# Insert some dummy data into the venues table
cursor.execute("""
    INSERT INTO venues (name, place, capacity) VALUES
    ('Venue A', 'City A', 1000),
    ('Venue B', 'City B', 2000),
    ('Venue C', 'City C', 500);
""")

# Insert some dummy data into the shows table
cursor.execute("""
    INSERT INTO shows (name, rating, tags, ticket_price, venue_id) VALUES
    ('Show A', 4, 'Comedy', 10.0, 1),
    ('Show B', 3, 'Drama', 15.0, 2),
    ('Show C', 5, 'Musical', 20.0, 3);
""")

# Commit the changes and close the connection
conn.commit()
conn.close()
