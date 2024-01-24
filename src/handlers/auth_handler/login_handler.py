''' Authenticating the user at the time of login '''
import mysql.connector
import logging
import hashlib
from database.database_access import QueryExecutor
from config.queries import Query
from utils.exception import InvalidUsernameorPassword

logger = logging.getLogger(__name__)

class LoginHandler:
    
    ''' class for authenticating user'''
    def __init__(self) -> None:
        # no of attempts given to user
        self.db_access = QueryExecutor()
    
    def user_authentication(self, user_data) -> tuple:
        '''Function to authenticate use'''
        
        user_info = self.db_access.single_data_returning_query(Query.SELECT_CREDENTIALS_USERNAME, (user_data["username"],))
        
        if user_info:
            pw = hashlib.md5(user_data["password"].encode()).hexdigest()
            if  user_info['password'] == pw:
                return user_info
            else:
                raise InvalidUsernameorPassword
        else: 
            raise InvalidUsernameorPassword
       
               