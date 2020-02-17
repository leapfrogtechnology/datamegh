""" File system utilities. """

import os
from glob import glob


def read(filename):
    """ Read contents of file and return it. """
    with open(filename, "r") as f:
        return f.read()


def write(filename, data):
    """ Write data to the file. """
    with open(filename, "w") as f:
        f.write(data)


def exists(path):
    """ Check if file path exists. """
    return os.path.exists(path)


def glob_all(paths):
    """ Get a list of all files from the given list of paths. """
    files = []

    for path in paths:
        files += glob(path)

    return files
