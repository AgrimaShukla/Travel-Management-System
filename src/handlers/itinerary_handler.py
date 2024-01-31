from config.queries import Query 
import shortuuid
from database.database_access import QueryExecutor
from utils.exception import DataNotFound, PackageDoesNotExist
from config.prompt import PrintPrompts

class ItineraryHandler:

    def __init__(self):
        self.db_access = QueryExecutor()
    
    def add_itinerary(self, package_id, day, city, desc):
        itinerary_id = "I_" + shortuuid.ShortUUID().random(length = 8)
        package_data = self.db_access.returning_query(Query.CHECK_PACKAGE_QUERY, (package_id, ))
        if package_data:
            data = (itinerary_id, package_id, day, city, desc)
            inserted = self.db_access.non_returning_query(Query.INSERT_ITINERARY_QUERY, data)
            return inserted
        else:
            raise PackageDoesNotExist(PrintPrompts.NO_PACKAGE_FOUND)

    def fetch_itinerary(self):
        data = self.db_access.returning_query(Query.SHOW_ITINERARY_QUERY)
        if data:
            return data
        else:
            raise DataNotFound(PrintPrompts.NO_ITINERARY_FOUND)
        
    def get_particular_itinerary(self, destination: str, category: str, days_night: str) -> None:
        obj_query_executor = QueryExecutor()
        data = (destination, category, days_night, PrintPrompts.ACTIVE)
        itinerary = obj_query_executor.returning_query(Query.SELECT_ITINERARY, data)
        if not itinerary:
            raise DataNotFound
        package_data = obj_query_executor.single_data_returning_query(Query.SELECT_PRICE, data)
        price = {'price': package_data['price']}
        itinerary[0].update(price)
        return itinerary[0]
    
    def check_itinerary(self, itinerary_id: str) -> tuple:
        '''To check existing itineraries'''
        data = self.db_access.single_data_returning_query(Query.CHECK_ITINERARY_QUERY, itinerary_id)
        return data
    
    def update_in_itinerary(self, itinerary_info) -> None:
        '''To update the itineraries'''
        package = self.check_itinerary((itinerary_info[3], ))
        if not package:
            raise DataNotFound(PrintPrompts.NO_ITINERARY_FOUND)
        self.db_access.non_returning_query(Query.UPDATE_ITINERARY_QUERY, itinerary_info)    
        
    