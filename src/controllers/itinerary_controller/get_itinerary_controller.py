from flask_smorest import abort
from handlers.itinerary_handler import ItineraryHandler
from utils.exception import DBException
from config.prompt import PrintPrompts
from utils.custom_response import CustomError
from config.status_code import StatusCodes

class GetItineraryController:
    def __init__(self) -> None:
        self.iti_handler = ItineraryHandler()

    def get_itinerary_details(self):
        try:
            result = self.iti_handler.fetch_itinerary()
            return result
        except DBException as err:
            return CustomError(StatusCodes.NOT_FOUND, err).jsonify_data