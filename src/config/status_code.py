from collections import namedtuple


INFO = namedtuple('StatusCodes', 'code status')
class StatusCodes:
    'Contains all the status codes and messages'

    OK =INFO(code=200, status='OK')
    CREATED=INFO(code=201, status='CREATED')
    BAD_REQUEST=INFO(code=400, status='BAD REQUEST')
    UNAUTHORIZED=INFO(code=401, status='UNAUTHORIZED')
    FORBIDDEN=INFO(code=403, status='FORBIDDEN')
    NOT_FOUND=INFO(code=404, status='NOT FOUND')
    CONFLICT=INFO(code=409, status='CONFLICT')
    UNPROCESSABLE_CONTENT=INFO(code=422, status='UNPROCESSABLE CONTENT')
    INTERNAL_SERVER_ERROR=INFO(code=500, status='INTERNAL SERVER ERROR')