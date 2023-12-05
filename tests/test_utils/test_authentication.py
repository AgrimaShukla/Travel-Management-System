import pytest
from utils.authentication import Authentication
from config.prompt import PrintPrompts
import hashlib


@pytest.fixture
def auth_fixture(mocker):
    a = Authentication()
    mock_db_access = mocker.Mock()
    mocker.patch.object(a, 'db_access', mock_db_access)
    mocker.patch.object(a, 'attempts', 1)
    return a

class TestAuthentication:
    def test_user_authentication(self, mocker, auth_fixture):
        password = hashlib.md5('Agrima@18'.encode()).hexdigest()
        ls = iter([(password,),('user',) ])
        auth_fixture.db_access.single_data_returning_query = lambda a, b: next(ls)
        mocker.patch('utils.authentication.validation.validate', lambda a, b: 'agrima_19')
        mocker.patch('utils.authentication.validation.validate_password', lambda a: 'Agrima@18')
        assert auth_fixture.user_authentication()[0] == 'user'

    def test_user_authentication_invalid(self, mocker, auth_fixture, capsys):
        ls = iter([(None,),('user',) ])
        auth_fixture.db_access.single_data_returning_query.return_value = next(ls)
        mocker.patch('utils.authentication.validation.validate', lambda a, b: 'agrima_19')
        mocker.patch('utils.authentication.validation.validate_password', lambda a: 'Agrima18')
        auth_fixture.user_authentication()
        captured = capsys.readouterr()
        assert f'{PrintPrompts.INVALID_CREDENTIALS}\n{PrintPrompts.ATTEMPTS}' in captured.out
        assert  auth_fixture.attempts == 0
