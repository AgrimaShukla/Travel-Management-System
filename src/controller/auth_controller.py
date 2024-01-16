''' Authenticating the user at the time of login '''

import time
import hashlib
import logging
from database.database_access import QueryExecutor
from utils.validation import validate, validate_password

from config.queries import Query
from config.prompt import InputPrompts
from config.regex_value import RegularExp

logger = logging.getLogger(__name__)

class AuthenticationController:
    
    ''' class for authenticating user'''
    def __init__(self) -> None:
        # no of attempts given to user
        self.db_access = QueryExecutor()
    
    def user_authentication(self, username) -> tuple:
        '''Function to authenticate use'''
        data = (username, )
        user_data = self.db_access.single_data_returning_query(Query.SELECT_CREDENTIALS_USERNAME, data)
        return user_data
        # to check if username matches

    def get_role(self, data):
        role = self.db_access.single_data_returning_query(Query.SELECT_CREDENTIALS_PASSWORD, data)  
        return role 
               