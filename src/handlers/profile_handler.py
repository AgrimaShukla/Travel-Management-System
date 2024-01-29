import mysql.connector
from database.database_access import QueryExecutor
from config.queries import Query
from utils.exception import UserAlreadyExists
from config.prompt import PrintPrompts
class ProfileHandler:

    '''Managing customer details'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()

    def get_user_details(self, customer_id) -> None:
        '''showing customer details'''
        customer_details = self.db_access.single_data_returning_query(Query.SELECT_CUSTOMER, customer_id)
        return customer_details 

    def update_details(self, user_data) -> None:
        '''update details of customer'''
        try:
            self.db_access.non_returning_query(Query.UPDATE_CUSTOMER,user_data)
        except mysql.connector.IntegrityError as er:
            raise UserAlreadyExists(PrintPrompts.USER_EXISTS)
    def delete_user(self, customer_id):
        self.db_access.non_returning_query(Query.DELETE_CUSTOMER, customer_id)
 