import numpy as np
import random

def expected_value(p, x):
    return sum([pi * xi for pi, xi in zip(p,x)])

transition_matrix = [ [0.5,0.35,0.15,0.], [0.,0.,0.2,0.8], [0.,0.,0.3,0.7], [1.0,0.,0.,0.]]
state_vector = [0.,1.0,0.,0.]
super_position_state = np.dot(state_vector, transition_matrix)

def get_next_state(super_position_state):
    weight_precision = 1000
    weight_sum = sum(super_position_state)
    weighted_state = map(lambda e: e * weight_precision / weight_sum, super_position_state)

    state_list = []
    i = 0
    for item in weighted_state:
        state_list += [ i ] * int(item) 
        i += 1
         
    new_state = [0.] * len(super_position_state)
    new_state[random.choice(state_list)] = 1.0
     
    return new_state

state_vector = get_next_state(super_position_state)

def get_state(state_vector):
    index = [i for i, e in enumerate(state_vector) if e != 0]
    return 'S' + str(index[0])

posCounts = {}
steps = 100
for i in range(steps):
    super_position_state = np.dot(state_vector, transition_matrix)
    state_vector = get_next_state(super_position_state)
    print(state_vector, ':', get_state(state_vector))
    s = get_state(state_vector)
    if s in posCounts.keys():
        posCounts[s] += 1
    else:
        posCounts[s] = 1
posCountsK = posCounts.keys()
for k in posCountsK:
    posCounts[k] = posCounts[k] / steps
lbls = []
lbl = 0
for k in posCountsK:
    lbls.append(lbl)
    lbl += 1
posCountsK = list(posCountsK)
#print(expected_value(posCounts.values(), lbls))
print("The expected value is state: {0}".format(posCountsK[int(expected_value(posCounts.values(), lbls))]))