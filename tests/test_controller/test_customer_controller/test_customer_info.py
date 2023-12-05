import pytest
from controllers.customer_controller.customer_info import CustomerDetails
from config.prompt import PrintPrompts
from utils.pretty_print import data_tabulate



@pytest.fixture
def customer_fixture(mocker):
    customer = CustomerDetails('C_123')
    mock_obj = mocker.Mock()
    mocker.patch.object(customer, 'db_access', mock_obj)
    # mocker.patch(customer, 'customer_id', 'C_1233')
    return customer

class TestCustomerInfo:

    def test_update_details(self, mocker, customer_fixture):
        mocker.patch('builtins.input', side_effect = ['1', '2', '3', '4', '5', '6'])
        mocker.patch('controllers.customer_controller.customer_info.validate', lambda a, b: 'Mumbai')
        mocker.patch('controllers.customer_controller.customer_info.CustomerDetails.show_details', lambda a: None)
        customer_fixture.update_details()
        customer_fixture.db_access.non_returning_query.assert_called()

    def test_not_update(self, mocker, customer_fixture, capsys):
        mocker.patch('controllers.customer_controller.customer_info.CustomerDetails.show_details', lambda a: None)
        mocker.patch('builtins.input', side_effect = ['7', '6'])
        customer_fixture.update_details()
        captured = capsys.readouterr()
        assert PrintPrompts.INVALID_PROMPT in captured.out
        assert PrintPrompts.CUSTOMER_DETAILS in captured.out

    def test_show_details(self, mocker, customer_fixture):
        mocker.patch('controllers.customer_controller.customer_info.data_tabulate', lambda a, b: None)
        customer_fixture.show_details()
        customer_fixture.db_access.single_data_returning_query.assert_called_once()
