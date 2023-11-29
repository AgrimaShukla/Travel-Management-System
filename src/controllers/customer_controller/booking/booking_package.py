'''This module is to show packages on the basis of options selected by user to further book the package'''

from config.prompt_values import DESTINATION_DICT, CATEGORY_DICT, DAY_DICT
from database.database_access import QueryExecutor
from controllers.customer_controller.review_module import Review
from config.prompt import InputPrompts, PrintPrompts, TabulateHeader
from utils.pretty_print import data_tabulate
from config.queries import Query 
from controllers.customer_controller.booking.booking_module import BookPackage

def view_package(destination: str, category: str, days_night: str, customer_id: str) -> None:
        '''To view the package after user preferences'''

        dest_value = DESTINATION_DICT[destination]
        category_value = CATEGORY_DICT[category]
        day_value = DAY_DICT[days_night]
        
        obj_query_executor = QueryExecutor()
        data = (dest_value, category_value, day_value, 'active')
        itinerary = obj_query_executor.returning_query(Query.SELECT_ITINERARY, data)
        package_data = obj_query_executor.single_data_returning_query(Query.SELECT_PRICE, data)
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
                    obj_book_package = BookPackage()
                    obj_book_package.add_booking(package_data[0], customer_id, day, package_data[1])
                case '2': 
                    obj_review = Review()
                    obj_review.show_review(package_data[0])
                case '3': break
                case _: print(PrintPrompts.INVALID_PROMPT)
                 