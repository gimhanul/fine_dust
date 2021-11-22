from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user_table'
   
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    email = db.Column(db.String(20), unique = True, nullable = False)
    password = db.Column(db.String(20))
    name = db.Column(db.String(10))

    def __init__(self, email, password, name):
        self.email = email
        self.name = name
        self.password = password


