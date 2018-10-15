import numpy as np
import random

expected_value_lambda = lambda n : n*7/2
variance_lambda = lambda n : 35/12

def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v,v)

def mean(x):
    return sum(x) / len(x)

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / n

def expected_value(p, x):
    return sum([pi * xi for pi, xi in zip(p,x)])

dice_count = int(input("How many dice? "))
roll_count = int(input("Number of rolls? "))

print("Expected value (calculated):")
print(expected_value_lambda(dice_count))
print("Variance (calculated):")
print(variance_lambda(dice_count))
print("Simulating the rolling of {0} dice...".format(dice_count))
print("Rolling {0} times...".format(roll_count))

tc = {}
for i in range(roll_count):
    total = 0
    for k in range(dice_count):
        total += random.randint(1,6)
    if total in tc:
        tc[total] += 1
    else:
        tc[total] = 1

print("Values recieved:")
print(tc)
print("Probs for each:")
ck = tc.keys()
for c in ck:
    tc[c] = tc[c] / roll_count
print(tc)
combos = list(tc.keys())
probs = list(tc.values())
print("Expected value:")
print(expected_value(probs, combos))
print("Variance:")
print(variance(combos))