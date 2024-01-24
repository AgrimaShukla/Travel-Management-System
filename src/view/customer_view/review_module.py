'''This module is for customers review of their experience'''

from utils.pretty_print import data_tabulate
from config.prompt import InputPrompts, PrintPrompts, TabulateHeader
from config.regex_value import RegularExp
from controller.customer_controller.review import Review
from utils.validation import validate

class ReviewViews:
    '''Review added by customer for a package'''
    def __init__(self) -> None:
        self.review_obj = Review()


    def get_review(self, booking_id: str, package_id: str) -> None:
        '''Adding review by customer'''
        name = validate(RegularExp.NAME, InputPrompts.ENTER_DETAIL.format('NAME')) 
        comment = validate(RegularExp.STRING_VALUE, InputPrompts.ENTER_DETAIL.format('COMMENT'))
        added = self.review_obj.add_review(name, comment, booking_id, package_id)
        if added == True:
            print( PrintPrompts.ADDED)
        else:
            print(PrintPrompts.UNEXPECTED_ISSUE)


    def show_review(self, package_id: str) -> None:
        '''Showing review to customer'''
        comment = self.review_obj.get_reviews(package_id)
        data_tabulate(comment, (TabulateHeader.NAME, TabulateHeader.COMMENT, TabulateHeader.DATE))


    def show_data(self, customer_id: str) -> None:
        '''Showing their package details to customer'''
        data = self.review_obj.get_bookings(customer_id)
        if data == -1:
            print(PrintPrompts.NO_BOOKINGS)
            return
        data_tabulate(data, (TabulateHeader.BOOKING_ID, TabulateHeader.PACKAGE_ID, TabulateHeader.START_DATE, TabulateHeader.END_DATE))
        while True:
            booking_id = tuple(i[0] for i in data)
            enter_booking_id = input(InputPrompts.ENTER_DETAIL.format('BOOKING_ID'))
            if enter_booking_id not in booking_id:
                print(PrintPrompts.INVALID_BOOKING)
                continue
            package_id = self.review_obj.get_package_id(enter_booking_id, )
            self.get_review(enter_booking_id, package_id[0])
            print(PrintPrompts.REVIEW)
            break
    
    