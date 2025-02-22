from flask import Flask
from flask_cors import CORS  # Import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db

# Create the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# Import routes
from routes import *

if __name__ == '__main__':
    app.run(debug=True)