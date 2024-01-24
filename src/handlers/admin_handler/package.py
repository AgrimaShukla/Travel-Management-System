from config.queries import Query 
import shortuuid

from database.database_access import QueryExecutor
from config.regex_value import RegularExp
from config.prompt_values import UPDATE_PACKAGE
from utils.exception import DataNotFound

class PackageHandler:

    def __init__(self):
        self.db_access = QueryExecutor()
    
    def add_package(self, package_name, duration, category, price, status):
        package_id = 'P_' + shortuuid.ShortUUID().random(length = 8)
        data = (package_id, package_name, duration, category, price, status)
        self.db_access.non_returning_query(Query.INSERT_PACKAGE_QUERY, data)

    def fetch_package(self):
        data = self.db_access.returning_query(Query.SELECT_PACKAGE)
        if data:
            return data
        else: 
            raise DataNotFound

    
    def check_package(self, package_data: tuple) -> list:
        '''To check package if it exists or not'''
        data = self.db_access.single_data_returning_query(Query.CHECK_PACKAGE_QUERY, package_data) 
        return data

    def change_status_package(self, data) -> None:
        '''Change status of package'''
        if_changed = self.db_access.non_returning_query(Query.CHANGE_STATUS_QUERY, data)
        return if_changed
    
    def update_in_package(self, package_info) -> None:
        '''To update the itineraries'''
        package = self.check_package((package_info[5], ))
        if not package:
            raise DataNotFound
        self.db_access.non_returning_query(Query.UPDATE_PACKAGE_QUERY, package_info)    
        
            