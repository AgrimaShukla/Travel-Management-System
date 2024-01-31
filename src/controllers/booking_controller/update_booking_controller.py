from handlers.booking_handler import BookingHandler
from utils.custom_response import CustomSuccessResponse
from config.status_code import StatusCodes
from config.prompt import PrintPrompts

class UpdateBookingController:

    def update_bookings(self, booking_data, booking_id):
        
        name = booking_data["name"]
        mobile_number = booking_data["mobile_number"]
        start_date = booking_data["start_date"]
        end_date = booking_data["end_date"]
        number_of_people = booking_data["number_of_people"]
        email = booking_data["email"]
        booking_details = (name, mobile_number, start_date, end_date, number_of_people, email, booking_id)
        BookingHandler().update_booking(booking_details)
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.UPDATED).jsonify_data
