# Show-Booking-App
uses Flask, Jinja2, SQLite, Werkzeug

This is a simple web application for booking tickets to shows. It is built using Flask, Jinja, and SQLite.

Installation:
Navigate to the project directory: cd ticket-show-booking
Install the required packages: pip install -r requirements.txt

Configuration:
By default, the app will use a SQLite database file located at db/ticket.db. 

Usage:
Run python3 schema_generation.py to create the database
Run the app: python3 app.py
Open a web browser and go to http://localhost:5000 to view the home page.
From the home page, you can view the list of shows and venues, and book tickets for shows.
To add a new show or venue, log in as an admin using the credentials admin / admin, and navigate to the appropriate management page (/venue-management or /show-management).
From the management pages, you can add new shows or venues, and delete existing ones.


