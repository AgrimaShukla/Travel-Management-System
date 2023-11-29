''' This module is for customer to view and book package'''
from shortuuid import ShortUUID
import logging
from datetime import datetime, timedelta

from utils.pretty_print import data_tabulate
from utils import validation
from config.prompt import PrintPrompts, InputPrompts, LoggingPrompt, TabulateHeader
from database.database_access import QueryExecutor
from config.queries import Query 
from config.regex_value import RegularExp

logger = logging.getLogger(__name__)

class BookPackage:
    '''This class handles customer booking of package'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()
        
    def add_booking(self, package_id: str, customer_id: str, days_night: str, price: int) -> None:
        '''Books the package for a customer'''
    
        booking_id = "B_" + ShortUUID().random(length = 10)
        name = validation.validate(InputPrompts.INPUT.format("name"), RegularExp.NAME)
        mobile_no = validation.validate(InputPrompts.INPUT.format("mobile no"), RegularExp.MOBILE_NUMBER)
        print(start_date)
        start_date = validation.validate_date()
        end_date = start_date + timedelta(days = days_night)
        print(end_date)
        number_of_people = validation.validate(InputPrompts.NO_OF_PEOPLE, RegularExp.PERSON)
        email = validation.validate(InputPrompts.EMAIL, RegularExp.EMAIL)
        booking_date = datetime.now().date()
        data_booking = (booking_id, name, mobile_no, start_date, end_date, number_of_people, email, booking_date)
        total_price = int(number_of_people) * price
        data_package = (package_id, customer_id, booking_id, total_price, 'ongoing')
        value = self.db_access.insert_table(Query.INSERT_BOOKING, data_booking, Query.INSERT_BOOKING_PACKAGE, data_package)
        if value == True:
            print(PrintPrompts.BOOKED_SUCCESSFULLY.format(total_price, booking_id))
            logger.info(LoggingPrompt.BOOKED)


    def display_booking(self, query: str, data: tuple) -> str:
        '''Display bookings of that particular customer'''
        data_booking = self.db_access.returning_query(query, data)
    
        if data_booking:
            # to display data using tabulate
            data_tabulate(data_booking, (TabulateHeader.BOOKING_ID, TabulateHeader.NAME, TabulateHeader.MOBILE_NUMBER, TabulateHeader.START_DATE, TabulateHeader.END_DATE, TabulateHeader.NO_OF_PEOPLE, TabulateHeader.EMAIL, TabulateHeader.BOOKING_DATE, TabulateHeader.STATUS))
            while True:
                booking_id = validation.validate_uuid(InputPrompts.ENTER_DETAIL.format("BOOKING ID: "), RegularExp.UUID)
                booking_id_lst = []
                for value in data_booking:
                    booking_id_lst.append(value[0])
                if booking_id in booking_id_lst:
                    return booking_id
                print(PrintPrompts.BOOKING_ID.format(booking_id))
        else:
            print(PrintPrompts.NO_BOOKINGS)


    def show_itinerary_package(self, customer_id: str) -> None:
        '''show itinerary for that package and particular customer'''
        booking_id = self.display_booking(Query.SELECT_BOOKING, (customer_id, ))
        if booking_id:
            data_itinerary = self.db_access.returning_query(Query.PACKAGE_FROM_BOOKING, (booking_id, ))
            data_tabulate(data_itinerary, (TabulateHeader.DAY, TabulateHeader.CITY, TabulateHeader.DESC))

    
    def cancel_booking(self, customer_id: str) -> None:
        '''To cancel the booking'''
        booking_id = self.display_booking(Query.BOOKING_NOT_CANCELLED, (customer_id, 'ongoing', datetime.now().date() + timedelta(days = 7)))
        if booking_id:
            self.db_access.non_returning_query(Query.UPDATE_BOOKING, ('cancelled', booking_id), PrintPrompts.CANCELLED)
