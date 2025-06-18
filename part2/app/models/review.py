from .basemodel import BaseModel
from .place import Place
from .user import User

class Review(BaseModel):
    """Review of a Place by a User"""
    MAX_TEXT_LENGTH = 1000

    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        if not isinstance(value, str):
            raise TypeError("Review text must be a string")
        if not value:
            raise ValueError("Review text cannot be empty")
        if len(value) > self.MAX_TEXT_LENGTH:
            raise ValueError(f"Review text must be at most {self.MAX_TEXT_LENGTH} characters")
        self.__text = value
        self.save()

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise TypeError("Rating must be an integer between 1 and 5")
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5")
        self.__rating = value
        self.save()

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        if not isinstance(value, Place):
            raise TypeError("Place must be a Place instance")
        self.__place = value
        self.save()

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise TypeError("User must be a User instance")
        self.__user = value
        self.save()

    def update(self, data):
        """Update review attributes via dict; uses BaseModel.update"""
        allowed = {'text', 'rating'}
        filtered = {k: v for k, v in data.items() if k in allowed}
        super().update(filtered)

    def __repr__(self):
