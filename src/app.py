''' Travel Itinerary system
    This module is entry point
'''
import logging
import os
from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from flask import Flask, jsonify
from flask_smorest import Api
from config.prompt import PrintPrompts, InputPrompts 
from routes.auth_routes.authorization import blp_auth
from routes.admin_routes.package import blp_package
from routes.admin_routes.itinerary import blp_itinerary
from routes.customer_routes.profile import blp_profile
# from view.menus.admin import AdminMenu
# from view.menus.user import UserMenu
# from view.registration import RegistrationViews
# from view.authentication import Authentication
import utils.initialize_app as initialize_app
from blocklist import BLOCKLIST


logging.basicConfig(format = '%(asctime)s - %(message)s', 
                    datefmt = '%d-%m-%Y %H:%M:%S',
                    filename = 'logs.txt',
                    level = logging.DEBUG)

logging.getLogger(__name__)

def main() -> None:
    '''Main function to check if user or admin and show corresponding menu'''
    while True:
        print(PrintPrompts.NAME)
        print(PrintPrompts.ENTRY)
        parameter = input(InputPrompts.ENTER)
        match parameter:
            case '1':
                obj_register = RegistrationViews()
                obj_register.enter_customer_details()
            case '2':
                obj_authenticate = Authentication()
                role = obj_authenticate.user_authentication()
                if role is not None and role[0] == 'user':
                    obj_user = UserMenu(role[1])
                    obj_user.user_menu()
                elif role is not None and role[0] == 'admin':
                    obj_admin = AdminMenu()
                    obj_admin.admin_menu()
            case '3': break
            case _: print(PrintPrompts.INVALID_PROMPT)

if __name__ == "__main__":

    # all the tables will be created
    # initialize_app.create_tables()
    # initialize_app.create_admin()
    # main()
    app = Flask(__name__)
    load_dotenv()
    app.config["API_TITLE"] = "Travel Management system"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    api = Api(app)
    app.config["JWT_SECRET_KEY"] = os.getenv('SECRET_KEY')
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
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
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )

    api.register_blueprint(blp_auth)
    api.register_blueprint(blp_package)
    api.register_blueprint(blp_itinerary)
    api.register_blueprint(blp_profile)
    app.run(debug=True)
