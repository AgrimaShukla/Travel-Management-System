class DBException(Exception):
    pass

class InvalidUsernameorPassword(DBException):
    pass

class UserAlreadyExists(DBException):
    pass

class IDdoesnotexist(DBException):
    pass

class DataNotFound(DBException):
    pass

class PackageDoesNotExist(DBException):
    pass