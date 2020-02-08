''' Database utility module. '''

import pyodbc

from datamegh.util.object import merge
from datamegh.util.logging import get_logger

# Database connection types
PG: str = 'pg'
MSSQL: str = 'mssql'
MYSQL: str = 'mysql'

# Drivers
DRIVER_PG = '{PostgreSQL Unicode}'
DRIVER_MSSQL = '{ODBC Driver 17 for SQL Server}'

# Defaults
DEFAULTS = {}
DEFAULTS[PG] = {
    'driver': DRIVER_PG,
    'port': '5432'
}
DEFAULTS[MSSQL] = {
    'driver': DRIVER_MSSQL,
    'port': '1433'
}
DEFAULTS[MYSQL] = {
    'driver': None, # TODO: Add MySQL driver.
    'port': '3306'
}

# Connection strings
CONN_STR: str = ';'.join([
    'DRIVER={driver}',
    'SERVER={host}',
    'PORT={port}',
    'DATABASE={database}',
    'UID={username}',
    'PWD={password}'
])

logger = get_logger('db')


def build_connstr(**args) -> str:
    ''' Build commection string from the received parameters. '''
    # Database client type to connect.
    client = args.get('client')

    if not client:
        raise RuntimeError('Database `client` must be provided to connect to.')
    
    defaults = DEFAULTS.get(client)

    if not defaults:
        raise RuntimeError('Unsupported database client type "{}".'.format(client))

    params = merge(defaults, args)

    connstr = CONN_STR.format(**params)

    return connstr


def connect(**params) -> pyodbc.Connection:
    ''' Open connection to a Database. '''
    logger.debug('Connecting to database: {}/{}'.format(params.get('host'), params.get('database')))

    connstr = build_connstr(**params)

    return pyodbc.connect(connstr)
