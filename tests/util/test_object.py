''' Tests for datamegh.util.object util. '''

import pytest
from datamegh.util.object import linearize, delinearize, merge


def test_linearize_1():
    '''
    Test a flat / linear dictionary
    is returned as it is.
    '''
    value = {
        'foo': 'bar',
        'just': 'test',
        'message': 'Hello World!',
    }

    assert linearize(value) == value


def test_linearize_2():
    '''
    Test an already linerized dictionary
    is returned as it is.
    '''
    value = {
        'foo.bar': 'Foo Bar',
        'just.test': 'Just Test',
        'just.a.simple.message': 'Hello World!',
        'array[0]': 'First',
        'array[1]': 'Second',
    }

    assert linearize(value) == value


def test_linearize_3():
    '''
    Test it linearizes the nested dictionary.
    '''
    value = {
        'foo': {'bar': 'Foo Bar'},
        'just': {
            'test': 'Just Test',
            'a': {
                'simple':
                {
                    'message':
                    'Hello World!'
                }
            }
        },
        'array': ['First', 'Second'],
    }

    expected = {
        'foo.bar': 'Foo Bar',
        'just.test': 'Just Test',
        'just.a.simple.message': 'Hello World!',
        'array.0': 'First',
        'array.1': 'Second',
    }

    assert linearize(value) == expected


def test_delinearize_1():
    '''
    Test a regular flat dictionary returned as it is.
    '''
    value = {
        'foo': 'bar',
        'just': 'test',
        'message': 'Hello World!',
    }

    assert delinearize(value) == value


def test_delinearize_2():
    '''
    Test it throws error if a
    non-flat / nested dictionary is provided.
    '''
    value = {
        'foo': {'bar': 'Foo Bar'},
        'just': {
            'test': 'Just Test',
            'a': 'b'
        },
        'array': ['First', 'Second'],
    }

    with pytest.raises(AssertionError) as ex:
        delinearize(value)

    assert ex.value.args[0] == "provided dictionary is not flat"


def test_delinearize_3():
    '''
    Test it delinearizes the linearized dictionary
    '''
    value = {
        'foo.bar': 'Foo Bar',
        'just.test': 'Just Test',
        'just.a.simple.message': 'Hello World!',
        'array.0': 'First',
        'array.1': 'Second',
    }

    expected = {
        'foo': {'bar': 'Foo Bar'},
        'just': {
            'test': 'Just Test',
            'a': {
                'simple':
                {
                    'message':
                    'Hello World!'
                }
            }
        },
        'array': ['First', 'Second'],
    }

    assert delinearize(value) == expected


def test_delinearize_4():
    '''
    Test it delinearizes an array.
    '''
    value = {
        'array.0': 'Test 1',
        'array.1': 'Test 2',
        'array.2': 'Test 3',
    }

    expected = {
        'array': ['Test 1', 'Test 2', 'Test 3'],
    }

    assert delinearize(value) == expected


def test_merge_v0():
    '''
    Test for datamegh.util.merge()
    Assert expected merge outcome when no conflicting keys are present.
    '''
    dict1 = {
        'key1': 'value1',
        'key2': {
            'key3': 'value3',
            'key4': 'value4'
        }
    }

    dict2 = {
        'keyA': 'valueA',
        'key2': {
            'keyB': 'valueB',
            'keyC': {
                'foo': 'bar'
            }
        }
    }

    expectedmerge = {
        'key1': 'value1',
        'key2': {
            'keyB': 'valueB',
            'key3': 'value3',
            'key4': 'value4',
            'keyC': {
                'foo': 'bar'
            }
        },
        'keyA': 'valueA'
    }

    merged = merge(dict1, dict2)

    assert merged == expectedmerge


def test_merge_v1():
    '''
    Test for datamegh.util.merge()
    Assert that second dictionary overrides conflicting keys during merge
    '''
    dict1 = {
        'key1': 'value1',
        'key2': {
            'key3': 'value3',
            'key4': 'value4'
        }
    }

    dict2 = {
        'key1': 'valueA',
        'key2': {
            'keyB': 'valueB'
        }
    }

    expectedmerge = {
        'key1': 'valueA',
        'key2': {
            'keyB': 'valueB',
            'key3': 'value3',
            'key4': 'value4'
        },
    }

    merged = merge(dict1, dict2)

    assert merged == expectedmerge


def test_merge_v2():
    '''
    Test merge() would show all the keys from the 
    initial dict, but also overwrite all the keys
    found in both dict, even if the second value is
    provided empty i.e None.
    '''
    merged = merge({
        'foo': 'bar',
        'bar': 'foo',
        'baz': 'Baz',
        'test': {
            'attr1': 'Foo Bar',
            'attr2': 'Hello World!',
            'attr3': ['value1', 'value2']
        }
    }, {
        'foo': None,
        'bar': 'Foo',
        'test': {
            'attr2': None,
            'attr3': ['1', '2']
        }
    })

    assert merged == {
        'foo': None,
        'bar': 'Foo',
        'baz': 'Baz',
        'test': {
            'attr1': 'Foo Bar',
            'attr2': None,
            'attr3': ['1', '2']
        }
    }
