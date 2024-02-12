import functools
from utils.custom_error_response import ApplicationException, DBException, CustomError
from config.status_code import StatusCodes
from config.prompt import PrintPrompts

def handle_bad_request(_err):
    '''Function to handle bad request'''
    error = CustomError(StatusCodes.BAD_REQUEST, message=PrintPrompts.BAD_REQUEST)
    return error.jsonify_data, error.code


def handle_internal_server_error(_err):
    '''Function to handle server side errors'''
    error = CustomError(StatusCodes.INTERNAL_SERVER_ERROR, message=PrintPrompts.SERVER_ERROR)
    return error.jsonify_data, error.code

def handle_custom_errors(func):
    '''Decorator to handle custom exceptions'''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except ApplicationException as e:
            return e.jsonify_data, e.code
        except DBException as e:
            return e.jsonify_data, e.code
        return res

    return wrapper