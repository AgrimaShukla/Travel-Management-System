import pytest
import hashlib
from controllers.registration import Registration
from config.prompt import PrintPrompts

@pytest.fixture
def registration_fixture(mocker):
    reg = Registration()
    obj_mock = mocker.Mock()
    mocker.patch.object(reg, 'db_access', obj_mock)
    return reg

def test_save_customer(mocker, registration_fixture, capsys):
    lst = ['agrima_17', 'Agrima', '9093839939', 'female', '21', 'agrima@gmail.com']
    mocker.patch('controllers.registration.validation.validate', lambda a, b: lst.pop(0))
    mocker.patch('controllers.registration.validation.validate_password', lambda a: 'Agrima@17')
    registration_fixture.db_access.insert_table.return_value = True
    registration_fixture.save_customer()
    captured = capsys.readouterr()
    assert f"{PrintPrompts.SUCCESFULLY}" in captured.out
