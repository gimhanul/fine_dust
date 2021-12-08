from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('config.Config')

from app.main.view import main as main

app.register_blueprint(main)