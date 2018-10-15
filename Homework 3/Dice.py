import numpy as np
import random

# probability:
# #_of_fav_occurences / total_number_occurances

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

p = [1/36,2/36,3/36,4/36,5/36,6/36,5/35,4/36,3/36,2/36,1/36]
x = [2,3,4,5,6,7,8,9,10,11,12]

print("2 dice combos:")
print(x)
print("Probs for combos:")
print(p)
print("Expected value:")
print(expected_value(p,x))
print("Variance:")
print(variance(x))
print("Simulating dice rolls...")
tc = {}
rolls = 1000000
print("Rolling {0} times...".format(rolls))
for i in range(0,rolls):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    total = d1 + d2
    if total in tc:
        tc[total] += 1
    else:
        tc[total] = 1
print("Values recieved:")
print(tc)
print("Probs for each:")
ck = tc.keys()
for c in ck:
    tc[c] = tc[c] / rolls
print(tc)
combos = list(tc.keys())
probs = list(tc.values())
print("Expected value:")
print(expected_value(probs, combos))
print("Variance:")
print(variance(combos))