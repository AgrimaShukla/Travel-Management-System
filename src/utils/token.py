import logging
from database.database_access import QueryExecutor
from flask_jwt_extended import create_access_token, create_refresh_token, get_jti
from config.queries import Query
from utils.role_mapping import Role
logger = logging.getLogger(__name__)

class Token:
    '''Class containing methods of token related functionalities'''

    def __init__(self):
        self.db_object = QueryExecutor()

    def check_token_revoked(self, jwt_payload) -> bool:
        '''Method to check if token is revoked'''

        logger.info('Checking if token is revoked or not')

        jti_access_token = jwt_payload["jti"]

        result = self.db_object.single_data_returning_query(Query.SELECT_TOKEN_IF_REVOKED,(jti_access_token,))
        if result[0]['token_status'] == "revoked":
            return True
        return False

    def revoke_token(self, jwt_payload)-> None:
        '''Method to revoke a token'''
        logger.info("Revoking token")

        jti_access_token = jwt_payload["jti"]

        self.db_object.non_returning_query(Query.UPDATE_TOKEN_STATUS,('revoked',jti_access_token,))

    def generate_token(self,role: str,user_id: str, fresh_value) -> tuple :
        '''Method to generate new access and refresh token and saving token in database'''
        logger.info('New access and refresh token issued')
        role_value = Role.get_role(role)
        access_token = create_access_token(identity=user_id, fresh = fresh_value, additional_claims={"game": role_value})
        access_jti = get_jti(access_token)
        refresh_token = create_refresh_token(identity=user_id, additional_claims={"game": role_value})
        refresh_jti = get_jti(refresh_token)
        self.db_object.non_returning_query(Query.INSERT_TOKEN, (user_id, access_jti, refresh_jti))
        return access_token, refresh_token