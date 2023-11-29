''' Authenticating the user at the time of login '''

import time
import hashlib
import logging

from database.database_access import QueryExecutor
from utils import validation
from config.queries import Query 
from config.prompt import PrintPrompts, InputPrompts
from config.regex_value import RegularExp

logger = logging.getLogger(__name__)

class Authentication:
    
    ''' class for authenticating user'''
    def __init__(self) -> None:
        # no of attempts given to user
        self.attempts = 3
        self.db_access = QueryExecutor()
    

    def invalid_username_password(self) -> None:
        '''To log and print invalid attempt to login'''
        logging.error("Invalid login attempt")
        print(PrintPrompts.INVALID_CREDENTIALS)
        self.attempts = self.attempts - 1
    

    def user_authentication(self) -> tuple:
        '''Function to authenticate use'''
        while self.attempts > 0: 
            username = validation.validate(InputPrompts.INPUT.format("username"), RegularExp.USERNAME)
            password = validation.validate_password(RegularExp.PASSWORD).encode()
            password = hashlib.md5(password).hexdigest()
            data = (username, )
            user_data = self.db_access.single_data_returning_query(Query.SELECT_CREDENTIALS_USERNAME, data)
    
            # to check if username matches
            if user_data is None:
                self.invalid_username_password()
                continue

            # to check if password matches
            elif user_data[0] == password:
                data = (username, password)
                role = self.db_access.single_data_returning_query(Query.SELECT_CREDENTIALS_PASSWORD, data)
                return role
            else:
                self.invalid_username_password()
                continue

        print("Attempts exhausted")
        time.sleep(3)      
               