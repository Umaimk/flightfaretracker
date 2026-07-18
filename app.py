from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():

    return render_template("result.html")


@app.route("/history")
def history():

    return render_template("history.html")


@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")



if __name__ == "__main__":

    app.run(debug=True)