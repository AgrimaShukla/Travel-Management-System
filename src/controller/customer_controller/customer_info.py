from database.database_access import QueryExecutor
from config.queries import Query
from utils.exception import exception_handler

class CustomerInfoController:
    '''Managing customer details'''

    def __init__(self, customer_id: str) -> None:
        self.customer_id = customer_id
        self.db_access = QueryExecutor()

    @exception_handler
    def display_details(self) -> None:
        '''showing customer details'''
        customer_details = self.db_access.single_data_returning_query(Query.SELECT_CUSTOMER, (self.customer_id, ))
        return customer_details 

    @exception_handler
    def update_details(self, value, column, entered_value) -> None:
        '''update details of customer'''
        result = self.db_access.non_returning_query(Query.UPDATE_CUSTOMER.format(column), (entered_value, self.customer_id))
        return result