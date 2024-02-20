from flask_smorest import abort
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps
from utils.custom_error_response import CustomError
from config.status_code import StatusCodes


def role_based_access(role):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["game"] not in role:
                return CustomError(StatusCodes.FORBIDDEN, "You don't have permission to access this functionality").jsonify_data
            else:
                return func(*args, **kwargs)
        return inner
    return wrapper