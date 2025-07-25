from flask import Flask
from flask_jwt_extended import JWTManager
from app.api import api

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

api.init_app(app)  # 👈 ici tu relies ton API à l'app Flask

if __name__ == "__main__":
    app.run(debug=True)
