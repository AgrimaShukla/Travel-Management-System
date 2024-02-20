'''Business for handling package related operations'''

import logging
from config.queries import Query 
import shortuuid
from database.database_access import QueryExecutor
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
import pymysql
from utils.custom_error_response import ApplicationException, DBException
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

class PackageHandler:
    '''Class for handling package'''

    def __init__(self):
        self.db_access = QueryExecutor()
    
    def add_package(self, package_data):
        '''Method for adding new package'''

        try:
            logger.info(f'{get_request_id()} - Adding new package')
            package_id = 'P_' + shortuuid.ShortUUID().random(length = 8)
            data = (package_id, package_data["package_name"], package_data["duration"], package_data["category"], package_data["price"], package_data["status"])
            self.db_access.non_returning_query(Query.INSERT_PACKAGE_QUERY, data)
            logger.info("Added new package")
            return package_id
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
        
    def fetch_package(self):
        '''Fetching all packages'''

        try:
            logger.info(f"{get_request_id} - Fetching all packages")
            data = self.db_access.returning_query(Query.SELECT_PACKAGE)
            return data
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)  
    
    def check_package(self, package_data: tuple) -> list:
        '''To check package if it exists or not'''

        try:
            logger.info(f"{get_request_id()} - Checking if a package exists or not")
            data = self.db_access.single_data_returning_query(Query.CHECK_PACKAGE_QUERY, package_data) 
            return data
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
    
    def get_price_of_package(self, package_id):
        '''To get price of a package with given package id'''

        try:
            logger.info(f"{get_request_id()} - Getting price of a particular package")
            price = self.db_access.single_data_returning_query(Query.SELECT_PRICE_PACKAGE, package_id)
            return price
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
    
    def change_status_package(self, data) -> None:
        '''Change status of package'''

        try:
            logger.info(f"{get_request_id()} - Changing status of package")
            if_changed = self.db_access.non_returning_query(Query.CHANGE_STATUS_QUERY, data)
            return if_changed
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
    
    def update_in_package(self, package_data, package_id) -> None:
        '''To update the itineraries'''

        try:
            logger.info(f"{get_request_id()} - Updating package with given package id")
            package = self.check_package((package_id, ))
            if not package:
                raise ApplicationException(StatusCodes.NOT_FOUND, PrintPrompts.NO_PACKAGE_FOUND)
            package_tuple = (package_data['package_name'], package_data['duration'], package_data['category'], package_data['price'], package_data['status'], package_id)
            self.db_access.non_returning_query(Query.UPDATE_PACKAGE_QUERY, package_tuple)  
        except pymysql.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)  
        
            