def function_filter(function_to_apply, iterable):
    """Filter result of function and apply it to all elements of the iterable"""
    for i in iterable:
        if function_to_apply(i) == True:
            yield i

def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if callable(function_to_apply) == False:
        raise TypeError("'{}' object is not callable".format(type(function_to_apply).__name__))
    elif not hasattr(iterable, '__iter__'):
        raise TypeError("'{}' object is not iterable".format(type(iterable).__name__))
    else:
        return function_filter(function_to_apply, iterable)