'''Controllers for fetching itinerary'''

import os
import logging
from handlers.itinerary_handler import ItineraryHandler
from flask import request
from flask_jwt_extended import get_jwt_identity
from utils.custom_error_response import CustomError
from config.status_code import StatusCodes
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from dotenv import load_dotenv
from utils.error_handler import handle_custom_errors

logger = logging.getLogger(__name__)

load_dotenv()

ADMIN = os.getenv('ADMIN')
CUSTOMER = os.getenv('CUSTOMER')

class GetItineraryController:
    '''Class for getting new itinerary'''
    def __init__(self) -> None:
        self.iti_handler = ItineraryHandler()

    @handle_custom_errors
    def get_itinerary_details(self):
        '''
        Getting itinerary based on role.
        Admin - allowed to access all itineraries
        Customer - allowed to access filtered itineraries
        '''

        logger.info(f'{get_request_id()} - Getting itineraries')
        query_parameter = request.args
        provided_parameters = list(request.args.keys())
        role = get_jwt_identity('role')
    
        if role == ADMIN and not query_parameter:
            logger.debug(f'{get_request_id()} - Fetching itinerary for admin')
            result = self.iti_handler.fetch_itinerary()
            return result
        elif role == CUSTOMER and len(provided_parameters) == 3:
            logger.debug(f'{get_request_id()} - Fetching itinerary for customer')
            destination = request.args.get("destination")
            category = request.args.get("category")
            days_night = request.args.get("days_night")
            days_night = days_night.replace('-', ' ')  
            result = self.iti_handler.get_particular_itinerary(destination, category, days_night)
            return result
        else:
            return CustomError(StatusCodes.BAD_REQUEST, PrintPrompts.INVALID_REQUEST).jsonify_data, StatusCodes.BAD_REQUEST
        