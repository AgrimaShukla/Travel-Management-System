'''Business for handling User related operations'''

import logging
import mysql.connector
from database.database_access import QueryExecutor
from config.queries import Query
from mysql import connector
from utils.custom_error_response import ApplicationException, DBException
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

class ProfileHandler:
    '''Class for managing customer details'''

    def __init__(self) -> None:
        self.db_access = QueryExecutor()

    def get_user_details(self, customer_id) -> None:
        '''showing customer details'''

        try:
            logger.info(f"{get_request_id()} Getting user details")
            customer_details = self.db_access.single_data_returning_query(Query.SELECT_CUSTOMER, customer_id)
            return customer_details 
        except connector.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)

    def update_details(self, user_data) -> None:
        '''update details of customer'''

        logger.info(f"{get_request_id()} - Updating user details")
        try:
            self.db_access.non_returning_query(Query.UPDATE_CUSTOMER,user_data)
        except mysql.connector.IntegrityError:
            logger.error(f"{get_request_id()} - User already exists")
            raise ApplicationException(StatusCodes.UNAUTHORIZED, PrintPrompts.USER_EXISTS)
        except connector.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
        
    def delete_user(self, customer_id):
        '''Deleting a particular user'''
        try:
            logger.info(f"{get_request_id()} - Deleting user account")
            self.db_access.non_returning_query(Query.DELETE_CUSTOMER, customer_id)
        except connector.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
 