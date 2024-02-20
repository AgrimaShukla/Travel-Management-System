''' Authenticating the user at the time of login '''

import logging
import hashlib
from database.database_access import QueryExecutor
from config.queries import Query
from utils.custom_error_response import ApplicationException, DBException
from config.prompt import PrintPrompts
from utils.token import Token
import pymysql
from utils.logging_request_id import get_request_id
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

class LoginHandler:
    
    ''' class for authenticating user'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()
        self.token_obj = Token()
    
    def user_authentication(self, user_data) -> tuple:
        '''Function to authenticate user'''
        try:
            logger.debug(f"{get_request_id()} - User is trying to login with username {user_data['username']}")
            user_info = self.db_access.single_data_returning_query(Query.SELECT_CREDENTIALS_USERNAME, (user_data["username"],))
            if user_info:
                pw = hashlib.md5(user_data["password"].encode()).hexdigest()
                if user_info['password'] == pw:
                    access_token, refresh_token = self.token_obj.generate_token(user_info["role"], user_info["user_id"], True)
                    return access_token, refresh_token
                else:
                    logger.error(f'{get_request_id()} - Invalid attempt to login with username {user_data["username"]}')
                    raise ApplicationException(StatusCodes.UNAUTHORIZED, PrintPrompts.INVALID_CREDENTIALS)
            else:
                logger.error(f"{get_request_id()} - Username does not exist {user_data['username']}") 
                raise ApplicationException(StatusCodes.UNAUTHORIZED, PrintPrompts.INVALID_CREDENTIALS)
        except pymysql.Error as e:
            print(e)
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
       
               