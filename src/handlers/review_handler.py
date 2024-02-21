'''Business for handling customers review of their trip'''

import logging
import shortuuid
from datetime import datetime
from database.database_access import QueryExecutor
from config.queries import Query
import pymysql
from utils.custom_error_response import ApplicationException, DBException
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

class ReviewHandler:
    
    '''Review added by customer for a package'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()


    def add_review(self, review_data, package_id: str) -> None:
        '''Adding review by customer'''
        
        try:
            logger.info(f"{get_request_id()} - Adding new review")
            date = datetime.now().date()
            review_id = 'R_' + shortuuid.ShortUUID().random(length = 8)
            review_tuple = (review_id, review_data["booking_id"], package_id, review_data["name"], review_data["comment"], date)
            self.db_access.non_returning_query(Query.INSERT_REVIEW, review_tuple)
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
      

    def get_reviews(self, package_id: str) -> None:
        '''Showing review to customer'''

        try:
            logger.info(f"{get_request_id()} - Fetching reviews for particular package")
            comment = self.db_access.returning_query(Query.SELECT_REVIEW, (package_id, ))
            if comment:
                return comment
            else:
                logger.error(f"{get_request_id()} - No reviews found")
                raise ApplicationException(StatusCodes.OK, PrintPrompts.NO_REVIEWS, comment)
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)

    def get_bookings_for_review(self, customer_id):
        '''Fetching Booking details for adding a review for them'''

        try:
            logger.info(f"{get_request_id()} - Fetching booking details for adding review for them")
            data = self.db_access.returning_query(Query.SELECT_FOR_REVIEW, (customer_id, PrintPrompts.ACTIVE, datetime.now().date()))
            return data
        except pymysql.Error:
            raise(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
      