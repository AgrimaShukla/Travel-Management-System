from shortuuid import ShortUUID
import logging
from datetime import datetime, timedelta
from database.database_access import QueryExecutor
from config.queries import Query 

logger = logging.getLogger(__name__)

class BookingHandler:
    '''This class handles customer booking of package'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()
        
    def add_booking(self, user_details, trip_details, days_night, price) -> None:
        '''Books the package for a customer'''
        
        booking_id = "B_" + ShortUUID().random(length = 10)
        booking_date = datetime.now().date()
        start_date = user_details[2]
        end_date = start_date + timedelta(days = days_night)
        user_details = (booking_id, end_date, booking_date) + user_details 
        total_price = int(user_details[3]) * price
        trip_details = (booking_id, total_price) + trip_details
        self.db_access.insert_table(Query.INSERT_BOOKING, user_details, Query.INSERT_BOOKING_PACKAGE, trip_details)
        return total_price

    def get_booking_details(self, user_id) -> str:
        '''Display bookings of that particular customer'''
        data_booking = self.db_access.returning_query(Query.SELECT_BOOKING, user_id)
        return data_booking
    
    def update_booking(self, booking_data):
        self.db_access.non_returning_query(Query.UPDATE_BOOKING, booking_data)

    def cancel_booking(self, booking_id: str) -> None:
        '''To cancel the booking'''
        self.db_access.non_returning_query(Query.UPDATE_BOOKING_STATUS, ('cancelled', booking_id))
        
