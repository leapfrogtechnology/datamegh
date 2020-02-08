''' Tests for the db utility. '''

import pytest
import logging

from mock import patch

from datamegh.util.db import connect, build_connstr, PG, MSSQL, MYSQL


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


def test_build_connstr_3():
    ''' Test it default values could be overwritten for supported clients. '''

    connstr_mssql = build_connstr(
        client=MSSQL,
        port=1444,
        driver='SOME_OTHER_DRIVER',
        host='localhost',
        database='test',
        username='test',
        password='Test@123'
    )

    assert connstr_mssql == 'DRIVER=SOME_OTHER_DRIVER;SERVER=localhost;PORT=1444;DATABASE=test;UID=test;PWD=Test@123'

    connstr_pg = build_connstr(
        client=PG,
        port=5444,
        driver='SOME_OTHER_DRIVER',
        host='localhost',
        database='test',
        username='test',
        password='Test@123'
    )

    assert connstr_pg == 'DRIVER=SOME_OTHER_DRIVER;SERVER=localhost;PORT=5444;DATABASE=test;UID=test;PWD=Test@123'

    # TODO: Add mysql


@patch('datamegh.util.db.pyodbc')
def test_connect(m_pyodbc):
    '''
    Test it invokes pyodbc connect 
    generating a connection string.
    '''

    connection = connect(
        client=PG,
        port=5444,
        driver='SOME_OTHER_DRIVER',
        host='localhost',
        database='test',
        username='test',
        password='Test@123'
    )
    expected_connstr = 'DRIVER=SOME_OTHER_DRIVER;SERVER=localhost;PORT=5444;DATABASE=test;UID=test;PWD=Test@123'
    m_pyodbc.connect.assert_called_once_with(expected_connstr)
