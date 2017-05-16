"""Doc strings everywhere."""


def fib(n):
    """For any n, return its zero-index Fibonacci sequence."""
    if type(n) == int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    else:
        return 'Please use an integer.'


def lucas(n):
    """For any n, return its zero-index Fibonacci sequence."""
    if type(n) == int:
        if n <= 0:
            return 2
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    else:
        return 'Please use an integer.'


def sum_series(n, x=0, y=1):
    """Find the number in the lucas sequnce."""
    if type(n) == int:
        if (n == 0):
            return x
        elif (n == 1):
            return y
        else:
            return sum_series(n - 1) + sum_series(n - 2)
    else:
        return 'Please use integers.'
