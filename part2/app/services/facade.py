#!/usr/bin/python3
from app.persistence.repository import InMemoryRepository
from ..models.user import User
from ..models.place import Place
from ..models.review import Review
from ..models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        #To create a user
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        #To retrive a user
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        #To retrive a user's email
        return self.user_repo.get_by_attribute('email', email)

    def create_amenity(self, amenity_data):
        #To create an amenity
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        #To retrieve an amenity
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        #To retrieve all amenities
        return self.amenity_repo.get_all(amenity)

    def update_amenity(self, amenity_id, amenity_data):
        #To update an amenity
        self.amenity_repo.update(amynity_id, amenity_data)
        return self.amenity_repo.get(amenity_id)

    def create_place(self, place_data):
        #To create a place
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        #To retrieve a place by ID, including associated owner and amenities
        return self.place_repo.get(place_id)

    def get_all_places(self):
        #To retrieve all places
        return self.place_repo.get_all(place)

    def update_place(self, place_id, place_data):
        #To update a place
        self.place_repo.update(place_id, place_data)
        return self.place_repo.get(place_id)

    def create_review(self, review_data):
        #To create a review, including validation for user_id, place_id, and rating
        review = Review(**review_data)
        self.review_repo.add(review)
        return(review)

    def get_review(self, review_id):
        #To retrieve a review
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        #To retrieve all reviews
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        #To retrieve all reviews for a specific place
        return self.review_repo.get_all(place_id)

    def update_review(self, review_id, review_data):
        #To update a review
        self.review_repo.update(review_id, review_data)
        return self.review_repo.get(review_id)

    def delete_review(self, review_id):
        #To delete a review
        return self.review_repo.delete(review_id)
