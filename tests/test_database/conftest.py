import pytest
from database.context_manager import DatabaseConnection

@pytest.fixture
def mock_database_connection(mocker):
    mock_connection = mocker.MagicMock(spec = DatabaseConnection)
    mocker.patch('database.database_access.DatabaseConnection', return_value = mock_connection)
    mock_cursor = mocker.MagicMock()
    mock_connection.__enter__.return_value.cursor.return_value = mock_cursor
    mock_connection.__exit__.return_value = None
    return mock_cursor
