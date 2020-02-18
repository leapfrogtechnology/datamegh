""" Tests for datamegh.util.object util. """

import pytest
from datamegh.util.object import linearize, delinearize, merge, dict_to_list, with_only


def test_dict_to_list_returns_list_when_valid_arguments_is_dict():
    """
    Test a dictionary converted to list.
    """
    value = {
        "foo": "bar",
        "just": "test",
        "hello": "world",
    }

    expected = [
        {"name": "foo", "value": "bar"},
        {"name": "just", "value": "test"},
        {"name": "hello", "value": "world"},
    ]

    assert dict_to_list(value) == expected


def test_dict_to_list_returns_empty_list_when_argument_is_empty_dict():
    """
    Test an empty dictionary converted to empty list.
    """
    assert dict_to_list({}) == []


def test_dict_to_list_raises_exception_when_argument_is_invalid():
    """
    Test an invalid argument such as int to dict_to_list
    """
    with pytest.raises(AttributeError) as ex:
        dict_to_list(1)

    assert (
        ex.value.args[0]
        == "Argument must be a dictionary, invalid argument received '1'."
    )


def test_linearize_1():
    """
    Test a flat / linear dictionary
    is returned as it is.
    """
    value = {
        "foo": "bar",
        "just": "test",
        "message": "Hello World!",
    }

    assert linearize(value) == value


def test_linearize_2():
    """
    Test an already linerized dictionary
    is returned as it is.
    """
    value = {
        "foo.bar": "Foo Bar",
        "just.test": "Just Test",
        "just.a.simple.message": "Hello World!",
        "array[0]": "First",
        "array[1]": "Second",
    }

    assert linearize(value) == value


def test_linearize_3():
    """
    Test it linearizes the nested dictionary.
    """
    value = {
        "foo": {"bar": "Foo Bar"},
        "just": {"test": "Just Test", "a": {"simple": {"message": "Hello World!"}}},
        "array": ["First", "Second"],
    }

    expected = {
        "foo.bar": "Foo Bar",
        "just.test": "Just Test",
        "just.a.simple.message": "Hello World!",
        "array.0": "First",
        "array.1": "Second",
    }

    assert linearize(value) == expected


def test_delinearize_1():
    """
    Test a regular flat dictionary returned as it is.
    """
    value = {
        "foo": "bar",
        "just": "test",
        "message": "Hello World!",
    }

    assert delinearize(value) == value


def test_delinearize_2():
    """
    Test it throws error if a
    non-flat / nested dictionary is provided.
    """
    value = {
        "foo": {"bar": "Foo Bar"},
        "just": {"test": "Just Test", "a": "b"},
        "array": ["First", "Second"],
    }

    with pytest.raises(AssertionError) as ex:
        delinearize(value)

    assert ex.value.args[0] == "provided dict is not flat"


def test_delinearize_3():
    """
    Test it delinearizes the linearized dictionary
    """
    value = {
        "foo.bar": "Foo Bar",
        "just.test": "Just Test",
        "just.a.simple.message": "Hello World!",
        "array.0": "First",
        "array.1": "Second",
    }

    expected = {
        "foo": {"bar": "Foo Bar"},
        "just": {"test": "Just Test", "a": {"simple": {"message": "Hello World!"}}},
        "array": ["First", "Second"],
    }

    assert delinearize(value) == expected


def test_delinearize_4():
    """
    Test it delinearizes an array.
    """
    value = {
        "array.0": "Test 1",
        "array.1": "Test 2",
        "array.2": "Test 3",
    }

    expected = {
        "array": ["Test 1", "Test 2", "Test 3"],
    }

    assert delinearize(value) == expected


def test_merge_v0():
    """
    Test for datamegh.util.merge()
    Assert expected merge outcome when no conflicting keys are present.
    """
    dict1 = {"key1": "value1", "key2": {"key3": "value3", "key4": "value4"}}

    dict2 = {"keyA": "valueA", "key2": {"keyB": "valueB", "keyC": {"foo": "bar"}}}

    expectedmerge = {
        "key1": "value1",
        "key2": {
            "keyB": "valueB",
            "key3": "value3",
            "key4": "value4",
            "keyC": {"foo": "bar"},
        },
        "keyA": "valueA",
    }

    merged = merge(dict1, dict2)

    assert merged == expectedmerge


def test_merge_v1():
    """
    Test for datamegh.util.merge()
    Assert that second dictionary overrides conflicting keys during merge
    """
    dict1 = {"key1": "value1", "key2": {"key3": "value3", "key4": "value4"}}

    dict2 = {"key1": "valueA", "key2": {"keyB": "valueB"}}

    expectedmerge = {
        "key1": "valueA",
        "key2": {"keyB": "valueB", "key3": "value3", "key4": "value4"},
    }

    merged = merge(dict1, dict2)

    assert merged == expectedmerge


def test_merge_v2():
    """
    Test merge() would show all the keys from the
    initial dict, but also overwrite all the keys
    found in both dict, even if the second value is
    provided empty i.e None.
    """
    merged = merge(
        {
            "foo": "bar",
            "bar": "foo",
            "baz": "Baz",
            "test": {
                "attr1": "Foo Bar",
                "attr2": "Hello World!",
                "attr3": ["value1", "value2"],
            },
        },
        {"foo": None, "bar": "Foo", "test": {"attr2": None, "attr3": ["1", "2"]}},
    )

    assert merged == {
        "foo": None,
        "bar": "Foo",
        "baz": "Baz",
        "test": {"attr1": "Foo Bar", "attr2": None, "attr3": ["1", "2"]},
    }


def test_with_only_returns_dictionary_when_both_src_and_attrs_are_valid_arguments():
    """
    Test datamegh.util.with_only() would return a dictionary when a valid source
    and attrs are provided to it
    """

    assert with_only({"key1": "value1", "key2": "value2"}, ["key1"]) == {
        "key1": "value1"
    }


def test_with_only_returns_empty_dictionary_when_attrs_is_empty():
    """
    Test datamegh.util.with_only() would return an empty dictionary when empty attrs
    list is provided to it.
    """

    assert with_only({"key1": "value1", "key2": "value2"}, []) == {}


def test_with_only_raises_attribute_error_when_first_argument_is_not_dictionary():
    """
    Test datamegh.util.with_only() would return an Attribute error when src is an invalid
    argument.
    """

    with pytest.raises(AttributeError) as ex:
        with_only(1, [])

    assert (
        ex.value.args[0]
        == "First argument must be a dictionary, invalid argument received '1'."
    )


def test_with_only_raises_attribute_error_when_second_argument_is_not_list():
    """
    Test datamegh.util.with_only() would return an Attribute error when attrs is an invalid
    argument.
    """

    with pytest.raises(AttributeError) as ex:
        with_only({}, 1)

    assert (
        ex.value.args[0]
        == "Second argument must be a list, invalid argument received '1'."
    )


def test_with_only_raises_type_error_when_first_argument_is_not_dictionary():
    """
    Test datamegh.util.with_only() would return an Attribute error when no arguments
    are provided to it.
    """

    with pytest.raises(TypeError) as ex:
        with_only()

    assert (
        ex.value.args[0]
        == "with_only() missing 2 required positional arguments: 'src' and 'attrs'"
    )
