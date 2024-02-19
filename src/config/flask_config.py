import os
from flask import jsonify
from flask_jwt_extended import JWTManager
from utils.token import Token

def app_config(app):
    app.config["API_TITLE"] = "Travel Management system"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["JWT_SECRET_KEY"] = os.getenv('SECRET_KEY')


def initialise_jwt(app):
    jwt = JWTManager(app)
    token_obj = Token()

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        status = token_obj.revoke_token(jwt_payload)
        if status == True:
            return (
                jsonify({"message": "The token has expired.", "error": "token_expired"}),
                401,
            )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        check_access_revoked = token_obj.check_token_revoked(jwt_payload,'access_token')
        # check_refresh_revoked = token_obj.check_token_revoked(jwt_payload,'refresh_token')
        return check_access_revoked 

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )
