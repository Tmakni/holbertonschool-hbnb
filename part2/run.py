from flask import Flask
from flask_restx import Api
from app.place import api as place_ns

app = Flask(__name__)
api = Api(app)

api.add_namespace(place_ns, path="/api/v1/places")

if __name__ == "__main__":
    app.run(debug=True)
