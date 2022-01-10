def compact(lst):
    for item in lst != int and str and float and True and False:
        return lst
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
