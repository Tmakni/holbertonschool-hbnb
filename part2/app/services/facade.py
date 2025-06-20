#!/usr/bin/python3
"""
Facade – couche d’agrégation pour le projet HBnB
Regroupe toute la logique haut-niveau (CRUD) en s’appuyant sur un
InMemoryRepository générique.
"""

from app.persistence.repository import InMemoryRepository

from ..models.user import User
from ..models.place import Place
from ..models.review import Review
from ..models.amenity import Amenity


class HBnBFacade:
    """Point d’entrée unique entre les ressources API et la couche data."""

    def __init__(self):
        # On garde un repo indépendant par type pour pouvoir
        # les swapper facilement (DB, Redis, etc.)
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # ---------- USERS ------------------------------------------------------
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

    # ---------- AMENITIES --------------------------------------------------
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        self.amenity_repo.update(amenity_id, amenity_data)
        return self.amenity_repo.get(amenity_id)

    # ---------- PLACES -----------------------------------------------------
    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id, place_data)
        return self.place_repo.get(place_id)

    # ---------- REVIEWS ----------------------------------------------------
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        """
        Renvoie toutes les reviews pour un place donné.
        Nécessite que le repo dispose d’une méthode de filtrage.
        À adapter selon ton implémentation de InMemoryRepository.
        """
        return self.review_repo.filter_by_attribute("place_id", place_id)

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)
        return self.review_repo.get(review_id)

    def delete_review(self, review_id):
        return self.review_repo.delete(review_id)
