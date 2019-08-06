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
    t_name = db.Column(db.String, unique=True, nullable=False)
    location = db.Column(db.String)
    surface = db.Column(db.String)
    series = db.Column(db.String)
    matches = db.relationship('Match', backref='tournament_id', lazy=True)

class Player (db.Model):
    __tablename__ = "player"
    id = db.Column(db.Integer, unique=True, autoincrement=True, primary_key=True)
    first = db.Column(db.String, nullable=False)
    last = db.Column(db.String, nullable=False)
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
    wins = db.relationship('Match', backref='winners_id', foreign_keys='Match.winner', lazy=True)
    losses = db.relationship('Match', backref='losers_id', foreign_keys='Match.loser', lazy=True)

class Round (db.Model):
    __tablename__ = "round"
    id = db.Column(db.Integer, unique=True, autoincrement=True, primary_key=True)
    r_name = db.Column(db.String, unique=True, nullable=False)
    matches = db.relationship('Match', backref='round_id', lazy=True)


class Match (db.Model):
    __tablename__ = "match"
    id = db.Column(db.Integer, unique=True, autoincrement=True, primary_key=True)
    best_of = db.Column(db.Integer)
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
    winner_rank = db.Column(db.Integer)
    loser_rank = db.Column(db.Integer)
    winner = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    loser = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    t_round = db.Column(db.Integer, db.ForeignKey('round.id'))
    tournament = db.Column(db.Integer, db.ForeignKey('tournament.id'))

# --- Flask Restless API --- #

manager = APIManager(app, flask_sqlalchemy_db=db)

### --- Home --- ###
@app.route('/')
@app.route('/index')
def index():
    return "<h3>Endpoints:</h3><p>/players</p"

### --- Players --- ###
manager.create_api(Player, url_prefix='', methods=['GET'], collection_name='players', results_per_page=10, max_results_per_page=100)

### --- Matches --- ###
manager.create_api(Match, url_prefix='', methods=['GET'], collection_name='matches', results_per_page=10, max_results_per_page=100)

### --- Tournaments --- ###
manager.create_api(Tournament, url_prefix='', methods=['GET'], collection_name='tournaments', results_per_page=10, max_results_per_page=100)