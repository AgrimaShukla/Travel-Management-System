'''Controller for updating controller'''

import logging
from handlers.itinerary_handler import ItineraryHandler
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

class UpdateItineraryController:
    '''Class for updating itineraries'''
    def __init__(self) -> None:
        self.iti_handler = ItineraryHandler()
    
    def change_itinerary(self, itinerary_data, itinerary_id):
        '''Method to Update itineraries'''
        logger.info(f'{get_request_id()} - Updating itineraries')
        self.iti_handler.update_in_itinerary(itinerary_data, itinerary_id)
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.UPDATED).jsonify_data
       