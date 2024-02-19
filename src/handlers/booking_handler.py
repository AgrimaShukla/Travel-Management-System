'''Business logic for handling bookings for customer'''

from shortuuid import ShortUUID
import logging
from datetime import datetime, timedelta
from flask_jwt_extended import get_jwt
from database.database_access import QueryExecutor
from config.queries import Query 
import pymysql
from utils.custom_error_response import ApplicationException, DBException
from handlers.package_handler import PackageHandler
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

class BookingHandler:
    '''This class handles customer booking of package'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()
        
    def add_booking(self, booking_data) -> None:
        '''Books the package for a customer'''

        try:
            logger.info('Adding new package')
            jwt = get_jwt()
            user_id = jwt.get('sub')
            package_id = booking_data["package_id"]
            price = self.db_access.single_data_returning_query(Query.SELECT_ONLY_PRICE, (package_id,))
            name = booking_data["name"]
            mobile_number = booking_data["mobile_number"]
            start_date = booking_data["start_date"]
            end_date = booking_data["end_date"]
            number_of_people = booking_data["number_of_people"]
            email = booking_data["email"]
            booking_id = "B_" + ShortUUID().random(length = 10)
            booking_date = str(datetime.now().date())
            total_price = number_of_people * price['price']
            user_details = (booking_id, booking_date, name, mobile_number, start_date, end_date, number_of_people, email) 
            trip_details = (booking_id, total_price, package_id, user_id, PrintPrompts.ACTIVE)
            self.db_access.insert_table(Query.INSERT_BOOKING, user_details, Query.INSERT_BOOKING_PACKAGE, trip_details)
            logger.info(f'{get_request_id} - Added new booking')
            return booking_id, total_price
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
       
    def get_booking_details(self, user_id) -> str:
        '''Display bookings of that particular customer'''

        try:
            logger.info(f"{get_request_id()} - Get all bookings")
            booking_data = self.db_access.returning_query(Query.SELECT_BOOKING, user_id)
            if not booking_data:
                logger.error(f"{get_request_id()} - No booking data found for user")
                raise ApplicationException(StatusCodes.NOT_FOUND, PrintPrompts.NO_BOOKINGS)
            logger.info(f"{get_request_id()} - Fetched booking data for user")
            return booking_data
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
    
    def get_active_booking(self, user_id):
        '''Get bookings that are not cancelled and their start date is more than 7 days away'''

        try:
            logger.info(f"{get_request_id()} - Getting bookings that can be cancelled")
            date = datetime.now().date() + timedelta(days = 7)
            booking_not_cancelled = self.db_access.returning_query(Query.BOOKING_NOT_CANCELLED, (user_id, PrintPrompts.ACTIVE, date))
            if booking_not_cancelled:
                logger.info(f"{get_request_id()} - Fetched bookings that can be cancelled")
                return booking_not_cancelled
            else:
                logger.error(f'{get_request_id()} - No bookings found for that user')
                raise ApplicationException(StatusCodes.NOT_FOUND, PrintPrompts.NO_BOOKINGS)
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)

    def  update_booking(self, booking_data, booking_id):
        '''Update a particular booking'''

        try:
            logger.info(f"{get_request_id()} - Updating a particular data")
            name = booking_data["name"]
            mobile_number = booking_data["mobile_number"]
            start_date = booking_data["start_date"]
            end_date = booking_data["end_date"]
            number_of_people = booking_data["number_of_people"]
            email = booking_data["email"]
            booking_details = (name, mobile_number, start_date, end_date, number_of_people, email, booking_id)
            package_obj = PackageHandler()
            package_data = self.db_access.single_data_returning_query(Query.SELECT_PACKAGE_FROM_BOOKING, (booking_id,))
            price = package_obj.get_price_of_package((package_data["package_id"],))
            new_price = price["price"] * number_of_people
            self.db_access.insert_table(Query.UPDATE_BOOKING, booking_details, Query.UPDATE_BOOKING_PACKAGE, (new_price, booking_id))
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)

    def cancel_booking(self, booking_id: str) -> None:
        '''To cancel the booking'''
        try:
            logger.info(f"{get_request_id()} - Cancelling booking with booking id {booking_id}")
            self.db_access.non_returning_query(Query.UPDATE_BOOKING_STATUS, (PrintPrompts.CANCELLED, booking_id))
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
        
