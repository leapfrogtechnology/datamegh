import pytest

from datamegh.api import http

TEST_URL = "https://httpbin.org/"


def test_get():
    response = http.get(TEST_URL + "/get")
    assert response.ok == True


def test_get_param():
    payload = {"key1": "value1", "key2": "value2"}
    response = http.get(TEST_URL + "/get", params=payload)
    assert response.ok == True
    assert response.url == TEST_URL + "/get?key1=value1&key2=value2"


def test_get_dict_param():
    payload_dict = {"key1": "value1", "key2": ["value2", "value3"]}
    response = http.get(TEST_URL + "/get", params=payload_dict)
    assert response.ok == True
    assert response.url == TEST_URL + "/get?key1=value1&key2=value2&key2=value3"


def test_post():
    response = http.post(TEST_URL + "/post", data={"key": "value"})
    assert response.ok == True


def test_put():
    response = http.put(TEST_URL + "/put", data={"key": "value"})
    assert response.ok == True


def test_patch():
    response = http.patch(TEST_URL + "/patch", data={"key": "value"})
    assert response.ok == True


def test_delete():
    response = http.delete(TEST_URL + "/delete")
    assert response.ok == True


def test_head():
    response = http.head(TEST_URL + "/get")
    assert response.ok == True


def test_options():
    response = http.options(TEST_URL + "/get")
    assert response.ok == True
