#!/usr/bin/python3
"""
User model for HBnB application
"""
import re
from .basemodel import BaseModel


def validate_email(email):
    """Validate email format"""
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if not isinstance(email, str) or not re.match(pattern, email):
        raise ValueError("Invalid email format")
    return email


def validate_name(name, field_name):
    """Validate that name is a non-empty string and within length"""
    if not isinstance(name, str) or not name.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    stripped = name.strip()
    if len(stripped) > 50:
        raise ValueError(f"{field_name} must be at most 50 characters")
    return stripped

class User(BaseModel):
    """Represents a user in the HBnB application"""

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        # Initialize private attributes
        self.__first_name = None
        self.__last_name = None
        self.__email = None
        self.__is_admin = None

        # Validate and assign via setters
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

        # Relationships as ID lists
        self.places = []   # store place IDs
        self.reviews = []  # store review IDs

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = validate_name(value, 'First name')
        self.save()

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = validate_name(value, 'Last name')
        self.save()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = validate_email(value)
        self.save()

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value):
        if not isinstance(value, bool):
            raise TypeError("is_admin must be a boolean")
        self.__is_admin = value
        self.save()

    def to_dict(self):
        """Serialize User to a dict"""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin,
            'places': self.places,
            'reviews': self.reviews,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
