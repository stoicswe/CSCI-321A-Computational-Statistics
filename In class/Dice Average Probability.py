import sys
import random

def e(x, p):
    sum = 0
    for i in len(x):
        sum += x[i] * p
    return sum