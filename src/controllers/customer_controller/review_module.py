'''This module is for customers review of their experience'''
import shortuuid
from datetime import datetime
from src.database import database_access
from src.config.queries import Query
from src.utils.pretty_print import data_tabulate
from src.utils.validation import validate, validate_uuid
from src.config.prompt import InputPrompts, PrintPrompts, TabulateHeader
from src.config.regex_value import RegularExp

class Review:
    '''Review added by customer for a package'''
    def __init__(self, booking_id: str, package_id: str) -> None:
        self.booking_id = booking_id
        self.package_id = package_id
        self.name = validate(InputPrompts.ENTER_DETAIL.format('NAME'), RegularExp.NAME)
        self.date = datetime.now().date()
        self.comment = validate(InputPrompts.ENTER_DETAIL.format('COMMENT'), RegularExp.STRING_VALUE)
        self.add_review()

    def add_review(self) -> None:
        '''Adding review by customer'''
        review_id = 'R_' + shortuuid.ShortUUID().random(length = 8)
        database_access.non_returning_query(Query.INSERT_REVIEW, (review_id, self.booking_id, self.package_id, self.name, self.comment, self.date), PrintPrompts.ADDED)


def show_review(package_id: str) -> None:
    '''Showing review to customer'''
    comment = database_access.returning_query(Query.SELECT_REVIEW, (package_id, ))
    data_tabulate(comment, (TabulateHeader.NAME, TabulateHeader.COMMENT, TabulateHeader.DATE))


def show_data(customer_id: str) -> None:
    '''Showing their package details to customer'''
    data = database_access.returning_query(Query.SELECT_FOR_REVIEW, (customer_id, 'ongoing', datetime.now().date()))
    if data:
        data_tabulate(data, (TabulateHeader.BOOKING_ID, TabulateHeader.PACKAGE_ID, TabulateHeader.START_DATE, TabulateHeader.END_DATE))
        while True:
            booking_id = tuple(i[0] for i in data)
            enter_booking_id = validate_uuid(InputPrompts.ENTER_DETAIL.format('BOOKING_ID'), RegularExp.UUID)
            if enter_booking_id in booking_id:
                package_id = database_access.single_data_returning_query(Query.SELECT_PACKAGE_REVIEW, (enter_booking_id, ))
                Review(enter_booking_id, package_id[0])
                break
            else:
                print(PrintPrompts.INVALID_BOOKING)
    else:
        print(PrintPrompts.NO_BOOKINGS)
