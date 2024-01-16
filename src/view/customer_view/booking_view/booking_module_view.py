''' This module is for customer to view and book package'''
import logging
from datetime import datetime, timedelta

from utils.pretty_print import data_tabulate
from config.prompt import PrintPrompts, InputPrompts, LoggingPrompt, TabulateHeader
from config.queries import Query 
from utils.validation import validate, validate_date
from config.regex_value import RegularExp

from controller.customer_controller.booking_controller.booking_module import BookPackage
logger = logging.getLogger(__name__)

class BookingPackageView:
    '''This class handles customer booking of package'''
    def __init__(self) -> None:
        self.booking = BookPackage()
        
    def booking_details(self, package_id: str, customer_id: str, days_night: str, price: int) -> None:
        '''Books the package for a customer'''
        name = validate(RegularExp.NAME, InputPrompts.INPUT.format("name"))
        mobile_no = validate(RegularExp.MOBILE_NUMBER, InputPrompts.INPUT.format("mobile no"))
        start_date = validate_date()
        number_of_people = validate(RegularExp.PERSON, InputPrompts.NO_OF_PEOPLE)
        email = validate(RegularExp.EMAIL, InputPrompts.EMAIL)
        if_booked = self.booking.add_booking(package_id, customer_id, days_night, price, name, mobile_no, start_date, number_of_people, email)
        total_price = int(number_of_people) * price
        if if_booked == True:
            print(PrintPrompts.BOOKED_SUCCESSFULLY.format(total_price))
            logger.info(LoggingPrompt.BOOKED)
        else:
            print(PrintPrompts.UNEXPECTED_ISSUE)


    def display_booking(self, query: str, data: tuple) -> str:
        '''Display bookings of that particular customer'''
        data_booking = self.booking.get_details(query, data)
    
        if data_booking:
            # to display data using tabulate
            data_tabulate(data_booking, (TabulateHeader.BOOKING_ID, TabulateHeader.NAME, TabulateHeader.MOBILE_NUMBER, TabulateHeader.START_DATE, TabulateHeader.END_DATE, TabulateHeader.NO_OF_PEOPLE, TabulateHeader.EMAIL, TabulateHeader.BOOKING_DATE, TabulateHeader.STATUS))
            while True:
                booking_id = input(InputPrompts.ENTER_DETAIL.format("BOOKING ID: "))
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
            data_itinerary = self.booking.get_details(Query.PACKAGE_FROM_BOOKING, (booking_id, ))
            data_tabulate(data_itinerary, (TabulateHeader.DAY, TabulateHeader.CITY, TabulateHeader.DESC))

    
    def cancel_booking(self, customer_id: str) -> None:
        '''To cancel the booking'''
        booking_id = self.display_booking(Query.BOOKING_NOT_CANCELLED, (customer_id, 'ongoing', datetime.now().date() + timedelta(days = 7)))
        if booking_id:
            result = self.booking.cancel_booking(booking_id)
            if result == True:
                print(PrintPrompts.CANCELLED)
            else:
                print(PrintPrompts.UNEXPECTED_ISSUE)

