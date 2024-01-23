''' This module is for registering user'''

import shortuuid

from config.queries import Query
from database.database_access import QueryExecutor
from utils.exception import exception_handler

class Registration:
    '''Registering the customer'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()

    @exception_handler
    def save_customer(self, username, password, name, mobile_no, gender, age, email) -> None:
        '''Saving the customer'''  
        user_id = "U" + shortuuid.ShortUUID().random(length = 10)

        customer_credentials = (user_id, username, password, 'user')
        customer_data = (user_id, name, mobile_no, gender, age, email)
        value = self.db_access.insert_table(Query.INSERT_CREDENTIALS, customer_credentials, Query.INSERT_CUSTOMER, customer_data)
        return value
