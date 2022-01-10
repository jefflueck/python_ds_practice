def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.

        >>> triple_and_filter([1, 2, 3, 4])
        [12]

        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]

        >>> triple_and_filter([1, 2])
        []
    """
    # My attempt
    # tripled = [x * 3 for x in nums]
    # tripled_filter = [x % 4 == 0 for x in tripled]
    # return tripled_filter

    return [num * 3 for num in nums if num % 4 == 0]


