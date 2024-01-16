'''Admin operations are handled in this module.
   - Show itinerary
   - Update itinerary'''

import logging

from config.prompt import PrintPrompts, InputPrompts, LoggingPrompt, TabulateHeader
from utils.pretty_print import data_tabulate
from utils.validation import validate, validate_uuid
from controller.admin_controller.itinerary import ItineraryController
from config.regex_value import RegularExp
logger = logging.getLogger(__name__)

class Itinerary:

    '''New Itinerary created by admin'''
    def __init__(self) -> None:
        
        self.iti_controller = ItineraryController()

    def add_itinerary(self, package_id: str) -> None:
        '''New itinerary added by admin'''
        while True:
            day = validate( RegularExp.NUMBER_VALUE, InputPrompts.INPUT.format('day'))
            city = validate(RegularExp.STRING_VALUE, InputPrompts.INPUT.format('city'))
            desc = validate(RegularExp.STRING_VALUE, InputPrompts.INPUT.format('desc'))
            inserted = self.iti_controller.add_itinerary(day, city, desc, package_id)
            if inserted == True:
                print(PrintPrompts.INSERTED)
                break
            else:
                print(PrintPrompts.UNEXPECTED_ISSUE)
    
    def show_itinerary(self) -> bool:
        '''All the itineraries are displayed'''
        data = self.iti_controller.fetch_itinerary()
        if not data:
            logger.info(LoggingPrompt.NO_DATA)
            return False
        else:
            data_tabulate(data, (TabulateHeader.PACKAGE_ID, TabulateHeader.ITINERARY_ID, TabulateHeader.DAY, TabulateHeader.CITY, TabulateHeader.DESC, TabulateHeader.STATUS))
            return True 

    def update_itinerary(self):
        not_exist_ititnerary = self.show_itinerary()
        while True:
            itinerary_id = validate_uuid(InputPrompts.ITINERARY_ID, RegularExp.UUID)
            # itinerary_id = validate_uuid(InputPrompts.ITINERARY_ID, RegularExp.UUID)
            return_value = self.iti_controller.check_itinerary(itinerary_id)
            if not return_value:
                print(PrintPrompts.NO_ITINERARY.format(itinerary_id))
                continue
            print(PrintPrompts.UPDATE_ITINERARY)
            value = input(InputPrompts.ENTER)
            if value not in ('1', '2', '3'):
                print(PrintPrompts.INVALID_PROMPT)
                continue
            match value:
                case '1': 
                    valid_value = validate(RegularExp.NUMBER_VALUE, InputPrompts.INPUT.format('day'))
                case '2':
                    valid_value = validate(RegularExp.STRING_VALUE, InputPrompts.INPUT.format('city'))
                case '3':
                    valid_value = validate(RegularExp.STRING_VALUE, InputPrompts.INPUT.format('desc'))
            return_value = self.iti_controller.update_in_itinerary(not_exist_ititnerary, itinerary_id, value, valid_value)
            if return_value == -1:
                print(PrintPrompts.NO_ITINERARY_FOUND)
            elif return_value == -2:
                print(PrintPrompts.NO_ITINERARY.format(itinerary_id))
            elif return_value == True:
                print(PrintPrompts.UPDATED)
                break
            else:
                print(PrintPrompts.UNEXPECTED_ISSUE)

