from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restless import APIManager
from flask_cors import CORS
import os

# --- Database Connection Info --- #
class Config (object):
    SQLALCHEMY_DATABASE_URI = "postgresql://dbd:dbdpassword@dbd.chncgtkyhkgz.us-east-2.rds.amazonaws.com:5432/dbd"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# --- Database Tables --- #

# Tournament table
class Tournament (db.Model):
    __tablename__ = "tournament"
    id = db.Column(db.Integer, unique=True, autoincrement=True, primary_key=True)
    t_name = db.Column(db.String, unique=True)
    location = db.Column(db.String)
    surface = db.Column(db.String)
    series = db.Column(db.String)

# Match table
class Match (db.Model):
    __tablename__ = "match"
    id = db.Column(db.Integer, unique=True, autoincrement=True, primary_key=True)
    m_date = db.Column(db.Date)
    w_set1 = db.Column(db.Integer)
    l_set1 = db.Column(db.Integer)
    w_set2 = db.Column(db.Integer)
    l_set2 = db.Column(db.Integer)
    w_set3 = db.Column(db.Integer)
    l_set3 = db.Column(db.Integer)
    w_set4 = db.Column(db.Integer)
    l_set4 = db.Column(db.Integer)
    w_set5 = db.Column(db.Integer)
    l_set5 = db.Column(db.Integer)

# --- Flask Restless API --- #

manager = APIManager(app, flask_sqlalchemy_db=db)

# Home route
@app.route('/')
@app.route('/index')
def index():
    return "<h3>Endpoints:</h3>"
