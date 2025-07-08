from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)

from app.models.user import User
from app import db

api = Namespace("auth", description="Operations d'authentification")

"""
Modèle utilisé par Swagger pour valider le JSON dentrée.
"""
login_model = api.model("Login", {
    "email": fields.String(required=True, description="Email de l'utilisateur"),
    "password": fields.String(required=True, description="Mot de passe"),
})

@api.route("/login")
class Login(Resource):
    """
    Reçoit email + mot de passe, renvoie un access_token et un refresh_token.
    """
    @api.expect(login_model)
    def post(self):
        """
        Étapes :
        1) Récupérer le JSON.
        2) Charger lutilisateur en base via lemail.
        3) Vérifier le mot de passe.
        4) Générer le JWT avec un claim is_admin.
        5) Renvoyer les deux tokens.
        """
        data = api.payload or {}
        user = User.query.filter_by(email=data.get("email")).first()

        if not user or not user.verify_password(data.get("password", "")):
            return {"error": "Invalid credentials"}, 401

        claims = {"is_admin": user.is_admin}
        access_token  = create_access_token(identity=user.id, additional_claims=claims)
        refresh_token = create_refresh_token(identity=user.id)

        return {
            "access_token":  access_token,
            "refresh_token": refresh_token,
            "token_type":    "Bearer"
        }, 200


@api.route("/refresh")
class Refresh(Resource):
    """
    Renvoie un nouveau access_token lorsque le refresh_token est encore valide.
    """
    @jwt_required(refresh=True)
    def post(self):
        user_id = get_jwt_identity()
        claims  = {"is_admin": get_jwt().get("is_admin", False)}
        new_access = create_access_token(identity=user_id, additional_claims=claims)
        return {"access_token": new_access, "token_type": "Bearer"}, 200
