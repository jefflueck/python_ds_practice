from typing import Counter


def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!')
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    # c = Counter('aeiou')
    # d = Counter(phrase)

    # return dict(c[d])

    # solution
    phrase = phrase.lower()
    counter = {}

    for ltr in phrase:
        if ltr in 'aeiou':
            counter[ltr] = counter.get(ltr, 0) + 1

    return counter





