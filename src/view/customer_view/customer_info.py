'''For showing and updating customer details'''

from utils.pretty_print import data_tabulate
from config.prompt import TabulateHeader
from config.prompt import InputPrompts, PrintPrompts
from config.prompt_values import CUSTOMER_DETAILS
from controller.customer_controller.customer_info import CustomerController
from utils.validation import validate
from config.regex_value import RegularExp

class CustomerDetails:

    '''Managing customer details'''
    def __init__(self, customer_id: str) -> None:
        self.customer_id = customer_id
        self.cust = CustomerController(self.customer_id)


    def show_details(self) -> None:
        '''showing customer details'''
        customer_details = self.cust.display_details()
        customer_details = [customer_details]
        data_tabulate(customer_details, (TabulateHeader.NAME, TabulateHeader.MOBILE_NUMBER, TabulateHeader.GENDER, TabulateHeader.AGE, TabulateHeader.EMAIL))


    def enter_details(self) -> None:
        '''update details of customer'''
        self.show_details()
        while True:
            print(PrintPrompts.CUSTOMER_DETAILS)
            value = input(InputPrompts.ENTER)
            match value:
                case '1': 
                    entered_value = validate(RegularExp.NAME, InputPrompts.INPUT.format('name'))
                case '2':
                    entered_value = validate(RegularExp.MOBILE_NUMBER, InputPrompts.INPUT.format('mobile number'))
                case '3':
                    entered_value = validate(RegularExp.GENDER, InputPrompts.INPUT.format('gender'))
                case '4': 
                    entered_value = validate(RegularExp.AGE, InputPrompts.INPUT.format('age'))
                case '5': 
                    entered_value = validate(RegularExp.EMAIL, InputPrompts.INPUT.format('email'))
                case '6':
                    break
                case '_':
                    print(PrintPrompts.INVALID_PROMPT)
                    continue

            column = CUSTOMER_DETAILS[value]
            # entered_value = input(InputPrompts.INPUT.format(column))
            updated = self.cust.update_details(column, entered_value)
            if updated == True:
                print(PrintPrompts.UPDATED)
            else:
                print(PrintPrompts.UNEXPECTED_ISSUE)
            