""" Datamegh package. """
from os import environ
from logging import INFO, DEBUG, ERROR, WARNING, CRITICAL


name = "datamegh"
version = "1.0.0-alpha.1"

log_level_map = {
    "info": INFO,
    "debug": DEBUG,
    "error": ERROR,
    "warning": WARNING,
    "critical": CRITICAL,
}
config: object = {
    "logging": {
        "level": log_level_map.get(environ.get("LOG_LEVEL", "debug")),
        "format": "%(asctime)s - [ %(levelname)s ] %(name)s - %(message)s",
    }
}
