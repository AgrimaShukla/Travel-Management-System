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
        database_access.insert_table(Query.INSERT_BOOKING, booking, Query.INSERT_BOOKING_PACKAGE, package, PrintPrompts.BOOKED_SUCCESSFULLY.format(total_price, self.booking_id))
        logger.info(LoggingPrompt.BOOKED)
        

    @staticmethod
    def show_booking(query_to_execute: str, tuple_of_data: tuple) -> tuple:
        '''Display the booking'''
        data_booking = database_access.returning_query(query_to_execute, tuple_of_data)
        if data_booking:
            # data to be shown to user
            filtered_view = [] 
            # to map user input with booking id
            id_days = dict() 
            row_value = 1
            # append data in list to display to user
            for it in data_booking:
                id_days[row_value] = it[0]
                filtered_view.append((it[1:]))
                row_value = row_value + 1

            tuple_of_data = (filtered_view, id_days)
            return tuple_of_data


    @staticmethod
    def show_booking_package(customer_id: str) -> tuple:
        '''Display the package of that booking'''
        tuple_of_data = BookPackage.show_booking(Query.SELECT_BOOKING, (customer_id,))
        while True:
            if tuple_of_data:
                # to display data using tabulate
                data_tabulate(tuple_of_data[0], (TabulateHeader.NAME, TabulateHeader.MOBILE_NUMBER, TabulateHeader.START_DATE, TabulateHeader.END_DATE, TabulateHeader.NO_OF_PEOPLE, TabulateHeader.EMAIL, TabulateHeader.BOOKING_DATE, TabulateHeader.STATUS))
                try:
                    option = int(input(InputPrompts.ENTER))
                    if option in tuple_of_data[1]:
                        data = database_access.returning_query(Query.PACKAGE_FROM_BOOKING, (tuple_of_data[1][option], ))
                        # to display data using tabulate
                        data_tabulate(data, (TabulateHeader.DAY, TabulateHeader.CITY, TabulateHeader.DESC))
                        return tuple_of_data[1][option]
                    else: 
                        print(PrintPrompts.INVALID_PROMPT)
                except ValueError:
                    print(PrintPrompts.INVALID_PROMPT)
            else:
                print(PrintPrompts.NO_BOOKINGS)
                break


    @staticmethod  
    def cancel_booking(customer_id: str) -> None:
        '''To cancel the booking'''
        tuple_of_data = BookPackage.show_booking(Query.BOOKING_NOT_CANCELLED, (customer_id, 'ongoing'))
        while True:
            if tuple_of_data:
                # to display using tabulate
                data_tabulate(tuple_of_data[0], (TabulateHeader.NAME, TabulateHeader.MOBILE_NUMBER, TabulateHeader.START_DATE, TabulateHeader.END_DATE, TabulateHeader.NO_OF_PEOPLE, TabulateHeader.EMAIL, TabulateHeader.BOOKING_DATE))
                try:
                    option = int(input(InputPrompts.ENTER))
                    if option in tuple_of_data[1]:
                        database_access.non_returning_query(Query.UPDATE_BOOKING, ('cancelled', tuple_of_data[1][option]), PrintPrompts.CANCELLED)
                        break
                    print(PrintPrompts.INVALID_PROMPT)
                except ValueError:
                    print(PrintPrompts.INVALID_PROMPT)
            else:
                print(PrintPrompts.NO_BOOKINGS)
                break


def view_package(destination: str, category: str, days_night: str, customer_id: str) -> None:
    '''To view the package after user preferences'''

    dest_value = DESTINATION_DICT[destination]
    category_value = CATEGORY_DICT[category]
    day_value = DAY_DICT[days_night]
    
    data = (dest_value, category_value, day_value, 'active')
    itinerary = database_access.returning_query(Query.SELECT_ITINERARY, data)

    # data to be shown to user
    filtered_view = [] 
    # to map duration with package id
    id_days = {} 

    # append data in list to display to user
    for it in itinerary:
        id_days[it[0]] = it[1]
        filtered_view.append((it[2:]))

    price = database_access.single_data_returning_query(Query.SELECT_PRICE, data)
    # using tabulate to display data
    data_tabulate(filtered_view, (TabulateHeader.DAY, TabulateHeader.CITY, TabulateHeader.DESC))

    print(PrintPrompts.PRICE.format(price[0]))
    while True:
        print(PrintPrompts.BOOKING)
        parameter = input(InputPrompts.ENTER)
        match parameter:
            case '1':
                package_id = list(id_days.keys())
                days = list(id_days.values())
                # to fetch no of days from duration to calculate end time of journey
                words = days[0].split()
                day = int(words[0])
                BookPackage(package_id[0], customer_id, day, price[0])
            case '2': break
            case _: print(PrintPrompts.INVALID_PROMPT)
