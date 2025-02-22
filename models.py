from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), nullable=False)  # "victim" or "responder"

class DisasterReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disaster_type = db.Column(db.String(50), nullable=False)  # e.g., flood, fire
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default="pending")  # "pending", "accepted", "resolved"
    responder_id = db.Column(db.Integer, nullable=True, default=2)

class RescueVehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)  # e.g., Ambulance, Fire Truck
    available = db.Column(db.Boolean, default=True)