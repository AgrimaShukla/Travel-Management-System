''' This module is for registering user'''

import hashlib
import logging
import shortuuid

from src.config.queries import Query
from src.utils import validation
from src.config.prompt import PrintPrompts, InputPrompts, LoggingPrompt
from src.config.regex_value import RegularExp
from src.database.database_access import insert_table

logger = logging.getLogger(__name__)

class Registration:
    '''Registering the customer'''
    def __init__(self) -> None:
        while True:
            self.username = validation.validate(InputPrompts.INPUT.format("username"), RegularExp.USERNAME)
            print(PrintPrompts.PASSWORD)
            self.password = validation.validate_password(RegularExp.PASSWORD).encode()
            self.password = hashlib.md5(self.password).hexdigest()
            self.user_id = "U" + shortuuid.ShortUUID().random(length = 10)
            self.name = validation.validate(InputPrompts.INPUT.format("name"), RegularExp.NAME)
            self.mobile_no = validation.validate(InputPrompts.INPUT.format("mobile no"), RegularExp.MOBILE_NUMBER)
            self.gender = validation.validate(InputPrompts.GENDER, RegularExp.GENDER)
            self.age = validation.validate(InputPrompts.INPUT.format("age"), RegularExp.AGE)
            self.email = validation.validate(InputPrompts.EMAIL, RegularExp.EMAIL)
            self.save_customer()
            break

    def save_customer(self) -> None:
        '''Saving the customer'''
        insert_customer_query = Query.INSERT_CUSTOMER
        insert_credentials_query = Query.INSERT_CREDENTIALS
        customer_credentials = (self.user_id, self.username, self.password, 'user')
        customer_data = (self.user_id, self.name, self.mobile_no, self.gender, self.age, self.email)
        value = insert_table(insert_credentials_query, customer_credentials, insert_customer_query, customer_data)
        if value == True:
            print(PrintPrompts.SUCCESFULLY)
            logger.info(LoggingPrompt.REGISTERED)
