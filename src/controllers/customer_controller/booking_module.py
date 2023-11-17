''' This module is for customer to view and book package'''
from shortuuid import ShortUUID
import logging
from datetime import datetime, timedelta

from src.config.prompt_values import DESTINATION_DICT, CATEGORY_DICT, DAY_DICT
from src.utils.pretty_print import data_tabulate
from src.utils import validation
from src.config.prompt import PrintPrompts, InputPrompts, LoggingPrompt, TabulateHeader
from src.database import database_access
from src.config.queries import Query 
from src.config.regex_value import RegularExp
from src.controllers.customer_controller.review_module import show_review

logger = logging.getLogger(__name__)

def check_date() -> None:
    '''Checking date if valid or not'''
    print(PrintPrompts.DATE)
    while True:
        date_str = input(InputPrompts.ENTER)
        try:
            start_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            if start_date > datetime.now().date():
                return start_date
            elif start_date <= datetime.now().date():
                print(PrintPrompts.INVALID_DATE)
            else: 
                print(PrintPrompts.INVALID_DATE_FORMAT)
        except ValueError:
            logger.exception(ValueError)
            print(PrintPrompts.INVALID_DATE)

class BookPackage:
    '''This class handles customer booking of package'''
    def __init__(self, package_id: str, customer_id: str, days_night: str, price: int) -> None:
        while True:
            self.package_id = package_id
            self.customer_id = customer_id
            self.price = price
            self.booking_id = "B_" + ShortUUID().random(length = 10)
            self.name = validation.validate(InputPrompts.INPUT.format("name"), RegularExp.NAME)
            self.mobile_no = validation.validate(InputPrompts.INPUT.format("mobile no"), RegularExp.MOBILE_NUMBER)
            start_date = check_date()
            self.end_date = start_date + timedelta(days = days_night)
            self.number_of_people = validation.validate(InputPrompts.NO_OF_PEOPLE, RegularExp.PERSON)
            self.email = validation.validate(InputPrompts.EMAIL, RegularExp.EMAIL)
            self.booking_date = datetime.now().date()
            data = (self.booking_id, self.name, self.mobile_no, start_date, self.end_date, self.number_of_people, self.email, self.booking_date)
            self.add_booking(data)
            break
        
    def add_booking(self, booking: tuple) -> None:
        '''Books the package for a customer'''
        total_price = int(self.number_of_people) * self.price
        package = (self.package_id, self.customer_id, self.booking_id, total_price, 'ongoing')
        value = database_access.insert_table(Query.INSERT_BOOKING, booking, Query.INSERT_BOOKING_PACKAGE, package)
        if value == True:
            print(PrintPrompts.BOOKED_SUCCESSFULLY.format(total_price, self.booking_id))
            logger.info(LoggingPrompt.BOOKED)


def display_booking(query: str, data: tuple) -> str:
    '''Display bookings of that particular customer'''
    data_booking = database_access.returning_query(query, data)
   
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


def show_itinerary_package(customer_id: str) -> None:
    '''show itinerary for that package and particular customer'''
    booking_id = display_booking(Query.SELECT_BOOKING, (customer_id, ))
    if booking_id:
        data_itinerary = database_access.returning_query(Query.PACKAGE_FROM_BOOKING, (booking_id, ))
        data_tabulate(data_itinerary, (TabulateHeader.DAY, TabulateHeader.CITY, TabulateHeader.DESC))

 
def cancel_booking(customer_id: str) -> None:
    '''To cancel the booking'''
    booking_id = display_booking(Query.BOOKING_NOT_CANCELLED, (customer_id, 'ongoing', datetime.now().date() + timedelta(days = 7)))
    if booking_id:
        database_access.non_returning_query(Query.UPDATE_BOOKING, ('cancelled', booking_id), PrintPrompts.CANCELLED)


def view_package(destination: str, category: str, days_night: str, customer_id: str) -> None:
    '''To view the package after user preferences'''
    dest_value = DESTINATION_DICT[destination]
    category_value = CATEGORY_DICT[category]
    day_value = DAY_DICT[days_night]
    
    data = (dest_value, category_value, day_value, 'active')
    itinerary = database_access.returning_query(Query.SELECT_ITINERARY, data)
    package_data = database_access.single_data_returning_query(Query.SELECT_PRICE, data)
    data_tabulate(itinerary, (TabulateHeader.DAY, TabulateHeader.CITY, TabulateHeader.DESC))
    print(PrintPrompts.PRICE.format(package_data[1]))

    while True:
        print(PrintPrompts.BOOKING)
        parameter = input(InputPrompts.ENTER)
        match parameter:
            case '1':
                # to fetch no of days from duration to calculate end time of journey
                words = package_data[2].split()
                day = int(words[0])
                BookPackage(package_data[0], customer_id, day, package_data[1])
            case '2': 
                show_review(package_data[0])
            case '3': break
            case _: print(PrintPrompts.INVALID_PROMPT)
