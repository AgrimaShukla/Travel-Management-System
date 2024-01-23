''' This module is for registering user'''

import logging
import maskpass
from utils.validation import validate, validate_password
from config.regex_value import RegularExp
import hashlib
from config.prompt import PrintPrompts, InputPrompts, LoggingPrompt
from controller.registration_controller import Registration
logger = logging.getLogger(__name__)

class RegistrationViews:
    '''Registering the customer'''
    def __init__(self) -> None:
        self.register = Registration()

    def enter_customer_details(self) -> None:
        '''Saving the customer'''   
        username = validate(RegularExp.USERNAME, InputPrompts.INPUT.format("username"))
        password = validate_password(RegularExp.PASSWORD).encode()
        password = hashlib.md5(password).hexdigest()
        name = validate(RegularExp.NAME, InputPrompts.INPUT.format("name"))
        mobile_no = validate(RegularExp.MOBILE_NUMBER, InputPrompts.INPUT.format("mobile no"))
        gender = validate(RegularExp.GENDER, InputPrompts.GENDER)
        age = validate(RegularExp.AGE, InputPrompts.INPUT.format("age"))
        # age = int(input("Enter age: "))
        email = validate(RegularExp.EMAIL, InputPrompts.EMAIL)
        if_registered = self.register.save_customer(username, password, name, mobile_no, gender, age, email)
        if if_registered == True:
            print(PrintPrompts.SUCCESFULLY)
            logger.info(LoggingPrompt.REGISTERED)
        else:
            print(PrintPrompts.UNEXPECTED_ISSUE)
