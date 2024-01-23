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


    def add_review(self, name, comment, booking_id: str, package_id: str) -> None:
        '''Adding review by customer'''
        
        date = datetime.now().date()
        review_id = 'R_' + shortuuid.ShortUUID().random(length = 8)
        added = self.db_access.non_returning_query(Query.INSERT_REVIEW, (review_id, booking_id, package_id, name, comment, date))
        return added


    def get_reviews(self, package_id: str) -> None:
        '''Showing review to customer'''
        comment = self.db_access.returning_query(Query.SELECT_REVIEW, (package_id, ))
        # data_tabulate(comment, (TabulateHeader.NAME, TabulateHeader.COMMENT, TabulateHeader.DATE))
        return comment

    def get_bookings(self, customer_id):
        data = self.db_access.returning_query(Query.SELECT_FOR_REVIEW, (customer_id, 'ongoing', datetime.now().date()))
        return data
    
    def get_package_id(self, booking_id):
        package_id = self.db_access.single_data_returning_query(Query.SELECT_PACKAGE_REVIEW, (booking_id, ))
        return package_id
