''' This module is for registering user'''


import logging
import shortuuid
import hashlib
import mysql.connector
from config.queries import Query
from database.database_access import QueryExecutor
from utils.exception import UserAlreadyExists
logger = logging.getLogger(__name__)

class RegistrationHandler:
    '''Registering the customer'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()

    def save_customer(self, username, password, name, mobile_no, gender, age, email) -> None:
        '''Saving the customer''' 
        try: 
            user_id = "U" + shortuuid.ShortUUID().random(length = 10)
            password =  hashlib.md5(password.encode()).hexdigest()
            customer_credentials = (user_id, username, password, 'user')
            customer_data = (user_id, name, mobile_no, gender, age, email)
            self.db_access.insert_table(Query.INSERT_CREDENTIALS, customer_credentials, Query.INSERT_USER, customer_data)
            
        except mysql.connector.IntegrityError as err:
            logger.exception(err)
            raise UserAlreadyExists
