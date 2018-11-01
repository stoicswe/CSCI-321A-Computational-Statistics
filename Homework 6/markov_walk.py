import numpy as np
import random

transition_matrix = [ [0.5,0.35,0.15,0.], [0.,0.,0.2,0.8], [0.,0.,0.3,0.7], [1.0,0.,0.,0.]]
state_vector = [0.,1.0,0.,0.]
super_position_state = numpy.dot(state_vector, transition_matrix)

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
    new_state[random.choice(state_list)] = 1.0;
     
    return new_state

state_vector = get_next_state(super_position_state)

def get_state(state_vector):
    index = [i for i, e in enumerate(state_vector) if e != 0]
    return 'S' + str(index[0])

for i in range(100):
    super_position_state = numpy.dot(state_vector, transition_matrix)
    state_vector = get_next_state(super_position_state)
    print(state_vector, ':', get_state(state_vector))