from shortuuid import ShortUUID
import logging
from datetime import datetime, timedelta

from utils.pretty_print import data_tabulate
from config.prompt import PrintPrompts, InputPrompts, LoggingPrompt, TabulateHeader
from database.database_access import QueryExecutor
from config.queries import Query 
from utils.exception import exception_handler

logger = logging.getLogger(__name__)

class BookPackage:
    '''This class handles customer booking of package'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()

    @exception_handler 
    def add_booking(self, package_id: str, customer_id: str, days_night: str, price: int, name, mobile_no, start_date, number_of_people, email) -> None:
        '''Books the package for a customer'''
        
        booking_id = "B_" + ShortUUID().random(length = 10)
        booking_date = datetime.now().date()
        end_date = start_date + timedelta(days = days_night)
        data_booking = (booking_id, name, mobile_no, start_date, end_date, number_of_people, email, booking_date)
        total_price = int(number_of_people) * price
        data_package = (package_id, customer_id, booking_id, total_price, 'ongoing')
        value = self.db_access.insert_table(Query.INSERT_BOOKING, data_booking, Query.INSERT_BOOKING_PACKAGE, data_package)
        return value

    @exception_handler
    def get_details(self, query: str, data: tuple) -> str:
        '''Display bookings of that particular customer'''
        data_booking = self.db_access.returning_query(query, data)
        return data_booking
    
    @exception_handler
    def cancel_booking(self, booking_id: str) -> None:
        '''To cancel the booking'''
        result = self.db_access.non_returning_query(Query.UPDATE_BOOKING, ('cancelled', booking_id))
        return result
