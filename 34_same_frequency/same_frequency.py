def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    # Not sure what to do with this problem
    new_set1 = [n for n in num1]
    new_set2 = [n for n in num2]
    if new_set1 == new_set2:
        return True

    return False
