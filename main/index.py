from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://ubuntu:dlatldhs@localhost:3306/test?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/join/")
def join():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
