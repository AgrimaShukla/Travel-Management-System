from flask.views import MethodView
from flask_smorest import Blueprint
from utils.role_based_access import role_based_access
from utils.role_mapping import Role
from controllers.booking_controller.get_booking_controller import GetBookingController
from controllers.booking_controller.get_active_booking_controller import GetActiveBookingController
from controllers.booking_controller.add_booking_controller import AddBookingController
from controllers.booking_controller.update_booking_controller import UpdateBookingController
from controllers.booking_controller.cancel_booking_controller import CancelBookingController
from schemas.booking_schema import GetBookingSchema, CreateBookingSchema, UpdateBookingSchema

blp_booking = Blueprint("Booking", __name__, description="Customer Booking")

@blp_booking.route("/booking")
class Booking(MethodView):

    @blp_booking.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_booking.response(200, GetBookingSchema(many=True))
    def get(self):
        return GetBookingController().get_bookings()
    
    @blp_booking.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_booking.arguments(CreateBookingSchema)
    def post(self, booking_data):
        return AddBookingController().create_booking(booking_data)

@blp_booking.route("/booking/active")
class Booking(MethodView):

    @blp_booking.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_booking.response(200, GetBookingSchema(many=True))
    def get(self):
        return GetActiveBookingController().get_active_booking()
    
@blp_booking.route("/booking/<string:booking_id>")
class UpdateBooking(MethodView):

    @blp_booking.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_booking.arguments(UpdateBookingSchema)
    def put(self, booking_data, booking_id):
        return UpdateBookingController().update_bookings(booking_data, booking_id)
    

@blp_booking.route("/booking/cancel/<string:booking_id>")
class CancelBooking(MethodView):
    @blp_booking.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    def put(self, booking_id):
        return CancelBookingController().cancel_bookings(booking_id)
