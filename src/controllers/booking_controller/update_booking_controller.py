'''Controller for updating booking'''

import logging
from handlers.booking_handler import BookingHandler
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from utils.error_handler import handle_custom_errors

logger = logging.getLogger(__name__)

class UpdateBookingController:
    '''Class for updating booking'''
    def __init__(self) -> None:
        self.booking_handler = BookingHandler()

    @handle_custom_errors
    def update_bookings(self, booking_data, booking_id):
        '''Method to update a particular booking'''
        logger.info(f'{get_request_id()} - Updating a particular booking')
        self.booking_handler.update_booking(booking_data, booking_id)
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.UPDATED).jsonify_data
