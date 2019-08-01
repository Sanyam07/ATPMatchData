from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_cors import CORS
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql://"
    + os.environ["DB_USERNAME"]
    + ":"
    + os.environ["DB_PW"]
    + "db370.chncgtkyhkgz.us-east-2.rds.amazonaws.com:3306/db370"
)
db = SQLAlchemy(app)
CORS(app)

# --- Database Tables --- #


# --- Flask Restless API --- #

manager = APIManager(app, flask_sqlalchemy_db=db)

### --- Home Route --- ###
@app.route('/')
@app.route('/index')
def index():
    return "<h3>Endpoints:</h3>"
