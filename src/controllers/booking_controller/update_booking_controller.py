from handlers.booking_handler import BookingHandler

class UpdateBookingController:
    def cancel_bookings(self, user_data):
        name = user_data["name"]
        mobile_number = user_data["mobile_number"]
        start_date = user_data["start_date"]
        end_date = user_data["end_date"]
        number_of_people = user_data["number_of_people"]
        email = user_data["email"]
        booking_id = user_data["booking_id"]
        BookingHandler().cancel_booking(booking_id)
    
