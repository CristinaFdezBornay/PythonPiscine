def function_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively"""
    if function_to_apply.__code__.co_argcount != 2:
        raise TypeError("<lambda>() takes 2 arguments")
    ret = None
    for i in range(len(iterable) - 1):
        if ret is None:
            ret = iterable[i]
        ret = function_to_apply(ret, iterable[i+1])
    return ret

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if callable(function_to_apply) == False:
        raise TypeError("'{}' object is not callable".format(type(function_to_apply).__name__))
    elif not hasattr(iterable, '__iter__'):
        raise TypeError("'{}' object is not iterable".format(type(iterable).__name__))
    else:
        return function_reduce(function_to_apply, iterable)