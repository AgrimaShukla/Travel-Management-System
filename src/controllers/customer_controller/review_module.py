'''This module is for customers review of their experience'''
import shortuuid
from datetime import datetime
from database.database_access import QueryExecutor
from config.queries import Query
from utils.validation import validate, validate_uuid
from utils.pretty_print import data_tabulate
from config.prompt import InputPrompts, PrintPrompts, TabulateHeader
from config.regex_value import RegularExp

class Review:
    '''Review added by customer for a package'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()


    def add_review(self, booking_id: str, package_id: str) -> None:
        '''Adding review by customer'''
        name = validate(InputPrompts.ENTER_DETAIL.format('NAME'), RegularExp.NAME)
        date = datetime.now().date()
        comment = validate(InputPrompts.ENTER_DETAIL.format('COMMENT'), RegularExp.STRING_VALUE)
        review_id = 'R_' + shortuuid.ShortUUID().random(length = 8)
        self.db_access.non_returning_query(Query.INSERT_REVIEW, (review_id, booking_id, package_id, name, comment, date), PrintPrompts.ADDED)


    def show_review(self, package_id: str) -> None:
        '''Showing review to customer'''
        comment = self.db_access.returning_query(Query.SELECT_REVIEW, (package_id, ))
        data_tabulate(comment, (TabulateHeader.NAME, TabulateHeader.COMMENT, TabulateHeader.DATE))


    def show_data(self, customer_id: str) -> None:
        '''Showing their package details to customer'''
        data = self.db_access.returning_query(Query.SELECT_FOR_REVIEW, (customer_id, 'ongoing', datetime.now().date()))
        if data:
            data_tabulate(data, (TabulateHeader.BOOKING_ID, TabulateHeader.PACKAGE_ID, TabulateHeader.START_DATE, TabulateHeader.END_DATE))
            while True:
                booking_id = tuple(i[0] for i in data)
                enter_booking_id = validate_uuid(InputPrompts.ENTER_DETAIL.format('BOOKING_ID'), RegularExp.UUID)
                if enter_booking_id in booking_id:
                    package_id = self.db_access.single_data_returning_query(Query.SELECT_PACKAGE_REVIEW, (enter_booking_id, ))
                    self.add_review(enter_booking_id, package_id[0])
                    break
                else:
                    print(PrintPrompts.INVALID_BOOKING)
        else:
            print(PrintPrompts.NO_BOOKINGS)
