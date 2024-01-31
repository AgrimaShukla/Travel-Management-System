from flask_smorest import abort
from flask_jwt_extended import verify_jwt_in_request, get_jwt


def role_based_access(role):
    def wrapper(func):
        def inner(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["role"] not in role:
                abort(401, message = "You don't have permission to access this functionality")
            else:
                return func(*args, **kwargs)
        return inner
    return wrapper