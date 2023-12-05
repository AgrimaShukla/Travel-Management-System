import pytest
from controllers.customer_controller.review_module import Review
from config.prompt import PrintPrompts
from utils.pretty_print import data_tabulate

@pytest.fixture
def review_test(mocker):
    review = Review()
    mock_obj = mocker.Mock()
    mocker.patch.object(review, 'db_access', mock_obj)
    return review

class TestReviewModule:

    def test_add_review(self, mocker, review_test):
        mocker.patch('controllers.customer_controller.review_module.validate', side_effects = ['Agrima', 'Nice'] )
        review_test.add_review('B_123', 'P_123')
        review_test.db_access.non_returning_query.assert_called_once()

    def test_show_review(self, review_test, capsys):
        review_test.db_access.returning_query.return_value = [('agrima', 'nice', '9-11-2023')]
        review_test.show_review('P_123')
        captured = capsys.readouterr()
        assert 'agrima' in captured.out

    def test_show_data(self, mocker, review_test, capsys):
        review_test.db_access.returning_query.return_value = [('B_123', '12-12-2023', '16-12-2023')]
        mocker.patch('controllers.customer_controller.review_module.data_tabulate', lambda a, b: None)
        mocker.patch('controllers.customer_controller.review_module.validate_uuid', side_effect  = ['B_124','B_123'])
        review_test.db_access.single_data_returning_query.return_value = ('P_123',)
        mocker.patch.object(review_test, 'add_review', lambda a, b: None)
        review_test.show_data('C_123')
        captured = capsys.readouterr()
        assert PrintPrompts.INVALID_BOOKING in captured.out
        assert PrintPrompts.REVIEW in captured.out

    def test_show_no_data(self, review_test, capsys):
        review_test.db_access.returning_query.return_value = None
        review_test.show_data('C_123')
        captured = capsys.readouterr()
        assert f"{PrintPrompts.NO_BOOKINGS}\n" == captured.out
