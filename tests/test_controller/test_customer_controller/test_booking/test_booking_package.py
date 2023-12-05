import pytest
from controllers.customer_controller.booking.booking_package import view_package
from config.prompt import PrintPrompts

@pytest.fixture
def query_executor(mocker):
    mock_cls = mocker.Mock()
    mocker.patch('controllers.customer_controller.booking.booking_package.QueryExecutor', mock_cls)
    return mock_cls

@pytest.fixture
def book_package(mocker):
    mock_cls = mocker.Mock()
    mocker.patch('controllers.customer_controller.booking.booking_package.BookPackage', mock_cls)
    return mock_cls

@pytest.fixture
def review(mocker):
    mock_cls = mocker.Mock()
    mocker.patch('controllers.customer_controller.booking.booking_package.Review', mock_cls)
    return mock_cls

class TestBookingPackage:

    def test_view_package(self, mocker, query_executor, book_package, review, capsys):
        query_executor().returning_query.return_value = [('1', 'mumbai', 'juhu'), ('2', 'ratnagiri', 'nagaun')]
        query_executor().single_data_returning_query.return_value = ('P_123', '20000', '3 days and 1 nights')
        mocker.patch('builtins.input', side_effect = ['1', '2', '4', '3'])
        mocker.patch('controllers.customer_controller.booking.booking_package.data_tabulate', lambda a, b: None)
        view_package('1', '1', '2', 'C_123')
        captured = capsys.readouterr()
        book_package().add_booking.assert_called_once() 
        review().show_review.assert_called_once()
        assert PrintPrompts.INVALID_PROMPT in captured.out
        assert 'Price' in captured.out
        assert PrintPrompts.BOOKING in captured.out
        