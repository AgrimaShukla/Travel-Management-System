'''For pretty print of console'''

from tabulate import tabulate
from typing import Union

def data_tabulate(data_displayed: Union[tuple, list], headers_data: tuple) -> None:
    '''Using tabulate to print the data for pretty print'''
    row_num = [i for i in range(1, len(data_displayed)+1)]
    print(
        tabulate(
            data_displayed,
            headers = headers_data,
            showindex = row_num,
            tablefmt = 'simple_grid'
        )
    )
