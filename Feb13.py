import os
import sys
import cvs

from sqlalchemy import create-engine
from sqlalchemy.orm import scoped_session, sessionmaker
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'app.db')

engine = create_engine(DATABASE_URL)

db = scoped_session(sessionmaker(bind=engine))

def create_database():
    db.execute("CREATE TABLE flights (origin VARCHAR(30), destination VARCHAR(30), duration VARCHAR(30), duration INT(6))")

def populate():
    f = open("flights.csv")
    reader = csv.reader():
    for origin, destination, duration in reader:
        db.execute("Insert into flights (origin, destination, duration) VALUES"
