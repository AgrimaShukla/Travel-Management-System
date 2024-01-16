from config.queries import Query 
import shortuuid

from database.database_access import QueryExecutor

from config.regex_value import RegularExp

from config.prompt import PrintPrompts, InputPrompts, LoggingPrompt, TabulateHeader
from config.prompt_values import UPDATE_ITINERARY


class ItineraryController:

    def __init__(self):
        self.db_access = QueryExecutor()
    
    def add_itinerary(self, day, city, desc, package_id):
        itinerary_id = "I_" + shortuuid.ShortUUID().random(length = 8)
        data = (itinerary_id, package_id, day, city, desc)
        inserted = self.db_access.non_returning_query(Query.INSERT_ITINERARY_QUERY, data)
        # print(PrintPrompts.ADDED)
        return inserted

    def fetch_itinerary(self):
        data = self.db_access.returning_query(Query.SHOW_ITINERARY_QUERY)
        return data

    def check_itinerary(self, itinerary_id: str) -> tuple:
        '''To check existing itineraries'''
        data = self.db_access.single_data_returning_query(Query.CHECK_ITINERARY_QUERY, (itinerary_id, ))
        return data
    
    def update_in_itinerary(self, not_exist_itinerary, itinerary_id, value, updated_value) -> None:
        '''To update the itineraries'''
        if not_exist_itinerary == False:
            return -1
        data = self.check_itinerary(itinerary_id)
        if not data:
            return -2
        column_name = UPDATE_ITINERARY[value]
        updated = self.db_access.non_returning_query(Query.UPDATE_ITINERARY_QUERY.format(column_name), (updated_value, itinerary_id))
        return updated
    