import uuid
from datetime import datetime
import re

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

class User(BaseModel):
    EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
    MAX_NAME_LENGTH = 50

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = None
        self.last_name = None
        self.email = None
        self.is_admin = is_admin
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)

    def set_first_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("First name must be a non-empty string")
        if len(name) > self.MAX_NAME_LENGTH:
            raise ValueError(f"First name must be at most {self.MAX_NAME_LENGTH} characters")
        self.first_name = name.strip()
        self.save()

    def set_last_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Last name must be a non-empty string")
        if len(name) > self.MAX_NAME_LENGTH:
            raise ValueError(f"Last name must be at most {self.MAX_NAME_LENGTH} characters")
        self.last_name = name.strip()
        self.save()

    def set_email(self, email):
        if not email or not self.EMAIL_REGEX.match(email):
            raise ValueError("Invalid email format")
        self.email = email
        self.save()

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

class Review(BaseModel):
    """Review of a Place by a User"""
    MAX_TEXT_LENGTH = 1000

    def __init__(self, text, rating, place, user):
        super().__init__()
        # Validate and assign using setters
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
        # Store foreign keys
        self.place_id = self.__place.id
        self.user_id = self.__user.id

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Review text must be a non-empty string")
        if len(value) > self.MAX_TEXT_LENGTH:
            raise ValueError(f"Review text must be at most {self.MAX_TEXT_LENGTH} characters")
        self.__text = value.strip()
        self.save()

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        self.__rating = value
        self.save()

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        # Avoid circular import at module level
        from .place import Place
        if not isinstance(value, Place):
            raise TypeError("Place must be a Place instance")
        self.__place = value
        self.save()

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        from .user import User
        if not isinstance(value, User):
            raise TypeError("User must be a User instance")
        self.__user = value
        self.save()

    def update(self, data):
        """Update only text and rating via provided dict"""
        for field in ('text', 'rating'):
            if field in data:
                setattr(self, field, data[field])
        self.save()

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'place_id': self.place_id,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Amenity(BaseModel):
    """Amenity that can be associated with Places"""
    MAX_NAME_LENGTH = 50

    def __init__(self, name):
        super().__init__()
        self.__name = None
        self.name = name  # triggers setter validation

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Amenity name must be a string")
        if not value:
            raise ValueError("Amenity name cannot be empty")
        if len(value) > self.MAX_NAME_LENGTH:
            raise ValueError(f"Amenity name must be at most {self.MAX_NAME_LENGTH} characters")
        self.__name = value
        self.save()

    def update(self, data):
        return super().update(data)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
