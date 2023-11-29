import pytest
from controllers.customer_controller.customer_info import CustomerDetails

@pytest.fixture
def customer_fixture(mocker):
    customer = CustomerDetails()
    mock_obj = mocker.Mock()
    mocker.patch.object(customer, 'db_access', mock_obj)
    mocker.patch(customer, 'customer_id', 'C_1233')
    return customer




