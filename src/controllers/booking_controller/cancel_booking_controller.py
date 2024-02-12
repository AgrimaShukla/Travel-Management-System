'''Controller for cancelling booking'''

import logging
from handlers.booking_handler import BookingHandler
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes
from utils.logging_request_id import get_request_id
from config.prompt import PrintPrompts
from utils.error_handler import handle_custom_errors

logger = logging.getLogger(__name__)

class CancelBookingController:
    '''Class for cancelling Booking'''

    def __init__(self) -> None:
        self.booking_handler = BookingHandler()

    @handle_custom_errors
    def cancel_bookings(self, booking_id):
        '''User cancelling booking'''
        logger.info(f'{get_request_id()} - Cancelling a booking')
        self.booking_handler.cancel_booking(booking_id)
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.CANCELLED).jsonify_data
