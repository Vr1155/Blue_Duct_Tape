from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=True)
    details = db.Column(db.Text, nullable=True)  # Store as JSON

class Policy(db.Model):
    policy_id = db.Column(db.Integer, primary_key=True)
    policy_name = db.Column(db.String(100), nullable=False)
    policy_category = db.Column(db.String(100), nullable=False)
    policy_requirements = db.Column(db.Text, nullable=False)  # Store as JSON
    policy_group = db.Column(db.String(100), nullable=True)
    policy_details = db.Column(db.Text, nullable=True)  # Store as JSON
