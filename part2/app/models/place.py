#!/usr/bin/python3


from uuid import uuid4
from datetime import datetime
from .basemodel import BaseModel


class Place(BaseModel):
    """Modèle Place plus flexible : accepte owner_id OU owner,
    initialise amenities & reviews par défaut."""

    def __init__(self, title, description, price, latitude, longitude,
                 owner_id=None, owner=None, amenities=None, reviews=None, **kwargs):
        super().__init__()
        # --- validations basiques ---
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        if price <= 0:
            raise ValueError("price must be positive")
        if not isinstance(latitude, (int, float)) or not -90.0 <= latitude <= 90.0:
            raise ValueError("latitude out of range")
        if not isinstance(longitude, (int, float)) or not -180.0 <= longitude <= 180.0:
            raise ValueError("longitude out of range")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

        self.owner_id = owner_id or owner

        self.amenities = amenities or []
        self.reviews = reviews or []

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
