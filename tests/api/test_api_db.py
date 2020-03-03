""" Tests for datamegh.api.db. """

import pytest

from mock import patch

from datamegh.api import db
from datamegh.util.db import PG


@patch("datamegh.api.db.pyodbc")
def test_connect(m_pyodbc):
    """
    Test it invokes pyodbc connect
    generating a connection string.
    """

    connection = db.connect(
        client=PG,
        port=5444,
        driver="SOME_OTHER_DRIVER",
        host="localhost",
        database="test",
        username="test",
        password="Test@123",
    )
    expected_connstr = "DRIVER=SOME_OTHER_DRIVER;SERVER=localhost;PORT=5444;DATABASE=test;UID=test;PWD=Test@123"
    m_pyodbc.connect.assert_called_once_with(expected_connstr)
