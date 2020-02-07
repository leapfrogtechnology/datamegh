''' Tests for datamegh.util.types. '''

from datamegh.util.types import (
    is_iterable,
    is_string,
    is_dict,
    is_list
)


def test_is_iterable_1():
    ''' Simple cases for is_iterable() '''
    def noop():
        pass

    assert is_iterable([]) is True
    assert is_iterable({}) is True
    assert is_iterable('random string') is True

    assert is_iterable(1) is False
    assert is_iterable(-5) is False
    assert is_iterable(0) is False
    assert is_iterable(noop) is False
    assert is_iterable(None) is False


def test_is_iterable_2():
    '''
    Other cases for is_iterable()
    Any construct that adheres to the iterator protocol should return True
    '''
    gen = (n for n in range(0, 10))

    assert is_iterable(gen) is True


def test_is_string_1():
    ''' Case 1 - positive; returns True for all possible values. '''
    assert is_string('') is True
    assert is_string('Foo') is True
    assert is_string(r'Foo') is True
    assert is_string("Bar") is True
    assert is_string(r"Bar") is True
    assert is_string(u"Hello") is True
    assert is_string(str(1)) is True
    assert is_string(str(False)) is True
    assert is_string(str(None)) is True


def test_is_string_2():
    ''' Case 1 - negative; returns True for all possible values. '''
    assert is_string(True) is False
    assert is_string(None) is False
    assert is_string(0) is False
    assert is_string(-1) is False
    assert is_string([]) is False
    assert is_string({}) is False


def test_is_dict_returns_true_for_a_valid_arguments_of_dict_data_type():
    ''' Test is_dict() for valid arguments of dict data type. '''
    assert is_dict({}) is True
    assert is_dict({'foo': 'bar'}) is True
    assert is_dict(dict()) is True


def test_is_dict_returns_false_for_arguments_other_than_a_dict():
    ''' Test is_dict() for valid arguments of other than dict data type. '''
    assert is_dict('') is False
    assert is_dict('Test') is False
    assert is_dict(u'Hello') is False
    assert is_dict(None) is False
    assert is_dict([]) is False


def test_is_list_returns_true_for_a_valid_arguments_of_list_data_type():
    ''' Test is_list() for valid arguments of list data type. '''
    assert is_list([]) is True
    assert is_list(list()) is True
    assert is_list(['apple', 'ball', 'cat']) is True
    assert is_list(['1', '2', '3']) is True


def test_is_list_returns_false_for_arguments_other_than_a_list():
    ''' Test is_list() for valid arguments of other than list data type. '''
    assert is_list('') is False
    assert is_list('Test') is False
    assert is_list(u'Hello') is False
    assert is_list(None) is False
    assert is_list({}) is False
    assert is_list({'foo': 'bar'}) is False
    assert is_list(dict()) is False
