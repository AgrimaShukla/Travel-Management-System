'''This module is to show packages on the basis of options selected by user to further book the package'''

from config.prompt import InputPrompts, PrintPrompts, TabulateHeader
from utils.pretty_print import data_tabulate
from view.customer_view.booking_view.booking_module_view import BookingPackageView
from view.customer_view.review_module import ReviewViews
from controller.customer_controller.booking_controller.get_package import get_package

def view_package(destination: str, category: str, days_night: str, customer_id: str) -> None:
        '''To view the package after user preferences'''
        itinerary, package_data = get_package(destination, category, days_night)
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
                    obj_book_package = BookingPackageView()
                    obj_book_package.booking_details(package_data[0], customer_id, day, package_data[1])
                case '2': 
                    obj_review = ReviewViews()
                    obj_review.show_review(package_data[0])
                case '3': break
                case _: print(PrintPrompts.INVALID_PROMPT)
                 