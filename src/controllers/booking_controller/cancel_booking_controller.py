from handlers.booking_handler import BookingHandler
from utils.custom_response import CustomSuccessResponse
from config.status_code import StatusCodes
from config.prompt import PrintPrompts

class CancelBookingController:
    
    def cancel_bookings(self, booking_id):
        BookingHandler().cancel_booking(booking_id)
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.CANCELLED).jsonify_data
