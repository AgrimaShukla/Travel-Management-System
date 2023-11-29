''' This module is for registering user'''

import hashlib
import logging
import shortuuid

from config.queries import Query
from utils import validation
from config.prompt import PrintPrompts, InputPrompts, LoggingPrompt
from config.regex_value import RegularExp
from database.database_access import QueryExecutor

logger = logging.getLogger(__name__)

class Registration:
    '''Registering the customer'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()


    def save_customer(self) -> None:
        '''Saving the customer'''   
        username = validation.validate(InputPrompts.INPUT.format("username"), RegularExp.USERNAME)
        print(PrintPrompts.PASSWORD)
        password = validation.validate_password(RegularExp.PASSWORD).encode()
        password = hashlib.md5(password).hexdigest()
        user_id = "U" + shortuuid.ShortUUID().random(length = 10)
        name = validation.validate(InputPrompts.INPUT.format("name"), RegularExp.NAME)
        mobile_no = validation.validate(InputPrompts.INPUT.format("mobile no"), RegularExp.MOBILE_NUMBER)
        gender = validation.validate(InputPrompts.GENDER, RegularExp.GENDER)
        age = validation.validate(InputPrompts.INPUT.format("age"), RegularExp.AGE)
        email = validation.validate(InputPrompts.EMAIL, RegularExp.EMAIL)

        insert_customer_query = Query.INSERT_CUSTOMER
        insert_credentials_query = Query.INSERT_CREDENTIALS
        customer_credentials = (user_id, username, password, 'user')
        customer_data = (user_id, name, mobile_no, gender, age, email)
        value = self.db_access.insert_table(insert_credentials_query, customer_credentials, insert_customer_query, customer_data)
        if value == True:
            print(PrintPrompts.SUCCESFULLY)
            logger.info(LoggingPrompt.REGISTERED)
