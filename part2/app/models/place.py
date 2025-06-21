#!/usr/bin/python3
"""Place model – compatible avec l’API (owner_id, amenities, reviews).
Chaque instance représente une annonce HBnB.
"""
from datetime import datetime
from .basemodel import BaseModel


class Place(BaseModel):
    """Représente un hébergement proposé à la location."""

    def __init__(
        self,
        title: str,
        price: float,
        latitude: float,
        longitude: float,
        owner_id: str,
        description: str | None = None,
        amenities: list[str] | None = None,
        reviews: list[str] | None = None,
        **kwargs,
    ) -> None:
        super().__init__()  # gère id, created_at, updated_at

        # ---------------- Validations de base -----------------
        if not isinstance(title, str) or not title.strip():
            raise TypeError("title must be a non‑empty string")

        if not isinstance(price, (int, float)) or price <= 0:
            raise TypeError("price must be a positive number")

        if not isinstance(latitude, (int, float)) or not -90.0 <= latitude <= 90.0:
            raise ValueError("latitude must be between -90 and 90")

        if not isinstance(longitude, (int, float)) or not -180.0 <= longitude <= 180.0:
            raise ValueError("longitude must be between -180 and 180")

        if not isinstance(owner_id, str) or not owner_id.strip():
            raise TypeError("owner_id must be a non‑empty string (User.id)")

        # ---------------- Affectations ------------------------
        self.title = title.strip()
        self.description = description.strip() if isinstance(description, str) else None
        self.price = float(price)
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id  # UUID ou string du User

        # Toujours des listes (copie défensive)
        self.amenities: list[str] = list(amenities) if amenities else []
        self.reviews: list[str] = list(reviews) if reviews else []

        # Timestamps (si BaseModel ne les gère pas déjà)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    # ---------------- Propriétés réglables -------------------
    @property
    def price(self) -> float:  # type: ignore[override]
        return self._price

    @price.setter
    def price(self, value: float) -> None:  # type: ignore[override]
        if not isinstance(value, (int, float)) or value <= 0:
            raise TypeError("price must be positive")
        self._price = float(value)
        self.updated_at = datetime.utcnow()

    # ---------------- Méthodes utilitaires -------------------
    def add_amenity(self, amenity_id: str) -> None:
        if amenity_id not in self.amenities:
            self.amenities.append(amenity_id)
            self.updated_at = datetime.utcnow()

    def add_review(self, review_id: str) -> None:
        if review_id not in self.reviews:
            self.reviews.append(review_id)
            self.updated_at = datetime.utcnow()

    def to_dict(self) -> dict:
        """Retourne un dictionnaire prêt à être sérialisé en JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "amenities": self.amenities,
            "reviews": self.reviews,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
