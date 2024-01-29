'''This module is for customers review of their experience'''
import shortuuid
from datetime import datetime
from database.database_access import QueryExecutor
from config.queries import Query
from utils.exception import DataNotFound
from config.prompt import PrintPrompts

class ReviewHandler:
    '''Review added by customer for a package'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()


    def add_review(self, name, comment, booking_id: str, package_id: str) -> None:
        '''Adding review by customer'''
        
        date = datetime.now().date()
        review_id = 'R_' + shortuuid.ShortUUID().random(length = 8)
        self.db_access.non_returning_query(Query.INSERT_REVIEW, (review_id, booking_id, package_id, name, comment, date))
      

    def get_reviews(self, package_id: str) -> None:
        '''Showing review to customer'''
        comment = self.db_access.returning_query(Query.SELECT_REVIEW, (package_id, ))
        if comment:
            return comment
        else:
            raise DataNotFound(PrintPrompts.NO_REVIEWS)

    def get_bookings_for_review(self, customer_id):
        data = self.db_access.returning_query(Query.SELECT_FOR_REVIEW, (customer_id, 'ongoing', datetime.now().date()))
        return data
    
    
    