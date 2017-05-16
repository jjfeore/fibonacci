def fib(n):
    """For any n, return its zero-index Fibonacci sequence."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def lucas(x,y,n):
    """ finds the number in the lucas sequnce"""
    if ( n == 1):
        return x
    elif ( n == 2):
        return y
    n = n -2
    temp = 0
    for z in range(n):
        temp = x + y
        x = y
        y = temp
    return temp

