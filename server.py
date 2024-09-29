from flask import Flask, request, jsonify
from db.models import db, User, Policy
import json

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create the database and tables
with app.app_context():
    db.create_all()

# Register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    password = data.get('password')
    email = data.get('email')
    phone = data.get('phone')
    details = data.get('details')  # Expecting JSON formatted string

    if not (name and password and email):
        return jsonify({"error": "Name, password, and email are required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    # Create and store user information
    new_user = User(
        name=name,
        password=password,  # In production, hash the password
        email=email,
        phone=phone,
        details=json.dumps(details)  # Store as JSON
    )

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# Login and verify user credentials
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not (email and password):
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or user.password != password:  # Check password (hash in production)
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful", "user_id": user.id}), 200

# Add Policy
@app.route('/policies', methods=['POST'])
def add_policy():
    data = request.json
    policy_name = data.get('policy_name')
    policy_category = data.get('policy_category')
    policy_requirements = data.get('policy_requirements')
    policy_group = data.get('policy_group')
    policy_details = data.get('policy_details')

    if not (policy_name and policy_category and policy_requirements):
        return jsonify({"error": "Policy name, category, and requirements are required"}), 400

    new_policy = Policy(
        policy_name=policy_name,
        policy_category=policy_category,
        policy_requirements=json.dumps(policy_requirements),  # Store as JSON
        policy_group=policy_group,
        policy_details=json.dumps(policy_details)  # Store as JSON
    )

    db.session.add(new_policy)
    db.session.commit()
    return jsonify({"message": "Policy added successfully", "policy_id": new_policy.policy_id}), 201

# Get all policies
@app.route('/policies', methods=['GET'])
def get_policies():
    policies = Policy.query.all()
    result = []
    for policy in policies:
        result.append({
            "policy_id": policy.policy_id,
            "policy_name": policy.policy_name,
            "policy_category": policy.policy_category,
            "policy_requirements": json.loads(policy.policy_requirements),  # Convert back to JSON
            "policy_group": policy.policy_group,
            "policy_details": json.loads(policy.policy_details) if policy.policy_details else None  # Convert back to JSON
        })
    return jsonify(result), 200

# Update a policy
@app.route('/policies/<int:policy_id>', methods=['PUT'])
def update_policy(policy_id):
    data = request.json
    policy = Policy.query.get_or_404(policy_id)

    policy.policy_name = data.get('policy_name', policy.policy_name)
    policy.policy_category = data.get('policy_category', policy.policy_category)
    policy.policy_requirements = json.dumps(data.get('policy_requirements', json.loads(policy.policy_requirements)))  # Update or keep existing
    policy.policy_group = data.get('policy_group', policy.policy_group)
    policy.policy_details = json.dumps(data.get('policy_details', json.loads(policy.policy_details))) if data.get('policy_details') else policy.policy_details  # Update or keep existing

    db.session.commit()
    return jsonify({"message": "Policy updated successfully"}), 200

# Delete a policy
@app.route('/policies/<int:policy_id>', methods=['DELETE'])
def delete_policy(policy_id):
    policy = Policy.query.get_or_404(policy_id)
    db.session.delete(policy)
    db.session.commit()
    return jsonify({"message": "Policy deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
