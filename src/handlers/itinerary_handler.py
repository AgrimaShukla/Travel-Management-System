'''Business for handling Itineraries operation'''

import logging
from config.queries import Query 
import shortuuid
from database.database_access import QueryExecutor
from mysql import connector
from utils.custom_error_response import ApplicationException, DBException
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

class ItineraryHandler:
    '''Class for handling Itinerary operations'''
    def __init__(self):
        self.db_access = QueryExecutor()
    
    def add_itinerary(self, itinerary_data, package_id):
        '''Method for adding new itinerary'''

        try:
            logger.info(f'{get_request_id()} - Adding itinerary')
            itinerary_id = "I_" + shortuuid.ShortUUID().random(length = 8)
            package_data = self.db_access.returning_query(Query.CHECK_PACKAGE_QUERY, (package_id, ))
            if package_data:
                data = (itinerary_id, itinerary_data["package_id"], itinerary_data["day"], itinerary_data["city"], itinerary_data["description"])
                inserted = self.db_access.non_returning_query(Query.INSERT_ITINERARY_QUERY, data)
                return inserted
            else:
                logger.error(f'{get_request_id()} - Package does not exist')
                raise ApplicationException(StatusCodes.NOT_FOUND,PrintPrompts.NO_PACKAGE_FOUND)
        except connector.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)

    def fetch_itinerary(self):
        '''Method for fetching all itineraries'''

        try:
            logger.info(f'{get_request_id()} - fetching itinerary')
            data = self.db_access.returning_query(Query.SHOW_ITINERARY_QUERY)
            return data
        except connector.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
       
        
    def get_particular_itinerary(self, destination: str, category: str, days_night: str) -> None:
        '''Method for fetching one itinerary based on given information'''

        try:
            logger.info(f'{get_request_id()} - Fetching a particular itinerary')
            obj_query_executor = QueryExecutor()
            data = (destination, category, days_night, PrintPrompts.ACTIVE)
            itinerary = obj_query_executor.returning_query(Query.SELECT_ITINERARY, data)
            if not itinerary:
                logger.error(f"{get_request_id()} - No itinerary found")
                raise ApplicationException(StatusCodes.NOT_FOUND, PrintPrompts.NO_ITINERARY_FOUND)
            package_data = obj_query_executor.single_data_returning_query(Query.SELECT_PRICE, data)
            price = {'price': package_data['price']}
            itinerary[0].update(price)
            return itinerary[0]
        except connector.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
    
    def check_itinerary(self, itinerary_id: str) -> tuple:
        '''To check if itinerary exists with given id'''

        try:
            logger.info(f"{get_request_id()} - Checking if itinerary exist for id {itinerary_id}")
            data = self.db_access.single_data_returning_query(Query.CHECK_ITINERARY_QUERY, itinerary_id)
            return data
        except connector.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
    
    def update_in_itinerary(self, itinerary_data, itinerary_id) -> None:
        '''To update an itinerary with given id'''

        try:
            logger.info(f"{get_request_id()} - Updating itinerary for given itinerary id")
            itinerary = self.check_itinerary((itinerary_id, ))
            if not itinerary:
                logger.error("No itinerary found with given itinerary id")
                raise ApplicationException(StatusCodes.NOT_FOUND, PrintPrompts.NO_ITINERARY_FOUND)
            itinerary_tuple = (itinerary_data['day'], itinerary_data['city'], itinerary_data['description'], itinerary_id)
            self.db_access.non_returning_query(Query.UPDATE_ITINERARY_QUERY, itinerary_tuple)    
            logger.info(f"{get_request_id()} - Updated itinerary")
        except connector.Error:
            raise DBException(StatusCodes.INTERNAL_SERVER_ERROR, PrintPrompts.INTERNAL_SERVER_ERROR)
