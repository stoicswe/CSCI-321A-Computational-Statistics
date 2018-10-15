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

sim = int(input("How many simulations to run? "))
if sim <= 0:
    sim = 100
counts = defaultdict(int)
a = 0
b = 0
aa = 0
bb = 0
for s in range(sim):
    a = random.randint(-1,1)
    b = random.randint(-1,1)
    aa = random.randint(-1,1)
    bb = random.randint(-1,1)
    f = abs(a*(b-bb) + aa*(b+bb))
    #f = a*(b-bb) + aa*(b+bb)
    counts[f] += 1
#calculate the average, variance, expected value
av = sum(counts.keys()) / len(counts.keys())
events = list(counts.values())
total_events = sim
probs = [ev / total_events for ev in events]
vals = list(counts.keys())
vals_squared = square(list(counts.keys()))
print("Average: {0}".format(av))
print("Variance: {0}".format(variance(vals)))
print("Expected Value: +-{0}".format(expected_value(probs, vals)))
plt.bar(counts.keys(), counts.values())
plt.show()