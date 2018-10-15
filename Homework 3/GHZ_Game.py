from qiskit import *
import numpy as np
import random as rand

shots = 1
backend = 'local_qasm_simulator'

N=100
cont_win = 0
cont_tot = 0

# ref sends 3 bit string:
# choices (RST):
# 000, 011, 101, 110
# sends R to alice, s to Bob, t to Charlie
# answers must be bits a, b, c, (each from respective persons)
# they win if a + b + c = r || s || t

# strategy:
# if q == 1, H to qubit

def xor(x, y):
    if(x == 0):
        if(y == 1):
            return 1
        elif(y == 0):
            return 0
    elif(x == 1):
        if(y == 1):
            return 0
        elif(y == 0):
            return 1

for i in range(N):

    Q_program = QuantumProgram()

    q = Q_program.create_quantum_register('q', 3) 
    c = Q_program.create_classical_register('c', 3)
    game = Q_program.create_circuit('game', [q], [c])
    
    game.h(q[0])
    game.cx(q[0],q[1])
    game.cx(q[1],q[2])

    ref_choices = ['000','011','101','110']

    random_choice = rand.randint(0,3)
    ref_choice = ref_choices[random_choice]
    print("Ref choice: {0}".format(ref_choice))
    r = 0
    s = 0
    t = 0
    if(ref_choice == '000'):
        r = 0
        s = 0
        t = 0
    elif(ref_choice == '011'):
        r = 0
        s = 1
        t = 1
    elif(ref_choice == '101'):
        r = 1
        s = 0
        t = 1
    elif(ref_choice == '110'):
        r = 1
        s = 1
        t = 0

    print("Ref chooses: {0}{1}{2}".format(r,s,t))

    if(r == 1): # alice (q == 1)
        game.h(q[0])
    if(s == 1): # bob (q == 1)
        game.h(q[1])
    if(t == 1): # charlie (q == 1)
        game.h(q[2])

    game.measure(q[0], c[0])
    game.measure(q[1], c[1])
    game.measure(q[2], c[2])

    circuits = ['game']
    result = Q_program.execute(circuits, shots=1)
    data = result.get_counts('game')
    print("Counts: {0}".format(data))
    
    for outcomes in data.keys():
        out = outcomes
    print("Outcome of Strategy: {0}".format(out))
    # which are the answers of Alice(a) and Bob (b), from a 'string' type  to 'integer' type 
    a = 0
    b = 0
    c = 0
    if(out == '000'):
        a = 0
        b = 0
        c = 0
    if(out == '101'):
        a = 1
        b = 0  
        c = 1
    if(out == '110'):
        a = 0
        b = 1
        c = 1
    if(out == '011'):
        a = 1
        b = 1
        c = 0
    res = a^b^c
    win = r^s^t
    print("Result: {0}".format(res))
    if(res == win):
        cont_win += 1
    cont_tot += 1 

qProb_win = cont_win/cont_tot
print('Alice, Bob, and Charlie won the game with probability: ', qProb_win*100, '%')