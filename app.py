from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():

    return render_template("result")


@app.route("/history")
def history():

    return "History page coming soon"


@app.route("/dashboard")
def dashboard():

    return "Dashboard coming soon"



if __name__ == "__main__":

    app.run(debug=True)