def single_letter_count(word, letter):
    # My attempt works
    sum = 0
    for char in word:
        if char.lower(char) == letter.lower():
            sum + sum
            return sum

    # Solution
    # return word.lower().count(letter.lower())

    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """