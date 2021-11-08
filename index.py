from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/join/")
def join():
    return render_template("signup.html")


@app.route("/good/")
def good():
    return render_template("good.html")

@app.route("/normal/")
def normal():
    return render_template("normal.html")

@app.route("/bad/")
def bad():
    return render_template("bad.html")

@app.route("/sobad/")
def bad():
    return render_template("sobad.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0")
