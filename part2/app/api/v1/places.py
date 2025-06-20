#!/usr/bin/python3


from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        data = api.payload or {}
        required_fields = ['title', 'price', 'latitude', 'longitude', 'owner_id', 'amenities']

        missing = [f for f in required_fields if f not in data]
        if missing:
            api.abort(400, f"Missing required field(s): {', '.join(missing)}")

        owner = facade.get_user(data['owner_id'])
        if not owner:
            api.abort(400, 'Owner not found')

        if data['price'] <= 0:
            api.abort(400, "Price must be positive")
        if not (-90.0 <= data['latitude'] <= 90.0):
            api.abort(400, "Latitude must be between -90 and 90")
        if not (-180.0 <= data['longitude'] <= 180.0):
            api.abort(400, "Longitude must be between -180 and 180")

        for amenity_id in data['amenities']:
            amenity = facade.get_amenity(amenity_id)
            if not amenity:
                api.abort(400, f"Amenity {amenity_id} not found")

        try:
            place = facade.create_place(data)
        except (TypeError, ValueError) as e:
            api.abort(400, str(e))

        return place.to_dict(), 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        result = [p.to_dict() for p in places]
        return result, 200



@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID, including owner and amenities"""
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, 'Place not found')

        place_data = place.to_dict()

        owner = facade.get_user(place_data['owner_id'])
        place_data['owner'] = owner.to_dict() if owner else None

        amenities_list = []
        for amenity_id in place_data.get('amenities', []):
            amenity = facade.get_amenity(amenity_id)
            if amenity:
                amenities_list.append(amenity.to_dict())
        place_data['amenities'] = amenities_list

        return place_data, 200
    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        data = api.payload or {}

        place = facade.get_place(place_id)
        if not place:
            api.abort(404, 'Place not found')

        updates = {}

        if 'title' in data:
            if not isinstance(data['title'], str) or not data['title'].strip():
                api.abort(400, 'Title must be a non-empty string')
            updates['title'] = data['title'].strip()

        if 'description' in data:
            if not isinstance(data['description'], str):
                api.abort(400, 'Description must be a string')
            updates['description'] = data['description']

        if 'price' in data:
            if not isinstance(data['price'], (int, float)) or data['price'] <= 0:
                api.abort(400, 'Price must be a positive number')
            updates['price'] = data['price']

        if 'latitude' in data:
            lat = data['latitude']
            if not isinstance(lat, (int, float)) or not (-90.0 <= lat <= 90.0):
                api.abort(400, 'Latitude must be between -90 and 90')
            updates['latitude'] = lat

        if 'longitude' in data:
            lon = data['longitude']
            if not isinstance(lon, (int, float)) or not (-180.0 <= lon <= 180.0):
                api.abort(400, 'Longitude must be between -180 and 180')
            updates['longitude'] = lon

        if 'amenities' in data:
            if not isinstance(data['amenities'], list):
                api.abort(400, 'Amenities must be a list of IDs')
            valid_amenities = []
            for amenity_id in data['amenities']:
                amenity = facade.get_amenity(amenity_id)
                if not amenity:
                    api.abort(400, f'Amenity {amenity_id} not found')
                valid_amenities.append(amenity_id)
            updates['amenities'] = valid_amenities

        try:
            updated_place = facade.update_place(place_id, updates)
        except (ValueError, TypeError) as e:
            api.abort(400, str(e))
        return updated_place.to_dict(), 200
