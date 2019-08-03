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

class Tournament (db.Model):
    __tablename__ = "tournament"
    id = db.Column(db.Integer, unique=True, autoincrement=True, primary_key=True)
    t_name = db.Column(db.String, unique=True)
    location = db.Column(db.String)
    surface = db.Column(db.String)
    series = db.Column(db.String)
    matches = db.relationship('Match', backref='match_id')

class Player (db.Model):
    __tablename__ = "player"
    id = db.Column(db.Integer, unique=True, autoincrement=True, primary_key=True)
    first = db.Column(db.String)
    last = db.Column(db.String)
    atp_url = db.Column(db.String)
    country = db.Column(db.String(3))
    date_of_birth = db.Column(db.Date)
    turned_pro = db.Column(db.String)
    weight_lbs = db.Column(db.Integer)
    weight_kg = db.Column(db.Integer)
    height_inches = db.Column(db.Integer)
    height_cm = db.Column(db.Integer)
    handedness = db.Column(db.String(1))
    backhand = db.Column(db.String(1))
    matches = db.relationship('Match', backref='match_id')

class Round(db.Model):
    __tablename__ = "round"
    id = db.Column(db.Integer, unique=True, autoincrement=True, primary_key=True)
    r_name = db.Column(db.String, unique=True)


class Match (db.Model):
    __tablename__ = "match"
    id = db.Column(db.Integer, unique=True, autoincrement=True, primary_key=True)
    m_date = db.Column(db.Date)
    round = db.Column(db.Integer, db.ForeignKey('round.id'))
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
    winner = db.Column(db.Integer, db.ForeignKey('player.id'))
    loser = db.Column(db.Integer, db.ForeignKey('player.id'))
    tournament = db.Column(db.Integer, db.ForeignKey('tournament.id'))

# --- Flask Restless API --- #

manager = APIManager(app, flask_sqlalchemy_db=db)

# Home route
@app.route('/')
@app.route('/index')
def index():
    return "<h3>Endpoints:</h3>"
