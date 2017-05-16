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
    (0, 1, 1, 0),
    (3 ,2 , 5, 12),
    (5,8,4,21),
    (9,7,6,62),
    (9,2,5,24)
]


@pytest.mark.parametrize('n, result', FIB_PARAMS)
def fib_test(n):
    """Tests to see if the Fibonacci nonsense returns the appropriate value."""
    from fib import fib
    assert fib(n) = result

@pytest.mark.parametrize('x,y,n,result',LUCA_PARMS)
def lucas_test(x,y,z):
    """Test the lucas function"""
    from fib import lucas
    assert lucas(x,y,n) =result

