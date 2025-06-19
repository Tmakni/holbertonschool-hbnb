#!/usr/bin/python3


from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade


api = Namespace('reviews', description='Review operations')
facade = HBnBFacade()

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user writing the review'),
    'place_id': fields.String(required=True, description='ID of the place being reviewed')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        data = api.payload or {}
        missing = [f for f in ('text', 'rating', 'user_id', 'place_id') if f not in data]
        if missing:
            api.abort(400, f"Missing required field(s): {', '.join(missing)}")
        place = facade.get_place(data['place_id'])
        if not place:
            api.abort(400, 'Place not found')
        user = facade.get_user(data['user_id'])
        if not user:
            api.abort(400, 'User not found')
        if hasattr(place, 'owner') and place.owner.id == user.id:
            api.abort(400, 'User cannot review their own place')
        try:
            review = facade.create_review(data)
            return review.to_dict(), 201
        except (TypeError, ValueError) as e:
            api.abort(400, str(e))

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        return [r.to_dict() for r in reviews], 200
