''' Authenticating the user at the time of login '''

import logging
import hashlib
from database.database_access import QueryExecutor
from config.queries import Query
from utils.exception import InvalidUsernameorPassword
from config.prompt import PrintPrompts
from flask_jwt_extended import create_access_token, create_refresh_token
from utils.role_mapping import Role

logger = logging.getLogger(__name__)

class LoginHandler:
    
    ''' class for authenticating user'''
    def __init__(self) -> None:
        # no of attempts given to user
        self.db_access = QueryExecutor()
    
    def user_authentication(self, user_data) -> tuple:
        '''Function to authenticate use'''
        
        user_info = self.db_access.single_data_returning_query(Query.SELECT_CREDENTIALS_USERNAME, (user_data["username"],))
        role = Role.get_role(user_info['role'])
        access_token = create_access_token(identity=user_info['user_id'], fresh=True, additional_claims={"role": role})
        refresh_token = create_refresh_token(identity=user_info['user_id'], additional_claims={"role": role})
        if user_info:
            pw = hashlib.md5(user_data["password"].encode()).hexdigest()
            if  user_info['password'] == pw:
                return access_token, refresh_token
            else:
                raise InvalidUsernameorPassword(PrintPrompts.INVALID_CREDENTIALS)
        else: 
            raise InvalidUsernameorPassword(PrintPrompts.INVALID_CREDENTIALS)
       
               