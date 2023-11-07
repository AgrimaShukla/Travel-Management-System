''' This module deals with all input validation for the user'''
import re
import logging
import maskpass

logger = logging.getLogger(__name__)

def error_handling(func):
    '''Decorator for handling errors'''
    def wrapper(*args, **kwargs):
        try: 
            matched = func(*args, **kwargs)
            if matched == False:
                raise Exception
        except:
            logger.exception("not validated")
            print("Wrong input! Enter again.")
        finally:
            return matched
    return wrapper
        

@error_handling
def input_validation(regex_exp, value) -> bool:
    '''matching regex with value'''
    matched = re.fullmatch(regex_exp, value)
    if matched != None:
        return True
    return False

def validate(prompts, regular_exp):
    '''taking input and pass to input validation'''
    while True:
        value = input(prompts).lower()
        check = input_validation(regular_exp, value)
        if check == True:
            return value
        
def validate_password(regex_exp) -> str:
    '''validating password should be minimum of length'''
    while True:
        password = maskpass.advpass()
        check = input_validation(regex_exp, password)
        if check == True:
            return password