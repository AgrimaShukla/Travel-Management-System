''' This module is for registering user'''

import logging
import shortuuid
import hashlib
import pymysql
from config.queries import Query
from database.database_access import QueryExecutor
from utils.custom_error_response import ApplicationException, DBException
from config.status_code import StatusCodes
from utils.logging_request_id import get_request_id
from config.prompt import PrintPrompts

logger = logging.getLogger(__name__)

class RegistrationHandler:
    '''Registering the customer'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()

    def save_customer(self, username, password, name, mobile_no, gender, age, email) -> None:
        '''Saving the customer''' 
        try: 
            logger.info(f"{get_request_id()} - saving new customer")
            user_id = "U" + shortuuid.ShortUUID().random(length = 10)
            password =  hashlib.md5(password.encode()).hexdigest()
            customer_credentials = (user_id, username, password, 'user')
            customer_data = (user_id, name, mobile_no, gender, age, email)
            self.db_access.insert_table(Query.INSERT_CREDENTIALS, customer_credentials, Query.INSERT_USER, customer_data)
            return user_id
        
        except pymysql.IntegrityError as err:
            logger.error(get_request_id(), err)
            raise ApplicationException(StatusCodes.CONFLICT, PrintPrompts.USER_EXISTS)
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)