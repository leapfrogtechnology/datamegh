""" Basic HTTP verbs for your API connection. """

import requests


def get(url, params=None, **kwargs):
    response = requests.get(url, params, **kwargs)
    return response


def options(url, **kwargs):
    response = requests.options(url, **kwargs)
    return response


def head(url, **kwargs):
    response = requests.head(url, **kwargs)
    return response


def post(url, data=None, json=None, **kwargs):
    response = requests.post(url, data, json, **kwargs)
    return response


def put(url, data=None, **kwargs):
    response = requests.put(url, data, **kwargs)
    return response


def patch(url, data=None, **kwargs):
    response = requests.patch(url, data, **kwargs)
    return response


def delete(url, **kwargs):
    response = requests.delete(url, **kwargs)
    return response
