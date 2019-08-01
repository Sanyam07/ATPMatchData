from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restless import APIManager
from flask_cors import CORS
import os

# --- Database Connection Info --- #
class Config (object):
    SQLALCHEMY_DATABASE_URI = "postgresql://dbd:dbpassword@db370.chncgtkyhkgz.us-east-2.rds.amazonaws.com:5432/dbd"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# --- Database Tables --- #

# Temporary table
class Temp (db.Model):
    __tablename__ = "temp"
    id = db.Column(db.Integer, primary_key =True)

# --- Flask Restless API --- #

manager = APIManager(app, flask_sqlalchemy_db=db)

# Home route
@app.route('/')
@app.route('/index')
def index():
    return "<h3>Endpoints:</h3>"
