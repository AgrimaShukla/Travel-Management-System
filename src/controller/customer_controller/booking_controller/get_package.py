'''This module is to show packages on the basis of options selected by user to further book the package'''

from database.database_access import QueryExecutor
from config.queries import Query 
from utils.exception import exception_handler

@exception_handler
def get_package(destination: str, category: str, days_night: str) -> None:
        '''To view the package after user preferences'''
        print('hey')
        obj_query_executor = QueryExecutor()
        data = (destination[0], category[0], days_night[0], 'active')
        print(data)
        itinerary = obj_query_executor.returning_query(Query.SELECT_ITINERARY, data)
        package_data = obj_query_executor.single_data_returning_query(Query.SELECT_PRICE, data)
        return itinerary, package_data
       