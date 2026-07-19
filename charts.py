import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


DATABASE = "data/flights.db"


def create_chart():

    conn = sqlite3.connect(DATABASE)


    df = pd.read_sql(
        "SELECT * FROM flights",
        conn
    )


    if len(df) > 0:


        plt.figure(figsize=(8,4))


        plt.plot(
            df["id"],
            df["price"],
            marker="o"
        )


        plt.title(
            "Flight Fare Trend"
        )


        plt.xlabel(
            "Search Number"
        )


        plt.ylabel(
            "Fare Price"
        )


        plt.grid()


        plt.savefig(
            "static/fare_chart.png"
        )


        plt.close()


    conn.close()