import pytest
from menus.user import UserMenu, PrintPrompts

@pytest.fixture
def user_fixture(mocker):
    user = UserMenu('C_123')
    mock_booking = mocker.Mock()
    mock_customer = mocker.Mock()
    mock_review = mocker.Mock()
    mocker.patch.object(user, 'obj_booking', mock_booking)
    mocker.patch.object(user, 'obj_customer', mock_customer)
    mocker.patch.object(user, 'obj_review', mock_review)
    return user

class TestUserMenu:

    def test_category(self, mocker, user_fixture, capsys):
        mocker.patch('builtins.input', side_effect = ['1', '2', '3', '5', '4'])
        mocker.patch.object(user_fixture, 'day_menu', lambda a, b, d: None)
        user_fixture.category_menu('beaches')
        captured = capsys.readouterr()
        assert 'INVALID OPTION'  in captured.out

    def test_destination(self, mocker, user_fixture, capsys):
        mocker.patch('builtins.input', side_effect = ['1', '2', '3', '4', '5', 'str', '6'])
        mocker.patch.object(user_fixture, 'category_menu', lambda a: None)
        user_fixture.destination_menu()
        captured = capsys.readouterr()
        assert 'INVALID OPTION'  in captured.out


    def test_day(self, mocker, user_fixture, capsys):
        mocker.patch('builtins.input', side_effect = ['1', '2', '3', '5', '4'])
        mocker.patch('menus.user.view_package', lambda a, b, c, d: None)
        user_fixture.day_menu('beaches', 'luxury', 'C_123')
        captured = capsys.readouterr()
        assert 'INVALID OPTION'  in captured.out

    def test_user_menu(self, mocker, user_fixture, capsys):
        mocker.patch('builtins.input', side_effect = ['1', '2', '3', '5', '4', '6', 'str', '7'])
        mocker.patch('menus.user.UserMenu.destination_menu', lambda _: None)
        user_fixture.user_menu()
        captured = capsys.readouterr()
        assert 'INVALID OPTION' in captured.out
