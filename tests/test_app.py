import pytest
from app import main

@pytest.fixture
def main_fixture(mocker):
    mock_reg = mocker.Mock()
    mock_auth = mocker.Mock()
    mock_user = mocker.Mock()
    mock_admin = mocker.Mock()
    mocker.patch('app.Registration', mock_reg)
    mocker.patch('app.Authentication', mock_auth)
    mocker.patch('app.UserMenu', mock_user)
    mocker.patch('app.AdminMenu', mock_admin)
    return (mock_reg, mock_auth, mock_user, mock_admin)

class TestMain:

    def test_main(self, mocker, main_fixture, capsys):
        mocker.patch('builtins.input', side_effect = ['1', '2', 'str', '2', '3'])
        mock_reg = main_fixture[0]
        mock_auth = main_fixture[1]
        mock_user = main_fixture[2]
        mock_admin = main_fixture[3]
        mock_reg().save_customer.return_value = None
        mocker.patch.object(mock_auth(), 'user_authentication', side_effect = [('user', 'C_123'), ('admin', 'A_123')])
        mock_user().user_menu.return_value = None
        mock_admin().admin_menu.return_value = None
        main()
        captured = capsys.readouterr()
        assert 'WELCOME' in captured.out
        assert 'LOGIN' in captured.out
        assert 'SELECT ONE' in captured.out
        assert 'INVALID' in captured.out
