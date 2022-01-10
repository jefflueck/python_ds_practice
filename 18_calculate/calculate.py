def calculate(operation, a, b, make_int=False, message='The solution to your problem = '):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == 'divide':
        result = a / b
    elif operation == 'multiply':
        result = a * b
    # Solution
    # Can we go over, confused.
    else:
        # ! This return is indented inside the def so program continues until the second return that lines up with the def of the program. VERY IMPROTANT!!
        return
    # We move on in the program if these above conditions are not meet and more parameters are passed in.
    if make_int:
        result = round(result)
    # End of Solution code
    return f'{message}{result}'
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)

    """
