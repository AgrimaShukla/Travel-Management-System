from flask_jwt_extended import get_jwt
from handlers.booking_handler import BookingHandler

class GetBookingController:
    def get_bookings(self):
        jwt = get_jwt()
        user_id = jwt.get('sub')
        booking_details = BookingHandler().get_booking_details((user_id,))
        return booking_details
