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

def get_dic(arr):
    d = {}
    for v in arr:
        if v in d:
            d[v] += 1
        else:
            d[v] = 1
    return d

def get_probs(dic, c):
    ks = dic.keys()
    for k in ks:
        dic[k] = dic[k] / c
    return dic

def expected_value(p, x):
    return sum([pi * xi for pi, xi in zip(p,x)])

titanic_data = genfromtxt('titanic.csv', delimiter=',')
#print(titanic_data)
#suv_pcla = correlation(titanic_data[:,0], titanic_data[:,1])
survival = titanic_data[:,0]
pclass = titanic_data[:,1]
sex = titanic_data[:,3]
payment = titanic_data[:,7]
total_events = len(survival)
#----------------------------
payment_c1 = []
payment_c2 = []
payment_c3 = []
for i in range(len(payment)):
    if pclass[i] == 1:
        payment_c1.append(payment[i])
    elif pclass[i] == 2:
        payment_c2.append(payment[i])
    elif pclass[i] == 3:
        payment_c3.append(payment[i])
#----------------------------
survivald = get_dic(survival)
pclassd = get_dic(pclass)
sexd = get_dic(sex)
paymentd = get_dic(payment)
#---------------------------
survival_probs = get_probs(survivald, total_events)
pclass_probs = get_probs(pclassd, total_events)
sex_probs = get_probs(sexd, total_events)
payment_probs = get_probs(paymentd, total_events)
payment_c1_probs = []
payment_c2_probs = []
payment_c3_probs = []
for i in range(len(payment_c1)):
    payment_c1_probs.append(pclass_probs[1] / len(payment_c1))
for i in range(len(payment_c2)):
    payment_c2_probs.append(pclass_probs[2] / len(payment_c2))
for i in range(len(payment_c3)):
    payment_c3_probs.append(pclass_probs[3] / len(payment_c3))
#----------------------------------------------------
print(survival_probs)
print(sex_probs)
print(pclass_probs)
print(sex_probs[0])
print(sex_probs[1])
sm1 = sex_probs[0]*pclass_probs[1]
sm2 = sex_probs[0]*pclass_probs[2]
sm3 = sex_probs[0]*pclass_probs[3]
sf1 = sex_probs[1]*pclass_probs[1]
sf2 = sex_probs[1]*pclass_probs[2]
sf3 = sex_probs[1]*pclass_probs[3]
print("P(S = True | G = male, c = 1) = {0}".format(sm1))
print("P(S = True | G = male, c = 2) = {0}".format(sm2))
print("P(S = True | G = male, c = 3) = {0}".format(sm3))
print("P(S = True | G = female, c = 1) = {0}".format(sf1))
print("P(S = True | G = female, c = 2) = {0}".format(sf2))
print("P(S = True | G = female, c = 3) = {0}".format(sf3))
#---------------------------------------------------------
ec1p = expected_value(payment_c1_probs, payment_c1)
ec2p = expected_value(payment_c2_probs, payment_c2)
ec3p = expected_value(payment_c3_probs, payment_c3)
print("Expected Payment for Class 1: {0}".format(ec1p))
print("Expected Payment for Class 2: {0}".format(ec2p))
print("Expected Payment for Class 3: {0}".format(ec3p))