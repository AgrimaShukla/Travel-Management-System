from flask_smorest import abort
from handlers.itinerary_handler import ItineraryHandler
from utils.exception import DBException
from utils.custom_response import CustomSuccessResponse, CustomError
from config.status_code import StatusCodes
from config.prompt import PrintPrompts

class CreateItineraryController:
    def __init__(self) -> None:
        self.iti_handler = ItineraryHandler()

    def create_new_itinerary(self, itinerary_data):
        try:
            self.iti_handler.add_itinerary(itinerary_data["package_id"], itinerary_data["day"], itinerary_data["city"], itinerary_data["description"])
            return CustomSuccessResponse(StatusCodes.CREATED, PrintPrompts.ITINERARY_ADDED).jsonify_data
        except DBException as err:
            return CustomError(StatusCodes.NOT_FOUND, err).jsonify_data