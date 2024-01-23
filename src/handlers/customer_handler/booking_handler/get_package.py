'''This module is to show packages on the basis of options selected by user to further book the package'''

from config.prompt_values import DESTINATION_DICT, CATEGORY_DICT, DAY_DICT
from database.database_access import QueryExecutor
from config.queries import Query 

def get_package(destination: str, category: str, days_night: str) -> None:
        '''To view the package after user preferences'''

        dest_value = DESTINATION_DICT[destination]
        category_value = CATEGORY_DICT[category]
        day_value = DAY_DICT[days_night]
        
        obj_query_executor = QueryExecutor()
        data = (dest_value, category_value, day_value, 'active')
        itinerary = obj_query_executor.returning_query(Query.SELECT_ITINERARY, data)
        package_data = obj_query_executor.single_data_returning_query(Query.SELECT_PRICE, data)
        return itinerary, package_data
        # data_tabulate(itinerary, (TabulateHeader.DAY, TabulateHeader.CITY, TabulateHeader.DESC))
 