'''Admin operations are handled in this module.
   - Show itinerary
   - Update itinerary'''

import logging
import shortuuid

from utils.validation import validate, validate_uuid
from config.prompt import PrintPrompts, InputPrompts, LoggingPrompt, TabulateHeader
from config.prompt_values import UPDATE_ITINERARY
from config.queries import Query 
from database.database_access import QueryExecutor
from utils.pretty_print import data_tabulate
from config.regex_value import RegularExp

logger = logging.getLogger(__name__)

class Itinerary:

    '''New Itinerary created by admin'''
    def __init__(self) -> None:
        self.db_access = QueryExecutor()

    def add_itinerary(self, package_id: str) -> None:
        '''New itinerary added by admin'''
        itinerary_id = "I_" + shortuuid.ShortUUID().random(length = 8)
        day = validate(InputPrompts.INPUT.format('day'), RegularExp.NUMBER_VALUE)
        city = validate(InputPrompts.INPUT.format('city'), RegularExp.STRING_VALUE)
        desc = validate(InputPrompts.INPUT.format('description'), RegularExp.STRING_VALUE)
        data = (itinerary_id, package_id, day, city, desc)
        self.db_access.non_returning_query(Query.INSERT_ITINERARY_QUERY, data, PrintPrompts.ADDED)
    
    
    def show_itinerary(self) -> bool:
        '''All the itineraries are displayed'''
        data = self.db_access.returning_query(Query.SHOW_ITINERARY_QUERY)
        if not data:
            logger.info(LoggingPrompt.NO_DATA)
            return False
        else:
            data_tabulate(data, (TabulateHeader.PACKAGE_ID, TabulateHeader.ITINERARY_ID, TabulateHeader.DAY, TabulateHeader.CITY, TabulateHeader.DESC, TabulateHeader.STATUS))
            return True
        
            
    def check_itinerary(self, itinerary_id: str) -> tuple:
        '''To check existing itineraries'''
        data = self.db_access.single_data_returning_query(Query.CHECK_ITINERARY_QUERY, (itinerary_id, ))
        return data


    def update_in_itinerary(self) -> None:
        '''To update the itineraries'''
        not_exist_ititnerary = self.show_itinerary()
        # if else to check if table is empty or not
        if not_exist_ititnerary == True:
            while True:
                itinerary_id = validate_uuid(InputPrompts.ITINERARY_ID, RegularExp.UUID)
                # to check if itinerary exists or not of given id
                data = self.check_itinerary(itinerary_id)
                if data:
                    print(PrintPrompts.UPDATE_ITINERARY)
                    value = input(InputPrompts.ENTER)
                    match value:
                        case '1': 
                            updated_value = validate(InputPrompts.INPUT.format('day'), RegularExp.NUMBER_VALUE)
                        case '2':
                            updated_value = validate(InputPrompts.INPUT.format('city'), RegularExp.STRING_VALUE)
                        case '3':
                            updated_value = validate(InputPrompts.INPUT.format('description'), RegularExp.STRING_VALUE)
                        case _: 
                            print(PrintPrompts.INVALID_PROMPT)
                            continue
                    column_name = UPDATE_ITINERARY[value]
                    self.db_access.non_returning_query(Query.UPDATE_ITINERARY_QUERY.format(column_name), (updated_value, itinerary_id), PrintPrompts.UPDATED)
                    break
                else:
                    print(PrintPrompts.NO_ITINERARY.format(itinerary_id))
        else:
            print(PrintPrompts.NO_ITINERARY_FOUND)
