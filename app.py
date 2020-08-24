# import necessary libraries
from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Pet = create_classes(db)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# create route that renders data.html template
@app.route("/data")
def data():
    return render_template("/data.html")

# create route that renders charts.html template
@app.route("/charts")
def charts():
    return render_template("/charts.html")

# create route that renders charts.html template
@app.route("/regressiondisasters")
def regressiondisasters():
    return render_template("/regressiondisasters.html")

# create route that renders charts.html template
@app.route("/regressionstocks")
def regressionstocks():
    return render_template("/regressionstocks.html")

if __name__ == "__main__":
    app.run()
