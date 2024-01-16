''' This module is for registering user'''


import logging
import shortuuid

from config.queries import Query
from database.database_access import QueryExecutor

logger = logging.getLogger(__name__)

class Registration:
    '''Registering the customer'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()

    def save_customer(self, username, password, name, mobile_no, gender, age, email) -> None:
        '''Saving the customer'''  
        user_id = "U" + shortuuid.ShortUUID().random(length = 10)

        customer_credentials = (user_id, username, password, 'user')
        customer_data = (user_id, name, mobile_no, gender, age, email)
        value = self.db_access.insert_table(Query.INSERT_CREDENTIALS, customer_credentials, Query.INSERT_CUSTOMER, customer_data)
        return value
