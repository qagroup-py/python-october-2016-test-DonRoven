def remove_duplicates(data):
    s = list(data)
    s1 = []
    for i in s:
        if i not in s1:
            s1.append(i)
    """
    Removes duplicate elements from given sequence:
    >>> remove_duplicates('abcdaefbg')
    ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    If mutable argument passed, it should remain unchanged:
    >>> data = [1, 2, 2, 3, 4, 2, 3, 5]
    >>> remove_duplicates(data)
    [1, 2, 3, 4, 5]
    >>> data
    [1, 2, 2, 3, 4, 2, 3, 5]

    Output should preserve order of first occurence in passed argument:
    >>> remove_duplicates('dcbacbd')
    ['d', 'c', 'b', 'a']
    >>> remove_duplicates([4, 8, 3, 2, 3, 8, 6, 4, 1])
    [4, 8, 3, 2, 6, 1]

    Args:
        data: sequence with possible duplicates

    Returns:
        List with all duplicates removed
    """
    return s1


def get_duplicates(data):
    d = list(data)
    dict1 = {}
    for i in d:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] +=1

    for i in d:
        if dict1[i] == 1:
            del(dict1[i])
    """
    Get all duplicates from given sequence along with duplicate count.
    >>> dups = get_duplicates([1, 2, 2, 3, 4, 3, 5, 6, 6, 2])
    >>> dups == {3: 2, 2: 3, 6: 2}
    True

    In case when no duplicates found, empty dict should be returned
    >>> get_duplicates('abcdefg')
    {}

    Args:
        data: sequence with possible duplicates

    Returns:
        Dictionary with duplicate values as keys, occurence count as values
    """
    return dict1

#print(get_duplicates([8, 8, 8, 8]))
# code below left for your own usage and can be deleted at will
# -------------------------------------------------------------
if __name__ == '__main__':
    # tests for this module lives in tests/test_duplicates.py
    import unittest
    unittest.main(module='test_duplicates')
