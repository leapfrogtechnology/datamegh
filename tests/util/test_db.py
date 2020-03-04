""" Tests for the db utility. """

import pytest

from datamegh.util.db import build_connstr, PG, MSSQL, MYSQL


def test_build_connstr_1():
    """ Test throws error if no client is provided. """

    with pytest.raises(
        RuntimeError, match="Database `client` must be provided to connect to."
    ):
        build_connstr()


def test_build_connstr_1():
    """ Test throws error if an unsupported client is provided. """

    with pytest.raises(RuntimeError, match='Unsupported database client type "abcdb".'):
        build_connstr(client="abcdb")


def test_build_connstr_3():
    """ Test it builds connection strings for supported clients. """

    connstr_mssql = build_connstr(
        client=MSSQL,
        host="localhost",
        database="test",
        username="test",
        password="Test@123",
    )

    assert (
        connstr_mssql
        == "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;PORT=1433;DATABASE=test;UID=test;PWD=Test@123"
    )

    connstr_pg = build_connstr(
        client=PG,
        host="localhost",
        database="test",
        username="test",
        password="Test@123",
    )

    assert (
        connstr_pg
        == "DRIVER={PostgreSQL Unicode};SERVER=localhost;PORT=5432;DATABASE=test;UID=test;PWD=Test@123"
    )

    connstr_mysql = build_connstr(
        client=MYSQL,
        host="localhost",
        database="test",
        username="test",
        password="Test@123",
    )

    assert (
        connstr_mysql
        == "DRIVER={MySQL ODBC 8.0 Driver};SERVER=localhost;PORT=3306;DATABASE=test;UID=test;PWD=Test@123"
    )


def test_build_connstr_4():
    """ Test it default values could be overwritten for supported clients. """

    connstr_mssql = build_connstr(
        client=MSSQL,
        port=1444,
        driver="SOME_OTHER_DRIVER",
        host="localhost",
        database="test",
        username="test",
        password="Test@123",
    )

    assert (
        connstr_mssql
        == "DRIVER=SOME_OTHER_DRIVER;SERVER=localhost;PORT=1444;DATABASE=test;UID=test;PWD=Test@123"
    )

    connstr_pg = build_connstr(
        client=PG,
        port=5444,
        driver="SOME_OTHER_DRIVER",
        host="localhost",
        database="test",
        username="test",
        password="Test@123",
    )

    assert (
        connstr_pg
        == "DRIVER=SOME_OTHER_DRIVER;SERVER=localhost;PORT=5444;DATABASE=test;UID=test;PWD=Test@123"
    )

    connstr_mysql = build_connstr(
        client=MYSQL,
        port=33066,
        driver="SOME_OTHER_DRIVER",
        host="localhost",
        database="test",
        username="test",
        password="Test@123",
    )

    assert (
        connstr_mysql
        == "DRIVER=SOME_OTHER_DRIVER;SERVER=localhost;PORT=33066;DATABASE=test;UID=test;PWD=Test@123"
    )
