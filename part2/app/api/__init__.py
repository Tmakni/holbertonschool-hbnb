from flask_restx import Api

from app.api.v1.users import api as users_ns  # 👈 importe ton namespace

api = Api(
    title='HBNB API',
    version='1.0',
    description='API for the HolbertonBnB project'
)

api.add_namespace(users_ns, path="/api/v1/users")  # 👈 ajoute le namespace à l'API
