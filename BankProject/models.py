from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app import app
import os
import csv
import sys

db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = 'sqlite:///' + os.path.join(basedir,'app.db')


class User(db.Model):
    user_ID = db.Column(db.Integer, primary_key = True, unique = True)
    last_name = db.Column(db.String(30), index = True, unique = True)
    first_name = db.Column(db.String(30), index = True, unique = True)
    age = db.Column(db.String(30), index = True, unique = True)
    gender = db.Column(db.String(30), index = True, unique = True)
    DOB = db.Column(db.String(30), index = True, unique = True)
    SSN = db.Column(db.String(30), index = True, unique = True)
    address = db.Column(db.String(30), index = True, unique = True)
    phone_number = db.Column(db.String(30), index = True, unique = True)
    email_address = db.Column(db.String(30), index = True, unique = True)

class Card(db.Model):
    user_ID = db.Column(db.Integer, foreign_key = True, unique = True, on_delete = models.CASCADE)
    type = db.Column(db.String(30), index = True, unique = True, on_delete = models.CASCADE)
    card_number = db.Column(db.String(30), index = True, unique = True, on_delete = models.CASCADE)
    CVV = db.Column(db.String(30), index = True, unique = True, on_delete = models.CASCADE)
    expiration_date = db.Column(db.String(30), index = True, unique = True, on_delete = models.CASCADE)
    name_on_card = db.Column(db.String(30), index = True, unique = True, on_delete = models.CASCADE)

class Credentials(db.Model):
    user_ID = db.Column(db.Integer, foreign_key = True, unique = True, on_delete = models.CASCADE)
    password = db.Column(db.String(3), index = True, unique = True, on_delete = models.CASCADE)
    security_question_answer = db.Column(db.String(30), index = True, unique = True, on_delete = models.CASCADE)
