from flask_smorest import abort
from handlers.itinerary_handler import ItineraryHandler
from utils.exception import DBException
from config.prompt import PrintPrompts
from utils.custom_response import CustomSuccessResponse, CustomError
from config.status_code import StatusCodes

class UpdateItineraryController:
    def __init__(self) -> None:
        self.iti_handler = ItineraryHandler()
    
    def change_itinerary(self, itinerary_data, itinerary_id):
        try:
            itinerary_tuple = (itinerary_data['day'], itinerary_data['city'], itinerary_data['description'], itinerary_id)
            self.iti_handler.update_in_itinerary(itinerary_tuple)
            return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.UPDATED).jsonify_data
        except DBException as err:
            return CustomError(StatusCodes.NOT_FOUND, err).jsonify_data
