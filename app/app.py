from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_namespace


app = Flask(__name__)

api = Api(app)

api.add_namespace(users_namespace, path="/api/v1/users")

if __name__ == "__main__":
    app.run(debug=True)
