from shortuuid import ShortUUID
import logging
from datetime import datetime, timedelta
from database.database_access import QueryExecutor
from config.queries import Query 
from utils.exception import DataNotFound
from handlers.package_handler import PackageHandler
from config.prompt import PrintPrompts
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

class BookingHandler:
    '''This class handles customer booking of package'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()
        
    def add_booking(self, user_details, trip_details, days_night, price) -> None:
        '''Books the package for a customer'''
       
        booking_id = "B_" + ShortUUID().random(length = 10)
        booking_date = str(datetime.now().date())
        user_details = (booking_id, booking_date) + user_details 
        total_price = user_details[6] * price
        trip_details = (booking_id, total_price) + trip_details
        self.db_access.insert_table(Query.INSERT_BOOKING, user_details, Query.INSERT_BOOKING_PACKAGE, trip_details)
        return total_price
       
    def get_booking_details(self, user_id) -> str:
        '''Display bookings of that particular customer'''
        booking_data = self.db_access.returning_query(Query.SELECT_BOOKING, user_id)
        return booking_data
    
    def get_active_booking(self, booking_data):
        booking_not_cancelled = self.db_access.returning_query(Query.BOOKING_NOT_CANCELLED, booking_data)
        if booking_not_cancelled:
            return booking_not_cancelled
        else:
            raise DataNotFound(StatusCodes.NOT_FOUND, PrintPrompts.NO_BOOKINGS)

    def update_booking(self, booking_data):
        package_obj = PackageHandler()
        package_data = self.db_access.single_data_returning_query(Query.SELECT_PACKAGE_FROM_BOOKING, (booking_data[6],))
        price = package_obj.get_price_of_package((package_data["package_id"],))
        new_price = price["price"] * booking_data[4]
        self.db_access.insert_table(Query.UPDATE_BOOKING, booking_data, Query.UPDATE_BOOKING_PACKAGE, (new_price, booking_data[6]))

    def cancel_booking(self, booking_id: str) -> None:
        '''To cancel the booking'''
        self.db_access.non_returning_query(Query.UPDATE_BOOKING_STATUS, (PrintPrompts.CANCELLED, booking_id))
        
