import pytest
import datetime
from utils.validation import input_validation
from utils.validation import validate, validate_uuid, validate_password, error_handling, validate_date
from config.regex_value import RegularExp
from config.prompt import InputPrompts, PrintPrompts

valid_data = [(RegularExp.USERNAME, 'aayushi_23'),
        (RegularExp.DURATION, '2 days 1 nights'),
        (RegularExp.MOBILE_NUMBER, '9899093849'),
        (RegularExp.NAME, 'Agrima Shukla'),
        (RegularExp.STATUS, 'active'),
        (RegularExp.STATUS, 'inactive'),
        (RegularExp.STRING_VALUE, 'mumbai and goa'),
        (RegularExp.AGE, '21'),
        (RegularExp.GENDER, 'female'),
        (RegularExp.NUMBER_VALUE, '1232'),
        (RegularExp.PASSWORD, 'Agrima@18'),
        (RegularExp.PERSON, '2'),
        (RegularExp.UUID, 'P_sgwft2SIO')]

invalid_data = [(RegularExp.USERNAME, 'aayushi@23'),
        (RegularExp.DURATION, '2  1 nights'),
        (RegularExp.MOBILE_NUMBER, '989909349'),
        (RegularExp.NAME, 'Agrim&&a Shukla'),
        (RegularExp.STATUS, 'deactivate'),
        (RegularExp.STRING_VALUE, 'mumbai 2451a'),
        (RegularExp.AGE, '2001'),
        (RegularExp.GENDER, '@2'),
        (RegularExp.NUMBER_VALUE, 'str'),
        (RegularExp.PASSWORD, ''),
        (RegularExp.PERSON, 'str'),
        (RegularExp.UUID, 'P@sgwft2SIO')]

data = [(InputPrompts.INPUT.format("name"), RegularExp)
]

def mock_error_handling():
    return False

@pytest.mark.parametrize("regex_exp, value", valid_data)
def test_valid_data(regex_exp, value):
    '''Test for validating input'''
    assert input_validation(regex_exp, value)

@pytest.mark.parametrize("regex_exp, value", invalid_data)
def test_invalid_data(regex_exp, value):
    '''Test for validating input'''
    assert not input_validation(regex_exp, value)

# @pytest.mark.parametrize("prompts, regular_exp", data)
# def test_validate_function(prompts, regular_exp):
    
@pytest.mark.parametrize("data", [(("@123", "agrima_18"), (False, True))])
def test_validate(monkeypatch, data):
    test_username = iter(data[0])
    result = iter(data[1])
    monkeypatch.setattr("builtins.input", lambda _: next(test_username))
    monkeypatch.setattr('utils.validation.input_validation', lambda a, b: next(result))
    assert validate(InputPrompts.INPUT.format("username"), RegularExp.USERNAME) == data[0][-1]
    
@pytest.mark.parametrize("data", [(("@123", "P_124567"), (False, True))])
def test_validate_uuid(monkeypatch, data):
    test_username = iter(data[0])
    result = iter(data[1])
    monkeypatch.setattr("builtins.input", lambda _: next(test_username))
    monkeypatch.setattr('utils.validation.input_validation', lambda a, b: next(result))
    assert validate_uuid(InputPrompts.INPUT.format("username"), RegularExp.USERNAME) == data[0][-1]

def test_validate_password(monkeypatch):
    data = ['123', 'vsjvs', 'Agrima@18']
    monkeypatch.setattr("utils.validation.maskpass.askpass", lambda **kwargs: data.pop(0))
    result = validate_password(RegularExp.PASSWORD) 
    assert result == 'Agrima@18'

def test_error_handling(capsys):
    error_handling(mock_error_handling)()
    captured = capsys.readouterr()
    assert "Wrong input! Enter again." in captured.out

def test_validate_date(monkeypatch):
    data = ['2020-12-01', '2023-11-31', '2023-12-03']
    monkeypatch.setattr('builtins.input', lambda _: data.pop(0))
    start_date = validate_date()
    assert start_date ==  datetime.date(2023, 12, 3)
    