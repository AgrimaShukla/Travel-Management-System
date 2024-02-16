from flask import request

def get_request_id():
    return request.environ.get("X-Request-Id")