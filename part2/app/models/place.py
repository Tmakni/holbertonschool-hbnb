#!/usr/bin/python3


from .basemodel import BaseModel


class Place(BaseModel):

    def __init__(self, title, description, price, latitude, longitude, owner, amenities, reviews):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not isinstance(latitude, (int, float)):
            raise TypeError("Latitude must be a number")
        if not isinstance(longitude, (int, float)):
            raise TypeError("Longitude must be a number")
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.amenities = []
        self.reviews = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("The Title must be a string")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if (value < -90.0 or value > 90.0):
            raise ValueError("Latitude not found")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if (value < -90.0 or value > 90.0):
            raise ValueError("Longitude not found")
        self._longitude = value

