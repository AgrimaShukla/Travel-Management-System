import pytest
from view.customer_view.customer_info import CustomerDetails


@pytest.fixture
def customer_fixture(mocker):
    customer = CustomerDetails('C_123')
    mock_obj = mocker.Mock()
    mocker.patch.object(customer, 'cust', mock_obj)
    return customer

class TestCustomerDetails:

    def test_show_details(self, mocker, customer_fixture):
       mocker.patch('view.customer_view.customer_info.data_tabulate', lambda a, b: None)
       customer_fixture.show_details()
       customer_fixture.cust.display_details.assert_called_once()

    def test_enter_details(self, mocker, customer_fixture):
        mocker.patch()
