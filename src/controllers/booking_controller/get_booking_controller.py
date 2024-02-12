'''Controller for getting booking details'''

import logging
from flask_jwt_extended import get_jwt_identity
from handlers.booking_handler import BookingHandler
from utils.error_handler import handle_custom_errors
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

class GetBookingController:
    '''Class for getting all bookings'''
    def __init__(self) -> None:
        self.booking_handler = BookingHandler()

    @handle_custom_errors
    def get_bookings(self):
        '''Method for getting bookings for a particular user'''
        logger.info(f'{get_request_id()} - Get all bookings')
        user_id = get_jwt_identity()
        booking_details = self.booking_handler.get_booking_details((user_id,))
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.SUCCESS, booking_details).jsonify_data
        

