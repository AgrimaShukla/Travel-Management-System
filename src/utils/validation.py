''' This module deals with all input validation for the user'''
import re
import logging
import maskpass

from datetime import datetime
from config.prompt import PrintPrompts, InputPrompts
from utils.custom_response import CustomError
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

def error_handling(func):
    '''Decorator for handling errors'''
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if value == True:
            return value
        else: 
            logger.exception("not validated")
            print("Wrong input! Enter again.")
    return wrapper

@error_handling
def input_validation(regex_exp: str, value: str) -> bool:
    '''matching regex with value'''
    result = re.fullmatch(regex_exp, value)
    if result != None:
        return True
    return False

def validate(regular_exp: str, prompts: str) -> str:
    '''taking input and passing to input validation'''
    while True:
        value = input(prompts).lower()
        result = input_validation(regular_exp, value)
        if result == True:
            return value

def validate_password(regex_exp: str) -> str:
    '''validating password should be minimum of length'''
    while True:
        password = maskpass.askpass()
        result = input_validation(regex_exp, password)
        if result == True:
            return password

def validate_uuid(prompts: str, regex_exp: str) -> str:
    '''validating unique id'''
    while True:
        uuid = input(prompts)
        result = input_validation(regex_exp, uuid)
        if result == True:
            return uuid

def validate_date(date_str) -> None:
    '''Checking date if valid or not'''
    
    try:
        start_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        print(type(start_date))
        if start_date > datetime.now().date():
            return start_date
        elif start_date <= datetime.now().date():
            return CustomError(StatusCodes.UNPROCESSABLE_CONTENT, PrintPrompts.INVALID_DATE)
        else: 
            return CustomError(StatusCodes.UNPROCESSABLE_CONTENT, PrintPrompts.INVALID_DATE_FORMAT)
    except ValueError:
        return CustomError(StatusCodes.UNPROCESSABLE_CONTENT, PrintPrompts.INVALID_DATE)

                      