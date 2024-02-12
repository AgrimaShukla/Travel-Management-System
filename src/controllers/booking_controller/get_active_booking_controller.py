'''Controller for getting Active bookings'''

import logging
from flask_jwt_extended import get_jwt_identity
from handlers.booking_handler import BookingHandler
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from utils.custom_success_response import CustomSuccessResponse
from utils.error_handler import handle_custom_errors
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)
                           
class GetActiveBookingController:
    '''Class get bookings that are not cancelled'''

    def __init__(self) -> None:
        self.booking_handler = BookingHandler()

    @handle_custom_errors
    def get_active_booking(self):
        '''Get active bookings'''
        logger.info(f'{get_request_id()} - Getting non cancelled booking')
        user_id = get_jwt_identity()
        booking_details = self.booking_handler.get_active_booking(user_id)
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.SUCCESS, booking_details).jsonify_data
       

        
