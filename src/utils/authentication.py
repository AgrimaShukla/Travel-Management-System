''' Authenticating the user at the time of login '''

import time
import hashlib
import logging
import maskpass

from src.database.database_access import single_data_returning_query
from src.config.prompt import PrintPrompts
from src.config.queries import Query 

logger = logging.getLogger(__name__)

class Authentication:
    
    ''' class for authenticating user'''
    def __init__(self) -> None:
        # no of attempts given to user
        self.attempts = 3
    

    def invalid_username_password(self) -> None:
        '''To log and print invalid attempt to login'''
        logging.error("Invalid login attempt")
        print(PrintPrompts.INVALID_CREDENTIALS)
        self.attempts = self.attempts - 1
    

    def user_authentication(self) -> tuple:
        '''Function to authenticate use'''
        while self.attempts > 0: 
            username = input("Enter your username: ")
            password = maskpass.advpass().encode()
            password = hashlib.md5(password).hexdigest()
            data = (username, )
            user_data = single_data_returning_query(Query.SELECT_CREDENTIALS_USERNAME, data)

            # to check if username matches
            if user_data is None:
                self.invalid_username_password()
                continue

            # to check if password matches
            elif user_data[0] == password:
                data = (username, password)
                role = single_data_returning_query(Query.SELECT_CREDENTIALS_PASSWORD, data)
                return role
            else:
                self.invalid_username_password()
                continue

        print("Attempts exhausted")
        time.sleep(3)      
               