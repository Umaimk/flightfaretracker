import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


DATABASE = "data/flights.db"


conn = sqlite3.connect(DATABASE)


df = pd.read_sql_query(
    "SELECT search_date, price FROM flights",
    conn
)


conn.close()


print(df)


if df.empty:
    print("No flight data found")
    exit()


plt.figure(figsize=(8,4))


plt.plot(
    df["search_date"],
    df["price"],
    marker="o",
    color="blue"
)


plt.title("Flight Fare Trend")

plt.xlabel("Search Date")

plt.ylabel("Price ($)")


plt.xticks(rotation=45)


plt.grid(True)


plt.tight_layout()


plt.savefig(
    "static/fare_chart.png"
)


plt.close()


print("Chart generated successfully")