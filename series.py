"""Doc strings everywhere."""


def fib(n):
    """For any n, return its zero-index Fibonacci sequence."""
    if type(n) == int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    else:
        return 'Please use an integer greater than 0.'


def lucas(n):
    """For any n, return its zero-index Lucas sequence."""
    if type(n) == int:
        if n == 1:
            return 2
        elif n == 2:
            return 1
        else:
            return lucas(n - 1) + lucas(n - 2)
    else:
        return 'Please use an integer greater than 0.'


def sum_series(n, x=0, y=1):
    """Find the number in the lucas sequnce."""
    if type(n) == int:
        if (n == 1):
            return x
        elif (n == 2):
            return y
        else:
            return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)
    else:
        return 'Please use an integer greater than 0.'

if __name__ == "__main__":
    print(fib(6))
    print(lucas(4))
    print(sum_series(8))
    print(sum_series(9, 3, 3))
