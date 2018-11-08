#import numpy as np
#import Qconfig
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import available_backends, execute, register, least_busy
from qiskit.tools.visualization import plot_histogram, circuit_drawer
from functools import reduce

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

# initialize
backend = least_busy(available_backends({'simulator': True, 'local': True}))
quantumReg = QuantumRegister(3)
classicReg = ClassicalRegister(3)
quantumCirc = QuantumCircuit(quantumReg, classicReg)
# grab user prefs
roll_count = int(input("Number of rolls? (up to 8192): "))
#build the dice, according to entangled states or not
quantumCirc.h(quantumReg[0])
quantumCirc.h(quantumReg[1])
quantumCirc.h(quantumReg[2])
quantumCirc.measure(quantumReg[0], classicReg[0])
quantumCirc.measure(quantumReg[1], classicReg[1])
quantumCirc.measure(quantumReg[2], classicReg[2])
# run the quantumCirc and get result for dice
job = execute(quantumCirc, backend=backend, shots=roll_count)
counts = job.result().get_counts(quantumCirc)
print(counts)
rolls = counts.keys()
first_dice = []
second_dice = []
total_count = {}
total_probs = {}
for k in rolls:
    print("{0}".format(k))
    total = int(str(int(k, 2)), 10) + 1
    total_count[total] = counts[k]
    total_probs[total] = counts[k] / roll_count
print("Expected value: {0}".format(expected_value(total_probs.values(), total_probs.keys())))
print("Variance: {0}".format(variance(total_count.keys())))
graph = plot_histogram(total_count)