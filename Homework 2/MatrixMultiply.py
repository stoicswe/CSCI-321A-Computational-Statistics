import numpy as np
import random as rand
import math

def dot(v, w):
    return sum(v_i*w_i for v_i, w_i in zip(v,w))

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

def is_diagonal(i, j):
    return 1 if i == j else 0

def is_zeros(i, j):
    return 0

def is_random(i, j):
    return rand.randint(1,10)

def matrix_multiply(A, B):
    arows, acols = shape(A)
    brows, bcols = shape(B)
    if arows == bcols:
        C = make_matrix(arows, bcols, is_zeros)

        for i in range(arows):
            for j in range(bcols):
                C[i][j] = dot(A[i], B[j])
        return C
    else:
        print("error! matrices to multiply dont match! (M,K K,M)")
        return -1

#A = make_matrix(4, 4, is_diagonal)
#B = make_matrix(4, 4, is_diagonal)
#A = make_matrix(3, 4, is_random)
#B = make_matrix(4, 3, is_random)

#===================================================================
#DEFINE VARIABLES AND MATRICES:
ZERO_POS = [[1], [0]]
ONE_POS =  [[0], [1]]
ZERO_ZERO = [[1],[0],[0],[0]]
ZERO_ONE =  [[0],[1],[0],[0]]
ONE_ZERO =  [[0],[0],[1],[0]]
ONE_ONE =   [[0],[0],[0],[1]]
#=====================================================================
#CHECK THESE MATRICES:
ZERO_ZERO_ZERO = [[1],[0],[0],[0],[0],[0],[0],[0]]
ZERO_ONE_ZERO =  [[0],[1],[0],[0],[0],[0],[0],[0]]
ZERO_ZERO_ONE =  [[0],[0],[1],[0],[0],[0],[0],[0]]
ONE_ZERO_ZERO =  [[0],[0],[0],[1],[0],[0],[0],[0]]
ZERO_ONE_ONE =   [[0],[0],[0],[0],[1],[0],[0],[0]]
ONE_ONE_ZERO =   [[0],[0],[0],[0],[0],[1],[0],[0]]
ONE_ZERO_ONE =   [[0],[0],[0],[0],[0],[0],[1],[0]]
ONE_ONE_ONE =    [[0],[0],[0],[0],[0],[0],[0],[1]]
#======================================================================
#DEFINE OPERATORS:
H = [[1/math.sqrt(2),1/math.sqrt(2)],[1/math.sqrt(2),-1/math.sqrt(2)]]
X = [[0,1],[1, 0]]
Z = [[0,1],[0,-1]]
CNOT = [
    [1,0,0,0], 
    [0,1,0,0], 
    [0,0,0,1], 
    [0,0,1,0]]
TOFOLLI = [
    [1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,1,0]]
FREDKIN_SWAP = [
    [1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1]]
#===================================================================
#DO MATH:
HX = matrix_multiply(H, X)
HXH = matrix_multiply(HX, H)
HZ = matrix_multiply(H, Z)
HZH = matrix_multiply(HZ, H)
X0 = matrix_multiply(ZERO_POS, X)
X1 = matrix_multiply(ONE_POS, X)
Z0 = matrix_multiply(ZERO_POS, Z)
Z1 = matrix_multiply(ONE_POS, Z)
CNOT_ZERO_ZERO = matrix_multiply(ZERO_ZERO, CNOT)
CNOT_ZERO_ONE = matrix_multiply(ZERO_ONE, CNOT)
CNOT_ONE_ZERO = matrix_multiply(ONE_ZERO, CNOT)
CNOT_ZERO_ONE = matrix_multiply(ONE_ONE, CNOT)
TOFOLLI_ZERO_ZERO_ZERO = matrix_multiply(ZERO_ZERO_ZERO, TOFOLLI)
TOFOLLI_ZERO_ONE_ZERO = matrix_multiply(ZERO_ONE_ZERO, TOFOLLI)
TOFOLLI_ONE_ZERO_ZERO = matrix_multiply(ONE_ZERO_ZERO, TOFOLLI)
TOFOLLI_ONE_ONE_ZERO = matrix_multiply(ONE_ONE_ZERO, TOFOLLI)
TOFOLLI_ZERO_ONE_ONE = matrix_multiply(ZERO_ONE_ONE, TOFOLLI)
TOFOLLI_ONE_ZERO_ONE = matrix_multiply(ONE_ZERO_ONE, TOFOLLI)
TOFOLLI_ONE_ONE_ONE = matrix_multiply(ONE_ONE_ONE, TOFOLLI)
TOFOLLI_ZERO_ZERO_ONE = matrix_multiply(ZERO_ZERO_ONE, TOFOLLI)
#===========================================================================
#PRINT THE VARS:
print("|0>")
print(ZERO_POS)
print("|1>")
print(ONE_POS)
print("|00>")
print(ZERO_ZERO)
print("|01>")
print(ZERO_ONE)
print("|10>")
print(ONE_ZERO)
print("|11>")
print(ONE_ONE)
print("|000>")
print(ZERO_ZERO_ZERO)
print("|001")
print(ZERO_ZERO_ONE)
print("|010")
print(ZERO_ONE_ZERO)
print("|100>")
print(ONE_ZERO_ZERO)
print("|011>")
print(ZERO_ONE_ONE)
print("|110>")
print(ONE_ONE_ZERO)
print("|111>")
print(ONE_ONE_ONE)
#===========================================================================
#PRINT THE OPERATORS:
print("H Matrix:")
print(H)
print("X Matrix:")
print(X)
print("Z")
print(Z)
print("CNOT")
print(CNOT)
print("TOFOLLI")
print(TOFOLLI)
#============================================================================
#PRINT THE RESULTS:
print("Result of H*X:")
print(HX)
print("Result of H*X*H")
print(HXH)
print("Result of H*Z")
print(HZ)
print("Result of H*Z*H")
print(HZH)
print("X|0>")
print(X0)
print("X|1>")
print(X1)
print("Z|0>")
print(Z0)
print("Z|1>")
print(Z1)
print("CNOT|00>")
print(CNOT_ZERO_ZERO)
print("CNOT|01>")
print(CNOT_ZERO_ONE)
print("CNOT|10>")
print(CNOT_ONE_ZERO)
print("CNOT|11>")
print(CNOT_ZERO_ONE)
print("TOFOLLI|000>")
print(TOFOLLI_ZERO_ZERO_ZERO)
print("TOFOLLI|010>")
print(TOFOLLI_ZERO_ONE_ZERO)
print("TOFOLLI|100>")
print(TOFOLLI_ONE_ZERO_ZERO)
print("TOFOLLI|110>")
print(TOFOLLI_ONE_ONE_ZERO)
print("TOFOLLI|011>")
print(TOFOLLI_ZERO_ONE_ONE)
print("TOFOLLI|101>")
print(TOFOLLI_ONE_ZERO_ONE)
print("TOFOLLI|111>")
print(TOFOLLI_ONE_ONE_ONE)
print("TOFOLLI|001>")
print(TOFOLLI_ZERO_ZERO_ONE)