"""Go away linter."""


import pytest


FIB_PARAMS = [
    (4, 2),
    (5, 3),
    (1, 0),
    (2, 1),
    (3, 1)
]


LUCAS_PARAMS = [
    (1, 2),
    (6, 11),
    (3, 3),
    (8, 29)
]


SUM_PARAMS = [
    (4, 2, 0, 1),
    (5, 3, 0, 1),
    (1, 1, 1, 0),
    (6, 66, 2, 12),
    (5, 79, 8, 21),
    (7, 531, 7, 62),
    (6, 126, 2, 24)
]


@pytest.mark.parametrize('n, result', FIB_PARAMS)
def test_fib(n, result):
    """Test to see if the Fibonacci nonsense returns the appropriate value."""
    from series import fib
    assert fib(n) == result


@pytest.mark.parametrize('n, result', LUCAS_PARAMS)
def test_lucas(n, result):
    """Test to see if the Lucas nonsense returns the appropriate value."""
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n,result,x,y', SUM_PARAMS)
def test_sum_series(n, result, x, y):
    """Test the sum_series function."""
    from series import sum_series
    assert sum_series(n, x, y) == result
