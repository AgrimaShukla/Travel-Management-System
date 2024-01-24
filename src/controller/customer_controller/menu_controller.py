from database.database_access import QueryExecutor
from config.queries import Query
from utils.exception import exception_handler

class MenuController:
    '''For fetching package details for customer'''

    def __init__(self) -> None:
        self.db_access = QueryExecutor()

    @exception_handler
    def get_package_name(self):
        '''Getting all types of package'''
        value = self.db_access.returning_query(Query.SELECT_PACKAGE_NAME)
        return value
    
    @exception_handler
    def get_duration(self):
        '''Getting all values for duration in package'''
        value = self.db_access.returning_query(Query.SELECT_DURATION)
        return value
    
    @exception_handler
    def get_category(self):
        '''Getting all types of category in package'''
        value = self.db_access.returning_query(Query.SELECT_CATEGORY)
        return value