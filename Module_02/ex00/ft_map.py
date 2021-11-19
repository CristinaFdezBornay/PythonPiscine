def function_map(function_to_apply, iterable):
    """
    Map the function to all elements of the iterable.
    """
    for i in iterable:
        yield function_to_apply(i)

def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if callable(function_to_apply) == False:
        raise TypeError("'{}' object is not callable".format(type(function_to_apply).__name__))
        return None
    elif not hasattr(iterable, '__iter__'):
        raise TypeError("'{}' object is not iterable".format(type(iterable).__name__))
        return None
    else:
        return function_map(function_to_apply, iterable)

