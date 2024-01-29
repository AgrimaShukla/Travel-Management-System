from handlers.booking_handler import BookingHandler

class CancelBookingController:
    def cancel_bookings(self, booking_id):
        BookingHandler().cancel_booking(booking_id)
    
