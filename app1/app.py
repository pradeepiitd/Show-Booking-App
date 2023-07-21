from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def home():
    conn = sqlite3.connect('db/ticket.db')
    cursor = conn.cursor()
    cursor.execute("SELECT shows.id, shows.name, shows.rating, shows.tags, shows.ticket_price, venues.name FROM shows INNER JOIN venues ON shows.venue_id = venues.id ORDER BY shows.id DESC LIMIT 5")
    shows = cursor.fetchall()
    #print(shows)
    conn.close()
    return render_template('home.html', shows=shows)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        conn = sqlite3.connect('db/ticket.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        conn.close()
        flash('Account created successfully!')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('db/ticket.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user is not None:
            session['user_id'] = user[0]
            flash('Login successful!')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logout successful!')
    return redirect(url_for('home'))

@app.route('/create_venue', methods=['GET', 'POST'])
def create_venue():
    if 'user_id' not in session:
        flash('Please login as an admin to create a venue.')
        return redirect(url_for('login'))
    elif request.method == 'POST':
        name = request.form['name']
        place = request.form['place']
        capacity = request.form['capacity']
        conn = sqlite3.connect('db/ticket.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO venues (name, place, capacity) VALUES (?, ?, ?)", (name, place, capacity))
        conn.commit()
        conn.close()
        flash('Venue created successfully!')
        return redirect(url_for('venue_management'))
    return render_template('create_venue.html')

@app.route('/venue_management')
def venue_management():
    if 'user_id' not in session:
        flash('Please login as an admin to access the Venue Management page.')
        return redirect(url_for('login'))
    conn = sqlite3.connect('db/ticket.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM venues")
    venues = cursor.fetchall()
    conn.close()
    return render_template('venue_management.html', venues=venues)

@app.route('/venue/<int:venue_id>/delete', methods=['POST'])
def delete_venue(venue_id):
    # Connect to the database file
    conn = sqlite3.connect('db/ticket.db')
    cursor = conn.cursor()

    # Delete the venue from the database
    cursor.execute("DELETE FROM venues WHERE id=?", (venue_id,))
    conn.commit()

    # Close the connection and redirect to the venue management page
    conn.close()
    return redirect(url_for('venue_management'))


@app.route('/create_show', methods=['GET', 'POST'])
def create_show():
    if 'user_id' not in session:
        flash('Please login as an admin to create a show.')
        return redirect(url_for('login'))
    elif request.method == 'POST':
        name = request.form['name']
        rating = request.form['rating']
        tags = request.form['tags']
        ticket_price = request.form['ticket_price']
        venue_id = request.form['venue_id']
        conn = sqlite3.connect('db/ticket.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO shows (name, rating, tags, ticket_price, venue_id) VALUES (?, ?, ?, ?, ?)", (name, rating, tags, ticket_price, venue_id))
        conn.commit()
        conn.close()
        flash('Show created successfully!')
        return redirect(url_for('show_management'))
    conn = sqlite3.connect('db/ticket.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM venues")
    venues = cursor.fetchall()
    conn.close()
    return render_template('create_show.html', venues=venues)

@app.route('/show/<int:show_id>/delete', methods=['POST'])
def delete_show(show_id):
    # Connect to the database file
    conn = sqlite3.connect('db/ticket.db')
    cursor = conn.cursor()

    # Delete the show from the database
    cursor.execute("DELETE FROM shows WHERE id=?", (show_id,))
    conn.commit()

    # Close the connection and redirect to the show management page
    conn.close()
    return redirect(url_for('show_management'))


@app.route('/show_management')
def show_management():
    if 'user_id' not in session:
        flash('Please login as an admin to access the Show Management page.')
        return redirect(url_for('login'))
    conn = sqlite3.connect('db/ticket.db')
    cursor = conn.cursor()
    cursor.execute("SELECT shows.id, shows.name, shows.rating, shows.tags, shows.ticket_price, venues.name FROM shows INNER JOIN venues ON shows.venue_id = venues.id")
    shows = cursor.fetchall()
    conn.close()
    return render_template('show_management.html', shows=shows)

@app.route('/show/<int:show_id>')
def show(show_id):
    conn = sqlite3.connect('db/ticket.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shows WHERE id=?", (show_id,))
    show = cursor.fetchone()
    conn.close()
    return render_template('show.html', show=show)

@app.route('/booking/<int:show_id>', methods=['GET', 'POST'])
def booking(show_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        quantity = request.form['quantity']
        conn = sqlite3.connect('db/ticket.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bookings (name, email, quantity, show_id) VALUES (?, ?, ?, ?)", (name, email, quantity, show_id))
        conn.commit()
        conn.close()
        flash('Booking successful! Check your email for confirmation.')
        return redirect(url_for('show', show_id=show_id))
    return render_template('booking.html', show_id=show_id)

if __name__ == '__main__':
    app.run(debug=True)

