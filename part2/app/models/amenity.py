#!/usr/bin/python3


from .basemodel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        if not isinstance(name, str):
            raise TypeError("Amenity name must be a string")
        if not name:
            raise ValueError("Amenity name cannot be empty")
        if len(name) > 50:
            raise ValueError("Amenity name must be at most 50 characters")
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
