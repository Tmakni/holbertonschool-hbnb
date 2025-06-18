#!/usr/bin/python3


from .basemodel import BaseModel


class Place(BaseModel):

    def __init__(self, title, description, price, latitude, longitude, owner, amenities):
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
        self.reviews = []
        self.amenities = amenities

    @property
    def title(self):
        return self._title
