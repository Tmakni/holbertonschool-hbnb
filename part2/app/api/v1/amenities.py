#!/usr/bin/python3


"""
Amenities endpoints for HBnB application (API v1)
"""


from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Input model for Amenity
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        data = api.payload or {}
        # Ensure name is provided
        if 'name' not in data or not isinstance(data['name'], str) or not data['name'].strip():
            api.abort(400, 'Missing or invalid field: name')
        try:
            amenity = facade.create_amenity(data)
            return amenity.to_dict(), 201
        except (TypeError, ValueError) as e:
            api.abort(400, str(e))

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()
        return [a.to_dict() for a in amenities], 200

@api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, 'Amenity not found')
        return amenity.to_dict(), 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        data = api.payload or {}
        # Ensure name is provided and valid
        if 'name' not in data or not isinstance(data['name'], str) or not data['name'].strip():
            api.abort(400, 'Missing or invalid field: name')
        try:
            updated = facade.update_amenity(amenity_id, data)
            if not updated:
                api.abort(404, 'Amenity not found')
            return updated.to_dict(), 200
        except (TypeError, ValueError) as e:
            api.abort(400, str(e))
