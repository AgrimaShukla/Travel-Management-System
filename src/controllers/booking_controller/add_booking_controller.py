from flask_jwt_extended import get_jwt
from handlers.booking_handler import BookingHandler
from utils.custom_response import CustomSuccessResponse
from config.status_code import StatusCodes
from config.prompt import PrintPrompts
from utils.validation import validate_date

class AddBookingController:

    def create_booking(self, booking_data):
        print(booking_data)
        jwt = get_jwt()
        user_id = jwt.get('sub')
        package_id = booking_data["package_id"]
        days_night = booking_data["days_night"]
        price = booking_data["price"]
        name = booking_data["name"]
        mobile_number = booking_data["mobile_number"]
        start_date = booking_data["start_date"]
        end_date = booking_data["end_date"]
        number_of_people = booking_data["number_of_people"]
        email = booking_data["email"]
        user_details = (name, mobile_number, start_date, end_date, number_of_people, email)
        trip_details = (package_id, user_id, PrintPrompts.ACTIVE)
        total_price = BookingHandler().add_booking(user_details, trip_details, days_night, price)
        return CustomSuccessResponse(StatusCodes.CREATED, PrintPrompts.BOOKED_SUCCESSFULLY.format(total_price)).jsonify_data
    