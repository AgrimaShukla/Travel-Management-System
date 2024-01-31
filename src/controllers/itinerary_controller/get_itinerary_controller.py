from flask_smorest import abort
from handlers.itinerary_handler import ItineraryHandler
from utils.exception import DBException
from flask import request
from flask_jwt_extended import get_jwt
from utils.custom_response import CustomError
from config.status_code import StatusCodes
from config.prompt import PrintPrompts
import os
from dotenv import load_dotenv

load_dotenv()


ADMIN = os.getenv('ADMIN')
CUSTOMER = os.getenv('CUSTOMER')

class GetItineraryController:
    def __init__(self) -> None:
        self.iti_handler = ItineraryHandler()

    def get_itinerary_details(self):
        try:
            query_parameter = request.args
            provided_parameters = list(request.args.keys())
            jwt = get_jwt()
            role = jwt.get('role')
            if role == ADMIN and not query_parameter:
                result = self.iti_handler.fetch_itinerary()
                return result
            elif role == CUSTOMER and len(provided_parameters) == 3:
                destination = request.args.get("destination")
                category = request.args.get("category")
                days_night = request.args.get("days_night")
                days_night = days_night.replace('-', ' ')  
                result = self.iti_handler.get_particular_itinerary(destination, category, days_night)
                return result
            else:
                return CustomError(StatusCodes.BAD_REQUEST, PrintPrompts.INVALID_REQUEST).jsonify_data
        except DBException as err:
            return CustomError(StatusCodes.NOT_FOUND, err).jsonify_data