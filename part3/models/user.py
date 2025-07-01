#!/usr/bin/python3

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()

class user(db.model):
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Colum(db.String(128), nullable=False)
    email = db.Colum(db.String(128), unique=True, nullable=False)
    password  = db.Colum(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


def hash_password(self, password):
    """Hashes the password before storing it."""
    self.password = bcrypt.generate_password_hash(password).decode('utf-8')

def verify_password(self, password):
    """Verifies if the provided password matches the hashed password."""
    return bcrypt.check_password_hash(self.password, password)
