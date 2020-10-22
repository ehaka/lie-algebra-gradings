#!/usr/bin/env sage

# Import the code without installation by temporarily adding 
# the folder containing the 'lie_gradings' package to path.
import sys
import pathlib
path = pathlib.Path().absolute().parent
sys.path.append(str(path))

# Define the product Heisenberg times Heisenberg
sc = {
    ('A','B'):{'C':1},
    ('X','Y'):{'Z':1}
}
names = ['A', 'B', 'C', 'X', 'Y', 'Z']
L = LieAlgebra(QQ, sc, names, nilpotent=True)

# Print the Lie brackets.
from itertools import combinations
print("Lie brackets for the double Heisenberg Lie algebra:")
for X,Y in combinations(L.basis(), 2):
    Z = L[X,Y]
    if Z:
        print("  [%s, %s] = %s"%(X, Y, Z))
        
# Define a grading that admits a positive realization.
L.inject_variables()
print("\nA grading that admits a positive realization:")
from lie_gradings.gradings.lie_algebra_grading import grading
layers = {
    (1,0,0): [X],
    (0,5,0): [Y],
    (1,5,0): [Z],
    (0,0,3): [A, B],
    (0,0,6): [C]
}
magma = AdditiveAbelianGroup([0,0,0])
gr = grading(L, layers, magma)
print(gr)

# Positivise.
print("A positive realization:")
print(gr.to_positive_grading())

# Define a grading without a positive realization.
print("\nA grading without a positive realization:")
from lie_gradings.gradings.lie_algebra_grading import grading
layers = {
     (1,0): [X],
    (-1,0): [A],
     (0,1): [Y, C],
     (1,1): [Z, B]
}
magma = AdditiveAbelianGroup([0,0])
gr = grading(L, layers, magma)
print(gr)

# Attempt to compute a positive grading (raises an error)
gr.to_positive_grading()
