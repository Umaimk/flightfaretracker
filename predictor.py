import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression


DATA = "data/training_data.csv"

MODEL = "models/model.pkl"


def train_model():

    df = pd.read_csv(DATA)

    X = df[["days_before_departure"]]

    y = df["price"]


    model = LinearRegression()

    model.fit(X, y)


    joblib.dump(
        model,
        MODEL
    )


    print("Model trained successfully")



def predict_price(days):

    model = joblib.load(MODEL)

    prediction = model.predict(
        [[days]]
    )

    return round(prediction[0], 2)



if __name__ == "__main__":

    train_model()