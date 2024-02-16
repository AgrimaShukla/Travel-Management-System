'''Controller for adding new booking'''

import logging
from handlers.booking_handler import BookingHandler
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes
from utils.logging_request_id import get_request_id
from config.prompt import PrintPrompts
from utils.error_handler import handle_custom_errors

logger = logging.getLogger(__name__)

class AddBookingController:
    '''Class for adding new booking'''

    def __init__(self) -> None:
        self.booking_handler = BookingHandler()

    @handle_custom_errors
    def create_booking(self, booking_data):
        '''Adding new booking'''
        logger.info(f'{get_request_id()} - Creating new booking')
        price, booking_id = self.booking_handler.add_booking(booking_data)
        response = {
            "price": price,
            "booking_id": booking_id
        }
        return CustomSuccessResponse(StatusCodes.CREATED, PrintPrompts.BOOKED_SUCCESSFULLY, response).jsonify_data
    