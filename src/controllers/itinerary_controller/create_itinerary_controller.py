'''Controller for adding new itinerary'''

import logging
from handlers.itinerary_handler import ItineraryHandler
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes
from utils.logging_request_id import get_request_id
from config.prompt import PrintPrompts
from utils.error_handler import handle_custom_errors

logger = logging.getLogger(__name__)

class CreateItineraryController:
    '''Class for creating a new itinerary'''
    def __init__(self) -> None:
        self.iti_handler = ItineraryHandler()

    @handle_custom_errors
    def create_new_itinerary(self, itinerary_data):
        '''Method to add new itinerary'''
        logger.info(f'{get_request_id()} - Adding new itinerary')
        itinerary_id = self.iti_handler.add_itinerary(itinerary_data)
        itinerary = [{
            "itinerary_id": itinerary_id
        }]
        return CustomSuccessResponse(StatusCodes.CREATED, PrintPrompts.ITINERARY_ADDED, itinerary).jsonify_data, 201
        