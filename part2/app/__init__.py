from flask import Flask
from flask_restx import Api

def create_app(test_config=False):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    if test_config:
        app.config['TESTING'] = True

    api = Api(app, version='1.0', title='HBnB API')

    # Import des 4 namespaces **à l’intérieur** de la factory
    from app.api.v1.users      import api as users_ns
    from app.api.v1.places     import api as places_ns
    from app.api.v1.reviews    import api as reviews_ns
    from app.api.v1.amenities import api as amenities_ns

    # Enregistrement sous les bons chemins
    api.add_namespace(users_ns,      path='/api/v1/users')
    api.add_namespace(places_ns,     path='/api/v1/places')
    api.add_namespace(reviews_ns,    path='/api/v1/reviews')
    api.add_namespace(amenities_ns,  path='/api/v1/amenities')

    return app
