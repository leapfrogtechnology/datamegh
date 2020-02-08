''' Tests for the db utility. '''

import pytest
import logging

from datamegh.util.db import build_connstr, PG, MSSQL, MYSQL


def test_build_connstr_1():
    ''' Test throws error if no client is provided. '''

    with pytest.raises(RuntimeError, match='Database `client` must be provided to connect to.'):
        connstr = build_connstr()


def test_build_connstr_1():
    ''' Test throws error if an unsupported client is provided. '''

    with pytest.raises(RuntimeError, match='Unsupported database client type "abcdb".'):
        connstr = build_connstr(client='abcdb')


def test_build_connstr_3():
    ''' Test it builds connection strings for supported clients. '''

    connstr_mssql = build_connstr(
        client=MSSQL,
        host='localhost',
        database='test',
        username='test',
        password='Test@123'
    )

    assert connstr_mssql == 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;PORT=1433;DATABASE=test;UID=test;PWD=Test@123'

    connstr_pg = build_connstr(
        client=PG,
        host='localhost',
        database='test',
        username='test',
        password='Test@123'
    )

    assert connstr_pg == 'DRIVER={PostgreSQL Unicode};SERVER=localhost;PORT=5432;DATABASE=test;UID=test;PWD=Test@123'

    # TODO: Add mysql
