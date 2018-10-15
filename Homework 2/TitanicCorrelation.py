import numpy as np
import csv
import collections
import math

from numpy import genfromtxt

def dot(v, w):
    return sum(v_i*w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v):
    return sum(v_i ** 2 for v_i in v)

def mean(x):
    return sum(x) / len(x)

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n%2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

#def mode(x):
#    counts = collections.Counter(x)
#    max_count = max(counts.values())
#    return [x_i for x_i, count in counts.iteritems() if count == max_count]

def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0
    
def column(matrix, i):
    return [row[i] for row in matrix]

#==========================================================
#in order to complete this homework, we will have to separate
#each row by ',' to individual columns. Then, we will have to
#convert non-numerical values to numbers, then we can calculate
#the correlation between different columns.

titanic_data = genfromtxt('titanic.csv', delimiter=',')
print(titanic_data)
print("Survival rate vs PClass:")
suv_pcla = correlation(titanic_data[:,0], titanic_data[:,1])
print(suv_pcla)
print("Survival vs Gender:")
suv_gen = correlation(titanic_data[:,0], titanic_data[:,3])
print(suv_gen)
print("Survival vs Spuses Aboard:")
suv_spa = correlation(titanic_data[:,0], titanic_data[:,4])
print(suv_spa)

if(suv_pcla > suv_gen):
    if(suv_gen > suv_spa):
        print("Survival rate vs PClass is the highest correlation.")
    else:
        print("Survival vs Spuses Aboard is the highest correlation.")
elif(suv_gen > suv_pcla):
    print("Survival vs Gender is the highest correlation.")
else:
    print("Survival vs Spuses Aboard is the highest correlation.")

""" with open('titanic.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'{", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{" ".join(row)}')
            line_count += 1
    print(f'Processed {line_count} lines.') """