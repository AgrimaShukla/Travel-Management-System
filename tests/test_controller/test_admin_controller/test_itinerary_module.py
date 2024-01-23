import pytest
from controller.admin_controller.itinerary import ItineraryController
from config.prompt import PrintPrompts

@pytest.fixture
def itinerary_fixture(mocker):
    obj_itinerary = ItineraryController()
    mocker_obj = mocker.Mock()
    mocker.patch.object(obj_itinerary, 'db_access', mocker_obj)
    return obj_itinerary

class TestItinerary:
        
    value = ['1', '2', '3']

    @pytest.mark.parametrize('value', value)
    def test_update_in_itinerary(self, mocker, itinerary_fixture, value):
        mocker.patch('controllers.admin_controller.itinerary_module.Itinerary.show_itinerary', lambda _: True)
        mocker.patch('controllers.admin_controller.itinerary_module.validate_uuid', lambda a,b: 'I_1234')
        mocker.patch('controllers.admin_controller.itinerary_module.Itinerary.check_itinerary', lambda a, b: ('mumbai',))
        # input_data = ['str', '2']
        mocker.patch('builtins.input', lambda a: value)
        mocker.patch('controllers.admin_controller.itinerary_module.validate', lambda a, b: 'pune')
        itinerary_fixture.update_in_itinerary()
        itinerary_fixture.db_access.non_returning_query.assert_called_once()

    
    def test_update_itinerary_invalid(self, mocker, itinerary_fixture, capsys):
        mocker.patch('controllers.admin_controller.itinerary_module.Itinerary.show_itinerary', lambda _: True)
        mocker.patch('controllers.admin_controller.itinerary_module.validate_uuid', side_effect = ['I_1234', 'I_124', 'I_125'])
        mocker.patch('controllers.admin_controller.itinerary_module.Itinerary.check_itinerary', side_effect = [False, True, True])
        mocker.patch('builtins.input', side_effect = ['str', '1'])
        mocker.patch('controllers.admin_controller.itinerary_module.validate', lambda a,b: 'beaches')
        itinerary_fixture.update_in_itinerary()
        captured = capsys.readouterr()
        assert 'INVALID' in captured.out
        assert 'NO ITINERARY' in captured.out

    def test_print_update_in_itinerary(self, mocker, itinerary_fixture, capsys):
        mocker.patch('controllers.admin_controller.itinerary_module.Itinerary.show_itinerary', lambda _: False)
        itinerary_fixture.update_in_itinerary()
        captured = capsys.readouterr()
        assert f"{PrintPrompts.NO_ITINERARY_FOUND}\n" == captured.out

    def test_check_itinerary(self, itinerary_fixture):
        itinerary_fixture.check_itinerary(('I_123,'))
        itinerary_fixture.db_access.single_data_returning_query.assert_called_once()

    def test_show_itinerary_true(self, itinerary_fixture):
        itinerary_fixture.db_access.returning_query.return_value = ['2 days 3 nights']
        value = itinerary_fixture.show_itinerary()
        assert value == True

    def test_show_itinerary_false(self, itinerary_fixture):
        itinerary_fixture.db_access.returning_query.return_value = []
        value = itinerary_fixture.show_itinerary()
        assert value == False

    def test_add_itinerary(self, mocker, itinerary_fixture):
        lst = ['2', 'mumbai', 'juhu beach']
        mocker.patch('controllers.admin_controller.itinerary_module.validate', lambda a, b: lst.pop(0))
        itinerary_fixture.add_itinerary('P_123')
        itinerary_fixture.db_access.non_returning_query.assert_called_once()
