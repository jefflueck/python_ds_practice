def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    new_list = [k for k in d]
    sorted_list = sorted(new_list)
    new_list = [sorted_list[0], sorted_list[-1]]
    tuple1 = tuple(new_list)
    return tuple1

