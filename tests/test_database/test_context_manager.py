import pytest
import sqlite3
from database.context_manager import DatabaseConnection

def test_database_connection():
    with DatabaseConnection(":memory:") as conn:
        assert conn is not None

def test_database_connection_class_error():
    with pytest.raises(sqlite3.Error):
        with DatabaseConnection(":memory:") as conn:
            raise sqlite3.Error
