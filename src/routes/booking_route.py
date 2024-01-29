from flask.views import MethodView
from flask_smorest import Blueprint
from utils.role_based_access import role_based_access
from utils.role_mapping import Role
from controllers.booking_controller.get_booking_controller import GetBookingController
from controllers.booking_controller.add_booking_controller import AddBookingController
from schemas.booking_schema import GetBookingSchema, CreateBookingSchema

blp_booking = Blueprint("Booking", __name__, description="Customer Booking")

@blp_booking.route("/booking")
class Booking(MethodView):

    @blp_booking.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_booking.response(200, GetBookingSchema)
    def get(self):
        return GetBookingController().get_bookings()
    
    @blp_booking.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_booking.arguments(CreateBookingSchema)
    def post(self, booking_data):
        return AddBookingController().create_booking(booking_data)
