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
    (0, 1, 1),
    (),
    (),
    (),
    ()
]


@pytest.mark.parametrize('n, result', FIB_PARAMS)
def fib_test(n):
    """Tests to see if the Fibonacci nonsense returns the appropriate value."""
    from fib import fib
    assert fib(n) = result

