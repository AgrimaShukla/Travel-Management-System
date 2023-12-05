import pytest
import sqlite3
from utils.initialize_app import create_admin, create_tables
from utils.initialize_app import QueryExecutor
from database.context_manager import DatabaseConnection


@pytest.fixture
def mock_database_connection(mocker):
    mock_connection = mocker.MagicMock(spec = DatabaseConnection)
    mocker.patch('utils.initialize_app.DatabaseConnection', return_value = mock_connection)
    mock_cursor = mocker.MagicMock()
    mock_connection.__enter__.return_value.cursor.return_value = mock_cursor
    mock_connection.__exit__.return_value = None
    return mock_cursor

@pytest.fixture
def mock_query_executor(mocker):
    obj_query_executor = mocker.Mock()
    mocker.patch('utils.initialize_app.QueryExecutor', obj_query_executor)
    return obj_query_executor

class TestInitializeApp:

    def test_create_tables(self, mock_database_connection):
        mock_cursor = mock_database_connection
        create_tables()
        mock_cursor.execute.assert_called()

    def test_create_tables_error(self, mock_database_connection, caplog):
        mock_cursor = mock_database_connection
        mock_cursor.execute.side_effect = sqlite3.Error('Mock Error')
        create_tables()
        assert 'Mock Error' in caplog.text

    def test_create_admin(self, monkeypatch, mock_query_executor):
        monkeypatch.setenv('USERNAME', 'ashukla123')
        monkeypatch.setenv('PASSWORD', 'admin123')
        monkeypatch.setenv('NAME', 'agrima shukla')
        monkeypatch.setenv('MOBILE_NUMBER', '9057689075')
        monkeypatch.setenv('GENDER', 'female')
        monkeypatch.setenv('AGE', '21')
        monkeypatch.setenv('EMAIL', 'admin@gmail.com')
        mock_query_executor().single_data_returning_query.return_value = None
        create_admin()
        mock_query_executor().insert_table.assert_called_once()


