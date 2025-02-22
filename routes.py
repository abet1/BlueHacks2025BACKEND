from flask import request, jsonify
from app import app  # Import the app object
from models import db, User, DisasterReport, RescueVehicle


@app.route('/')
def home():
    return "Welcome to the Disaster Response Backend!"


# Register a new user (only role is required)
@app.route('/register', methods=['POST'])
def register():
    data = request.json

    # Create a new user with only the role
    new_user = User(
        role=data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# Report a disaster (Victim)
@app.route('/report', methods=['POST'])
def report_disaster():
    data = request.json
    new_report = DisasterReport(
        disaster_type=data['disaster_type'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        address=data['address']
    )
    db.session.add(new_report)
    db.session.commit()
    return jsonify({"message": "Disaster reported successfully"}), 201

# Get all disasters (Responder)
@app.route('/disasters', methods=['GET'])
def get_disasters():
    disasters = DisasterReport.query.filter_by(status="pending").all()
    disaster_list = []
    for disaster in disasters:
        disaster_list.append({
            "id": disaster.id,
            "disaster_type": disaster.disaster_type,
            "latitude": disaster.latitude,
            "longitude": disaster.longitude,
            "address": disaster.address
        })
    return jsonify(disaster_list), 200

# Accept a disaster (Responder)
@app.route('/accept-disaster/<int:disaster_id>', methods=['PUT'])
def accept_disaster(disaster_id):
    data = request.json
    disaster = DisasterReport.query.get(disaster_id)
    if disaster:
        disaster.status = "accepted"
        disaster.responder_id = data['responder_id']
        db.session.commit()
        return jsonify({"message": "Disaster accepted"}), 200
    return jsonify({"message": "Disaster not found"}), 404

# Mark a disaster as resolved (Responder)
@app.route('/resolve-disaster/<int:disaster_id>', methods=['PUT'])
def resolve_disaster(disaster_id):
    disaster = DisasterReport.query.get(disaster_id)
    if disaster:
        disaster.status = "resolved"
        db.session.commit()
        return jsonify({"message": "Disaster resolved"}), 200
    return jsonify({"message": "Disaster not found"}), 404

# Get available rescue vehicles (Victim)
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = RescueVehicle.query.filter_by(available=True).all()
    vehicle_list = [{"id": v.id, "name": v.name} for v in vehicles]
    return jsonify(vehicle_list), 200