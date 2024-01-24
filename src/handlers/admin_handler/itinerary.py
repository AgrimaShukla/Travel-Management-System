from config.queries import Query 
import shortuuid
from database.database_access import QueryExecutor
from utils.exception import DataNotFound, PackageDoesNotExist

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
            raise PackageDoesNotExist

    def fetch_itinerary(self):
        data = self.db_access.returning_query(Query.SHOW_ITINERARY_QUERY)
        if data:
            return data
        else:
            raise DataNotFound

    def check_itinerary(self, itinerary_id: str) -> tuple:
        '''To check existing itineraries'''
        data = self.db_access.single_data_returning_query(Query.CHECK_ITINERARY_QUERY, itinerary_id)
        return data
    
    def update_in_itinerary(self, itinerary_info) -> None:
        '''To update the itineraries'''
        package = self.check_itinerary((itinerary_info[3], ))
        if not package:
            raise DataNotFound
        self.db_access.non_returning_query(Query.UPDATE_ITINERARY_QUERY, itinerary_info)    
        
    