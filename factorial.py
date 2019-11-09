
"""
Count fac
>>> fac(5)
120
"""

import sys
import doctest


def fac(n: int):
    """
    Return factorial value.
    If the passed value is lower than zero or is not an instance of integer
    then ValueError is raised
    >>> fac(-1)
    Traceback (most recent call last):
        ...
    ValueError: Value of parameter must be greater or equal to zero
    >>> fac('Oh, hi Mark!')
    Traceback (most recent call last):
        ...
    ValueError: Unexpected type <class 'str'>
    """
    try:
        n = int(n)
    except ValueError:
        print(f'Unexpected type {type(n)}', file=sys.stderr)
        raise ValueError(f'Unexpected type {type(n)}')

    if n < 0:
        raise ValueError(f'Value of parameter must be greater or equal to zero')

    while n > 0:
        return n * fac(n-1)
    return 1


if __name__ == '__main__':
    doctest.testmod()
