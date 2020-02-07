''' Database utility module. '''

import pyodbc

from datamegh.util.logging import get_logger


# Drivers
DRIVER_PG = '{PostgreSQL Unicode}'
DRIVER_MSSQL = '{ODBC Driver 17 for SQL Server}'

# Database Connections
PG: str = 'pg'
MSSQL: str = 'mssql'
MYSQL: str = 'mysql'

# Connection strings
CONN_STR: str = ';'.join([
    'DRIVER={driver}',
    'SERVER={server}',
    'PORT={port}',
    'DATABASE={database}',
    'UID={username}',
    'PWD={password}'
])

logger = get_logger('db')


def connect(**params) -> pyodbc.Connection:
    ''' Open connection to a Database. '''
    logger.debug('Connecting to database: {}/{}'.format(params.get('host'), params.get('database')))

    # Build a connection string. 
    connection_str = CONN_STR.format(
        driver=params['driver'],
        server=params['host'],
        database=params['database'],
        username=params['username'],
        password=params['password'],
        port=params.get('port')
    )

    return pyodbc.connect(connection_str)
