import pytest
import sqlite3
from database.database_access import QueryExecutor

@pytest.fixture
def query_executor_fixture():
    query_executor = QueryExecutor()
    return query_executor

class TestQueryExecutor:

    returning_query = "SELECT * FROM table"
    single_returning_query = "SELECT name, age FROM table WHERE id = ?"
    non_returning_query = "INSERT INTO table WHERE name = ? AND profession = ?"
    data = ('example', 'data')
    mock_fetchall_result = [('result1',), ('result2',)]
    insert_1 = 'INSERT INTO table1 VALUES (?, ?)'
    insert_2 = 'INSERT INTO table2 VALUES (?, ?)'
    para_1 = ('123', 'user')
    para_2 = ('Agrima', '21')


    def test_returning_query_params(self, mock_database_connection, query_executor_fixture):
        mock_cursor = mock_database_connection
        mock_cursor.execute().fetchall.return_value = self.mock_fetchall_result
        result = query_executor_fixture.returning_query(self.returning_query, self.data)
        mock_cursor.execute.assert_called_with(self.returning_query, self.data)
        assert result == self.mock_fetchall_result

    def test_returning_query_error(self, mock_database_connection, caplog, query_executor_fixture):
        mock_cursor = mock_database_connection
        mock_cursor.execute.side_effect = sqlite3.Error('Mock Error')
        query_executor_fixture.returning_query(self.returning_query)
        assert 'Mock Error' in caplog.text

    def test_returning_query_without_params(self, mock_database_connection, query_executor_fixture):
        mock_cursor = mock_database_connection
        mock_cursor.execute().fetchall.return_value = self.mock_fetchall_result
        result = query_executor_fixture.returning_query(self.returning_query)
        mock_cursor.execute.assert_called()
        assert result == self.mock_fetchall_result

    def test_non_returning_query_params(self, mock_database_connection, query_executor_fixture, capsys):
        mock_cursor = mock_database_connection
        query_executor_fixture.non_returning_query(self.non_returning_query, self.data, "Done")
        captured = capsys.readouterr()
        mock_cursor.execute.assert_called_once()
        assert "Done" in captured.out

    def test_non_returning_query_error(self, mock_database_connection, query_executor_fixture, capsys, caplog):
        mock_cursor = mock_database_connection
        mock_cursor.execute.side_effect = sqlite3.Error('Mock Error')
        query_executor_fixture.non_returning_query(self.non_returning_query, self.data, "Error")
        captured = capsys.readouterr()
        assert "Mock Error" in caplog.text
        assert "UNEXPECTED " in captured.out
    
    
    def test_non_returning_query_integrity_error(self, mock_database_connection, query_executor_fixture, capsys, caplog):
        mock_cursor = mock_database_connection
        mock_cursor.execute.side_effect = sqlite3.IntegrityError('Mock Error')
        query_executor_fixture.non_returning_query(self.non_returning_query, self.data, "Error")
        captured = capsys.readouterr()
        assert "Mock Error" in caplog.text
        assert "USER " in captured.out

    def test_single_data_returning_query(self, mock_database_connection, query_executor_fixture):
        mock_cursor = mock_database_connection
        mock_cursor.execute().fetchone.return_value = self.mock_fetchall_result
        result = query_executor_fixture.single_data_returning_query(self.single_returning_query, ('123', ))
        mock_cursor.execute.assert_called()
        assert result == self.mock_fetchall_result

    def test_single_data_returning_query_error(self, mock_database_connection, query_executor_fixture, caplog, capsys):
        mock_cursor = mock_database_connection
        mock_cursor.execute.side_effect = sqlite3.Error('Mock Error')
        query_executor_fixture.single_data_returning_query(self.single_returning_query, self.data)
        captured = capsys.readouterr()
        assert 'Mock Error' in caplog.text
        assert 'UNEXPECTED' in captured.out

    def test_insert_table(self, mock_database_connection, query_executor_fixture):
        mock_cursor = mock_database_connection
        result = query_executor_fixture.insert_table(self.insert_1, self.para_1, self.insert_2, self.para_2)
        assert True == result
        mock_cursor.execute.assert_called()

    def test_insert_table_error(self, mock_database_connection, query_executor_fixture, caplog, capsys):
        mock_cursor = mock_database_connection
        mock_cursor.execute.side_effect = sqlite3.Error('Mock Error')
        query_executor_fixture.insert_table(self.insert_1, self.para_1, self.insert_2, self.para_2)
        captured = capsys.readouterr()
        assert 'Mock Error' in caplog.text
        assert 'UNEXPECTED' in captured.out

    def test_insert_table_integrity_error(self, mock_database_connection, query_executor_fixture, caplog, capsys):
        mock_cursor = mock_database_connection
        mock_cursor.execute.side_effect = sqlite3.IntegrityError('Mock Error')
        query_executor_fixture.insert_table(self.insert_1, self.para_1, self.insert_2, self.para_2)
        captured = capsys.readouterr()
        assert 'Mock Error' in caplog.text
        assert 'USER' in captured.out
