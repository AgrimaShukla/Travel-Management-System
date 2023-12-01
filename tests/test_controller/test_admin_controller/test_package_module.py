import pytest
from controllers.admin_controller.package_module import Package
from config.prompt import PrintPrompts

@pytest.fixture
def package_fixture(mocker):
    obj_package = Package()
    mock_obj = mocker.Mock()
    mocker.patch.object(obj_package, 'db_access', mock_obj)
    return obj_package

def test_update_in_package(mocker, package_fixture):
    mocker.patch('controllers.admin_controller.package_module.Package.show_package', lambda a,b,c: True)
    mocker.patch('controllers.admin_controller.package_module.validate_uuid', lambda a,b :'P_1234')
    check_package = ['False', 'True']
    mocker.patch('controllers.admin_controller.package_module.Package.check_package', lambda a, b: check_package.pop(0))
    value = ['str', '3']
    mocker.patch('builtins.input', lambda _: value.pop(0))
    mocker.patch('controllers.admin_controller.package_module.validate', lambda a,b: 'beaches')
    package_fixture.update_in_package()
    package_fixture.db_access.non_returning_query.assert_called_once()

def test_print_update_in_package(mocker, package_fixture, capsys):
    mocker.patch('controllers.admin_controller.package_module.Package.show_package', lambda a,b,c: False)
    package_fixture.update_in_package()
    captured = capsys.readouterr()
    assert 'NO PACKAGE FOUND' in captured.out

def test_change_status(mocker, package_fixture):
    mocker.patch('controllers.admin_controller.package_module.Package.show_package', lambda a,b,c: True)
    mocker.patch('builtins.input', lambda _: 'P_1234')
    mocker.patch('controllers.admin_controller.package_module.Package.check_package', lambda a, b: True)
    package_fixture.change_status_package('activate')
    package_fixture.db_access.non_returning_query.assert_called_once()

def test_print_change_status(mocker, package_fixture, capsys):
    mocker.patch('controllers.admin_controller.package_module.Package.show_package', lambda a,b,c: False)
    package_fixture.change_status_package('activate')
    captured = capsys.readouterr()
    assert f"{PrintPrompts.NO_PACKAGE_FOUND}\n" == captured.out

def test_no_package_status(mocker, package_fixture, capsys):
    mocker.patch('controllers.admin_controller.package_module.Package.show_package', lambda a,b,c: True)
    mocker.patch('builtins.input', lambda _: 'P_1234')
    mocker.patch('controllers.admin_controller.package_module.Package.check_package', lambda a, b: None)
    package_fixture.change_status_package('activate')
    captured = capsys.readouterr()
    assert f"{PrintPrompts.NO_PACKAGE.format('P_1234')}\n" == captured.out
    
def test_add_package(mocker, package_fixture):
    lst = ['beaches', '2 days 1 nights', 'luxury', '20000', 'active']
    mocker.patch('controllers.admin_controller.package_module.validate', lambda a,b: lst.pop(0))
    package_fixture.add_package()
    package_fixture.db_access.non_returning_query.assert_called_once()

def test_check_package(package_fixture):
    package_fixture.check_package(('P_123,'))
    package_fixture.db_access.single_data_returning_query.assert_called_once()

def test_show_package_false(package_fixture):
    package_fixture.db_access.returning_query.return_value = []
    value = package_fixture.show_package('123', 'active')
    assert value == False

def test_show_package_true(package_fixture):
    package_fixture.db_access.returning_query.return_value = ['agrima']
    value = package_fixture.show_package('123', 'active')
    assert value == True

def test_show_package_print(package_fixture, capsys):
    package_fixture.db_access.returning_query.return_value = [('P_123', 'beaches', '2 days 1 nights', 'luxury', '19000', 'active')]
    package_fixture.show_package('123', 'active')
    captured = capsys.readouterr()
    assert 'beaches' in captured.out