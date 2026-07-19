from flask import Flask, render_template, request
from flask import send_file
import pandas as pd
from datetime import datetime
import database
import predictor
import charts
import random

app = Flask(__name__)

# Create the database when the application starts
database.create_database()


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():

    origin = request.form.get("origin")
    destination = request.form.get("destination")
    departure_date = request.form.get("date")
    airline = request.form.get("airline")


    if not origin or not destination or not departure_date or not airline:

        return """
        <h3>Please fill all flight details.</h3>
        <a href="/">Go Back</a>
        """


    price = random.randint(150, 500)

    search_date = datetime.now().strftime("%Y-%m-%d")


    database.insert_flight(
        origin,
        destination,
        airline,
        departure_date,
        price,
        search_date
    )


    results = [
    {
        "airline": airline,
        "origin": origin,
        "destination": destination,
        "departure": departure_date,
        "price": price
    }
]
    


    # AI Prediction
    predicted_price = predictor.predict_price(10)


    if predicted_price < price:

        decision = "WAIT"

    else:

        decision = "BUY NOW"



    return render_template(
    "results.html",
    flights=results,
    predicted_price=predicted_price,
    decision=decision
)

@app.route("/history")
def history():

    flights = database.get_all_flights()

    return render_template(
        "history.html",
        flights=flights
    )


@app.route("/dashboard")
def dashboard():

    stats = database.get_statistics()

    predicted_price = predictor.predict_price(10)

    if predicted_price < stats["average_fare"]:
        decision = "WAIT"
    else:
        decision = "BUY NOW"


    return render_template(
        "dashboard.html",
        stats=stats,
        predicted_price=predicted_price,
        decision=decision
    )

@app.route("/export")
def export():

    database.export_csv()

    return send_file(
        "data/fares.csv",
        as_attachment=True
    )

# ==============================
# Booking Feature
# ==============================

@app.route("/book")
def book():

    airline = request.args.get("airline")

    price = request.args.get("price")

    return render_template(
        "booking.html",
        airline=airline,
        price=price
    )



@app.route("/confirm_booking", methods=["POST"])
def confirm_booking():

    name = request.form["name"]

    email = request.form["email"]

    tickets = request.form["tickets"]
    airline = request.form["airline"]
    price = request.form["price"]


    booking_date = datetime.now().strftime("%Y-%m-%d")


    database.save_booking(
        name,
        email,
        tickets,
        booking_date
    )


    return render_template(
        "confirmation.html",
        name=name,
        email=email,
        tickets=tickets
    )


@app.route("/bookings")
def bookings():

    confirmed = database.get_bookings()

    return render_template(
        "bookings.html",
        bookings=confirmed
    )

@app.route("/select/<airline>/<price>")
def select_flight(airline, price):

    price = float(price)


    # AI prediction
    predicted_price = predictor.predict_price(10)


    # Recommendation
    difference = price - predicted_price


    if difference > 20:

        decision = "WAIT - Price may decrease"

    else:

        decision = "BUY NOW - Good price"



    return render_template(
        "result.html",
        airline=airline,
        price=price,
        predicted_price=predicted_price,
        decision=decision
    )

if __name__ == "__main__":

    app.run(debug=True)