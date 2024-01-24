''' Authenticating the user at the time of login '''


import hashlib
import logging


from utils import validation

from config.prompt import PrintPrompts, InputPrompts
from config.regex_value import RegularExp
from controller.auth_controller import AuthenticationController

logger = logging.getLogger(__name__)

class Authentication:
    
    ''' class for authenticating user'''
    def __init__(self) -> None:
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
            user_data = self.auth_cont.user_authentication(username)
            if user_data is None:
                self.invalid_username_password()
                continue
            elif user_data[1] == password:
                return user_data
            else:
                self.invalid_username_password()
                continue