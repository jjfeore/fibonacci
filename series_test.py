"""Go away linter."""


import pytest


FIB_PARAMS = [
    (4, 3),
    (5, 5),
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2)
]


LUCAS_PARAMS = [
    (0, 2),
    (1, 1),
    (6, 18),
    (3, 4),
    (8, 47)
]


SUM_PARAMS = [
    (4, 3),
    (5, 5),
    (0, 0),
    (1, 0, 1, 0),
    (5, 3, 2, 12),
    (4, 5, 8, 21),
    (6, 9, 7, 62),
    (5, 9, 2, 24)
]


@pytest.mark.parametrize('n, result', FIB_PARAMS)
def fib_test(n, result):
    """Test to see if the Fibonacci nonsense returns the appropriate value."""
    from fib import fib
    assert fib(n) == result


@pytest.mark.parametrize('n, result', LUCAS_PARAMS)
def lucas_test(n, result):
    """Test to see if the Lucas nonsense returns the appropriate value."""
    from fib import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n,result,x,y', SUM_PARAMS)
def sum_series_test(n, result, x=0, y=1):
    """Test the sum_series function."""
    from fib import sum_series
    assert sum_series(n, x, y) == result
