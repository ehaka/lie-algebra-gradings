#!/usr/bin/env sage

# Import the code without installation by temporarily adding 
# the folder containing the 'lie_gradings' package to path.
import sys
import pathlib
path = pathlib.Path().absolute().parent
sys.path.append(str(path))

# In the Cicalò-de Graaf-Schneider classification, 
# the second Heisenberg Lie algebra is L_{5,4}.
from lie_gradings.classification.dimension_5 import L5_4
L = L5_4(QQ)

# Print the Lie brackets.
from itertools import combinations
print("Lie brackets for the second Heisenberg Lie algebra:")
for X,Y in combinations(L.basis(), 2):
    Z = L[X,Y]
    if Z:
        print("  [%s, %s] = %s"%(X, Y, Z))

# Compute a maximal grading.
print("\nMaximal grading:")
from lie_gradings.gradings.grading import maximal_grading
gr = maximal_grading(L)
print(gr)

# Enumerate all torsion free gradings.
from lie_gradings.gradings.grading import torsion_free_gradings
grlist = torsion_free_gradings(L)
print("Torsion free gradings:")
for gr in grlist:
    print(gr)
    
# Compute the stratification.
print("Stratification:")
from lie_gradings.gradings.grading import stratification
gr = stratification(L)
print(gr)
