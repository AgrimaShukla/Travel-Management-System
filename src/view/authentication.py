''' Authenticating the user at the time of login '''

import time
import hashlib
import logging
import maskpass

from utils import validation

from config.prompt import PrintPrompts, InputPrompts
from config.regex_value import RegularExp
from controller.auth_controller import AuthenticationController

logger = logging.getLogger(__name__)

class Authentication:
    
    ''' class for authenticating user'''
    def __init__(self) -> None:
        # no of attempts given to user
        self.attempts = 3
        self.auth_cont = AuthenticationController()
    

    def invalid_username_password(self) -> None:
        '''To log and print invalid attempt to login'''
        logging.error("Invalid login attempt")
        print(PrintPrompts.INVALID_CREDENTIALS)
    

    def user_authentication(self) -> tuple:
        '''Function to authenticate use'''
        while True:
            username = validation.validate(RegularExp.USERNAME, InputPrompts.INPUT.format("username"))
            password = validation.validate_password(RegularExp.PASSWORD).encode()
            password = hashlib.md5(password).hexdigest()
            # data = (username, )
            user_data = self.auth_cont.user_authentication(username)
            # user_data = self.db_access.single_data_returning_query(Query.SELECT_CREDENTIALS_USERNAME, data)

            # to check if username matches
            if user_data is None:
                self.invalid_username_password()
                continue

            # to check if password matches
            elif user_data[0] == password:
                data = (username, password)
                role = self.auth_cont.get_role(data)
                return role
            else:
                self.invalid_username_password()
                continue
