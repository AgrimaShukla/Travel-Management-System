''' Authenticating the user at the time of login '''
import mysql.connector
import logging
import hashlib
from database.database_access import QueryExecutor
from config.queries import Query
from utils.exception import InvalidUsernameorPassword
from utils.role_mapping import Role
from flask_jwt_extended import create_access_token, create_refresh_token

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
            role = Role.get_role(user_info[2])
            if  user_info[1] == pw:
                access_token = create_access_token(identity=user_info[0], fresh=True, additional_claims={"role": role})
                refresh_token = create_refresh_token(identity=user_info[0], additional_claims={"role": role})
                return {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "message": "User successfully logged in"
                }
            else:
                raise InvalidUsernameorPassword
        else: 
            raise InvalidUsernameorPassword
        # except sqlite3.IntegrityError as error:
        #     logger.exception(error)
        #     raise InvalidUsernameorPassword("User already exists")

               