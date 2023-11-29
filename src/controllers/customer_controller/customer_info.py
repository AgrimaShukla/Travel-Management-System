'''For showing and updating customer details'''

from database.database_access import QueryExecutor
from utils.pretty_print import data_tabulate
from config.prompt import TabulateHeader
from config.queries import Query
from utils.validation import validate
from config.prompt import InputPrompts, PrintPrompts
from config.regex_value import RegularExp
from config.prompt_values import CUSTOMER_DETAILS

class CustomerDetails:

    '''Managing customer details'''
    def __init__(self, customer_id: str) -> None:
        self.customer_id = customer_id
        self.db_access = QueryExecutor()


    def show_details(self) -> None:
        '''showing customer details'''
        customer_details = self.db_access.single_data_returning_query(Query.SELECT_CUSTOMER, (self.customer_id, ))
        customer_details = [customer_details]
        data_tabulate(customer_details, (TabulateHeader.NAME, TabulateHeader.MOBILE_NUMBER, TabulateHeader.GENDER, TabulateHeader.AGE, TabulateHeader.EMAIL))


    def update_details(self) -> None:
        '''update details of customer'''
        self.show_details()
        while True:
            print(PrintPrompts.CUSTOMER_DETAILS)
            details = input(InputPrompts.ENTER)
            if details in ('1', '2', '3', '4', '5', '6'):
                match details:
                    case '1': 
                        update_value = validate(InputPrompts.ENTER_DETAIL.format('NAME'), RegularExp.NAME)
                    case '2':
                        update_value = validate(InputPrompts.ENTER_DETAIL.format('MOBILE NUMBER'), RegularExp.MOBILE_NUMBER)
                    case '3':
                        update_value = validate(InputPrompts.GENDER, RegularExp.GENDER)
                    case '4': 
                        update_value = validate(InputPrompts.ENTER_DETAIL.format('AGE'), RegularExp.AGE)
                    case '5': 
                        update_value = validate(InputPrompts.EMAIL, RegularExp.EMAIL)
                    case '6': break
                column = CUSTOMER_DETAILS[details]
                self.db_access.non_returning_query(Query.UPDATE_CUSTOMER.format(column), (update_value, self.customer_id), PrintPrompts.UPDATED)

            else:
                print(PrintPrompts.INVALID_PROMPT)
