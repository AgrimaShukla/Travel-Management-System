''' Travel Itinerary system
    This module is entry point
'''
import logging

from dotenv import load_dotenv
from flask import Flask, request
from shortuuid import ShortUUID
from utils.initialize_app import create_tables, create_admin
from flask_smorest import Api
from utils.custom_error_response import CustomError
from routes.auth_route import blp_auth
from config.prompt import PrintPrompts
from routes.package_route import blp_package
from routes.itinerary_route import blp_itinerary
from routes.user_route import blp_profile
from routes.review_route import blp_review
from routes.booking_route import blp_booking
from config.status_code import StatusCodes
from config.flask_config import app_config, initialise_jwt
from blocklist import BLOCKLIST


logging.basicConfig(format = '%(asctime)s - %(message)s', 
                    datefmt = '%d-%m-%Y %H:%M:%S',
                    filename = 'logs.txt',
                    level = logging.DEBUG)

logger = logging.getLogger(__name__)

BASE_URL = '/travelmanagementsystem'

def create_app():
    app = Flask(__name__)
    create_tables()
    create_admin()
    load_dotenv()
    
    app_config(app)
    api = Api(app)
    initialise_jwt(app)

    app.register_error_handler(
        Exception,
        lambda _: CustomError(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR).jsonify_data
    )

   # setting req Id for logging
    @app.before_request
    def set_custom_headers():
        request_id = ShortUUID().random(length=10)
        request.environ["X-Request-Id"] = request_id

    api.register_blueprint(blp_auth, url_prefix = BASE_URL)
    api.register_blueprint(blp_package, url_prefix = BASE_URL)
    api.register_blueprint(blp_itinerary, url_prefix = BASE_URL)
    api.register_blueprint(blp_profile, url_prefix = BASE_URL)
    api.register_blueprint(blp_review, url_prefix = BASE_URL)
    api.register_blueprint(blp_booking, url_prefix = BASE_URL)
    app.run(debug=True)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)