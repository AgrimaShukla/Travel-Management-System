'''For showing and updating customer details'''

from src.database import database_access
from src.utils.pretty_print import data_tabulate
from src.config.prompt import TabulateHeader
from src.config.queries import Query
from src.utils.validation import validate
from src.config.prompt import InputPrompts, PrintPrompts
from src.config.regex_value import RegularExp
from src.config.prompt_values import CUSTOMER_DETAILS

def show_details(customer_id: str) -> None:
    '''showing customer details'''
    customer_details = database_access.single_data_returning_query(Query.SELECT_CUSTOMER, (customer_id, ))
    customer_details = [customer_details]
    data_tabulate(customer_details, (TabulateHeader.NAME, TabulateHeader.MOBILE_NUMBER, TabulateHeader.GENDER, TabulateHeader.AGE, TabulateHeader.EMAIL))


def update_details(customer_id: str) -> None:
    '''update details of customer'''
    show_details(customer_id)
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
            database_access.non_returning_query(Query.UPDATE_CUSTOMER.format(column), (update_value, customer_id), PrintPrompts.UPDATED)

        else:
            print(PrintPrompts.INVALID_PROMPT)
