""" Database connection API. """

import pyodbc

from datamegh.util.object import merge
from datamegh.util.db import build_connstr

from datamegh.api.logging import get_logger

logger = get_logger("datamegh.api.db")


def connect(**params) -> pyodbc.Connection:
    """ Open connection to a Database. """
    logger.debug(
        "Connecting to database: {}/{}".format(
            params.get("host"), params.get("database")
        )
    )

    connstr = build_connstr(**params)

    return pyodbc.connect(connstr)
