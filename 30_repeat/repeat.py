def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    # My first attempt
    # return phrase * num

    # My second attempt
    # if num == int:
    #    return phrase * num

    # My third attempt
    # if num == int:
    #     new_phrase = phrase * num
    #     return new_phrase

    # return None

    # Solution
    if not isinstance(num, int) or num < 0:
        return None

    return phrase * num
