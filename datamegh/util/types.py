""" Type utility functions. """


def is_string(obj):
    """ Check if the object is a string. """
    try:
        basestring
    except NameError:
        basestring = str

    return isinstance(obj, basestring)


def is_iterable(obj):
    """ Check if the object is iterable. """
    has_iter = hasattr(obj, "__iter__")
    has_get_item = hasattr(obj, "__getitem__")

    return has_iter or has_get_item


def is_dict(obj):
    """ Check if the object is a dict. """
    return type(obj) == type({})


def is_list(value):
    """ Check if the given value is a list. """
    return isinstance(value, list)
