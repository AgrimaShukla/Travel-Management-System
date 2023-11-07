'''For pretty print of console'''

from tabulate import tabulate

def data_tabulate(data_displayed, headers_data):
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