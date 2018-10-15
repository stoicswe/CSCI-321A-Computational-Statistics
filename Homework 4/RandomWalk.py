import numpy
import math
import random
import collections
import matplotlib.pylab as plt
from collections import defaultdict

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

def square(list):
    return [i ** 2 for i in list]

n_steps = int(input("Enter the number of steps to walk: "))
sim = int(input("How many simulations to run? (the more sims, the more accurate it gets) "))
if sim <= 0:
    sim = 1000
counts = defaultdict(int)
for s in range(sim):
    c_pos = 0
    for n in range(n_steps):
        #print("Step {3}: {1}|{0}|{2}".format(c_pos, c_pos-1, c_pos+1, n))
        direction = random.randint(0, 1)
        #print("Choosing direction: {0}".format(direction))
        if direction == 0:
            c_pos -= 1
            counts[c_pos] += 1
        else:
            c_pos += 1
            counts[c_pos] += 1
#calculate the average, variance, expected value
av = sum(counts.keys()) / len(counts.keys())
events = list(counts.values())
total_events = n_steps * sim
probs = [ev / total_events for ev in events]
vals = list(counts.keys())
vals_squared = square(list(counts.keys()))
print("Average: {0}".format(av))
print("Variance: {0}".format(variance(vals)))
print("Expected Value: {0}".format(expected_value(probs, vals)))
keys = list(counts.keys())
keys.sort()
print("{0: <5}   {1: <5}   {2: <5}".format("Step","Count","Probability"))
print("--------------------------------------------")
for k in keys:
    print("{0: <5}   {1: <5}   {2: <5}".format(k, counts[k], (counts[k]/total_events)))
plt.bar(counts.keys(), counts.values())
plt.show()