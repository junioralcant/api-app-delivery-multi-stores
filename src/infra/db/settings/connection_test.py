
import pytest
from .connection import DBConnectionHandler


@pytest.mark.skip(reason="Sensitive test")
def test_create_database_connection():
    db_connect_handle = DBConnectionHandler()

    engine = db_connect_handle.get_engine()

    assert engine is not None
