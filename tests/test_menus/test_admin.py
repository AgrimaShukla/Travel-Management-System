import pytest
from menus.admin import AdminMenu, PrintPrompts

@pytest.fixture
def admin_fixture(mocker):
    admin = AdminMenu()
    mock_package = mocker.Mock()
    mock_itinerary = mocker.Mock()
    mocker.patch.object(admin, 'obj_package', mock_package)
    mocker.patch.object(admin, 'obj_itinerary', mock_itinerary)
    return admin

def test_admin_menu(mocker, admin_fixture, capsys):
    mocker.patch('builtins.input', side_effect = ['1', '2', '3', '4', '5', '8', '7'])
    admin_fixture.admin_menu()
    captured = capsys.readouterr()
    assert PrintPrompts.INVALID_PROMPT in captured.out

def test_admin_itinerary(mocker, admin_fixture, capsys):
    mocker.patch('builtins.input', side_effect = ['6', '2', '3', '7', '4', '7'])
    admin_fixture.admin_menu()
    captured = capsys.readouterr()
    assert PrintPrompts.INVALID_PROMPT in captured.out
