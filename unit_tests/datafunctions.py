"""Writing functions to work witth arrays and strings"""

import string
import numpy as np

def increment(x):
    """ads one to x"""
    return(x+1)


def strip_punctuation(text):
    """strips punctuation"""
    exclude = string.punctuation
    return ''.join(s for s in text if s not in exclude)


