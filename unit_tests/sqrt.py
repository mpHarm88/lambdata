"""
Unit Tests

"""

import numpy as np

def sqrt_np(x):
    return np.sqrt(x)

def lazy_sqrt(x):
    """simplest way to do a square root"""
    return x**0.5

def builtin_sqrt(x):
    """use the math library to get the square root"""
    from math import sqrt
    return sqrt(x)

def newton_sqrt(x):
    """uses the Newton method to return dquare root"""
    val = x 
    while True:
        last = val
        val = (val + x/val)
        if abs(val-last) < 1e-9:
            break
    return val


