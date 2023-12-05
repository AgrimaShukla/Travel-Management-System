import pytest
from controllers.customer_controller.booking.booking_module import BookPackage, data_tabulate
from config.prompt import PrintPrompts


@pytest.fixture
def book_package(mocker):
    book = BookPackage()
    mock_obj = mocker.Mock()
    mocker.patch.object(book, 'db_access', mock_obj)
    return book

class TestBookingModule:
    
    def test_add_booking(self, mocker, book_package, capsys):
        mocker.patch('controllers.customer_controller.booking.booking_module.validation', side_effect = ['Agrima', '9087950909', '2023-12-01', '2'])
        book_package.db_access.insert_table.return_value = True
        book_package.add_booking('P_123', 'C_123', 2, '19000')
        captured = capsys.readouterr()
        assert 'Booked' in captured.out

    def test_display_itinerary(self, mocker, book_package, capsys):
        mocker.patch.object(book_package.db_access, 'returning_query', side_effect = [(('B_124', 'ashukla', '2024-01-10'),)])
        mocker.patch('controllers.customer_controller.booking.booking_module.data_tabulate', lambda a, b: None)
        mocker.patch('controllers.customer_controller.booking.booking_module.validation.validate_uuid', side_effect = ['B_123', 'B_124'])
        book_package.display_booking('', '')
        captured = capsys.readouterr()
        assert 'BOOKING ID' in captured.out

    def test_display_not_itinerary(self, mocker, book_package, capsys):
        book_package.db_access.returning_query.return_value = []
        book_package.display_booking('', '')
        captured = capsys.readouterr()
        assert PrintPrompts.NO_BOOKINGS in captured.out

    def test_show_itinerary(self, mocker, book_package):
        mocker.patch.object(book_package, 'display_booking', lambda a, b: 'B_123')
        # book_package.display_booking.return_value = 'B_123'
        book_package.db_access.returning_query.return_value = [('1', 'mumbai', 'juhu'),]
        mock_tabulate = mocker.Mock()
        mocker.patch('controllers.customer_controller.booking.booking_module.data_tabulate', mock_tabulate)
        book_package.show_itinerary_package('C_123')
        mock_tabulate.assert_called_once()

    def test_cancel_booking(self, book_package):
        book_package.display_booking = lambda a, b: 'B_123'
        book_package.cancel_booking('C_123')
        book_package.db_access.non_returning_query.assert_called_once()
