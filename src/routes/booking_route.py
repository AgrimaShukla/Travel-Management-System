'''Routes for booking related operations'''

import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from utils.role_based_access import role_based_access
from utils.role_mapping import Role
from controllers.booking_controller.get_booking_controller import GetBookingController
from controllers.booking_controller.get_active_booking_controller import GetActiveBookingController
from controllers.booking_controller.add_booking_controller import AddBookingController
from controllers.booking_controller.update_booking_controller import UpdateBookingController
from controllers.booking_controller.cancel_booking_controller import CancelBookingController
from utils.logging_request_id import get_request_id
from schemas.booking_schema import GetBookingSchema, CreateBookingSchema, UpdateBookingSchema

logger = logging.getLogger(__name__)

blp_booking = Blueprint("Booking", __name__, description="Customer Booking")

@blp_booking.route("/v1/booking")
class Booking(MethodView):
    '''
    Route for:-  
    - Getting booking details
    - Adding new booking
    '''

    @blp_booking.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_booking.response(200, GetBookingSchema(many=True))
    def get(self):
        '''Get all bookings for a particular customer'''
        logger.info(f"{get_request_id()} -  route for getting all bookings")
        return GetBookingController().get_bookings()
    
    @blp_booking.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_booking.arguments(CreateBookingSchema)
    def post(self, booking_data):
        '''Posting new booking'''
        logger.info(f"{get_request_id()} -  route for posting bookings")
        return AddBookingController().create_booking(booking_data)

@blp_booking.route("/v1/booking/active")
class Booking(MethodView):
    '''
    Route for:-
    - Getting active bookings
    '''

    @blp_booking.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_booking.response(200, GetBookingSchema(many=True))
    def get(self):
        '''Getting all non cancelled booking'''
        logger.info(f"{get_request_id()} -  route for get non cancelled booking")
        return GetActiveBookingController().get_active_booking()
    

@blp_booking.route("/v1/booking/<string:booking_id>")
class UpdateBooking(MethodView):
    '''
    Route for:-
    - Updating booking details
    '''

    @blp_booking.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_booking.arguments(UpdateBookingSchema)
    def put(self, booking_data, booking_id):
        '''Updating booking details'''
        logger.info(f"{get_request_id()} -  route for changing booking details")
        return UpdateBookingController().update_bookings(booking_data, booking_id)
    
@blp_booking.route("/v1/booking/cancel/<string:booking_id>")
class CancelBooking(MethodView):
    '''
    Route for:-
    - Cancelling booking
    '''

    @blp_booking.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    def put(self, booking_id):
        '''Cancelling booking'''
        logger.info(f"{get_request_id()} -  route for cancelling booking")
        return CancelBookingController().cancel_bookings(booking_id)
