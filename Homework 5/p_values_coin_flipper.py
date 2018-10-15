import math
import random

def count_extreme_values(flips = 1000, theta = 0, factor = 1):
    extreme_value_count = 0
    for _ in range(1000):
        num_heads = sum(1 if random.random() < 0.5 else 0     # count # of heads
                        for _ in range(flips))                # in 1000 flips
        num_heads += theta
        if num_heads >= 530/factor or num_heads <= 470/factor:# and count how often
            extreme_value_count += 1                          # the # is 'extreme'

    return extreme_value_count / 1000

print("P Vals for 1000 flips with unfair coin (first is fair):")
pvals_1000 = []
for i in range(100):
    pvals_1000.append(count_extreme_values(1000, i))
print(pvals_1000)

print("P Vals for 100 flips with unfair coin (first is fair):")
pvals_100 = []
for i in range(10):
    pvals_100.append(count_extreme_values(100, i, 10))
print(pvals_100)

print("P Vals for 10 flips with unfair coin (first is fair):")
pvals_10 = []
for i in range(5):
    pvals_10.append(count_extreme_values(10, i, 100))
print(pvals_10)