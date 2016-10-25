def sum_regular(data):
    """
    Sums all elements in passed sequence.
    You may assume that all elements in passed argument is numeric

    >>> sum_regular([3, 6, 9])
    18
    >>> sum_regular(range(10))
    45
    >>> sum_regular((8.2, 6.3, 13.1))
    27.6
    >>> sum_regular([])
    0

    Args:
        data: iterable or sequence with numbers

    Returns:
        Sum of all elements in passed args, as single number
    """
    return sum(list(data))


def multiply_regular(data):
    """
    Multiplies all elements in passed sequence.
    You may assume that all elements in passed argument is numeric.

    >>> multiply_regular([3, 6, 9])
    162
    >>> multiply_regular(range(10))
    0
    >>> multiply_regular(range(1, 10))
    362880
    >>> multiply_regular((8.2, 6.3, 13.1))
    676.746
    >>> multiply_regular(tuple())
    1

    Args:
        data: iterable or sequence with numbers

    Returns:
        Multiplication of all elements in passed args, as single number
    """
    d = list(data)
    if d == []:
        return 1
    else:
        r = d[0]
        i = 1
        while i < len(d):
            r *= d[i]
            i += 1
    return r


# code below left for your own usage and can be deleted at will
# -------------------------------------------------------------
if __name__ == '__main__':
    # tests for this module uses docstrings as source
#    import doctest
#    doctest.testmod(verbose=True)

    print (multiply_regular(tuple()))
