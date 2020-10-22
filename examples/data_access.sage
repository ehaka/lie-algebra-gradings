#!/usr/bin/env sage

# Import the code without installation by temporarily adding 
# the folder containing the 'lie_gradings' package to path.
import sys
import pathlib
path = pathlib.Path().absolute().parent
sys.path.append(str(path))

# In the Cicalò-de Graaf-Schneider classification, 
# the product of two Heisenberg Lie algebras is L_{6,22}(1).
# We will load some info about its grading from the precomputed data.
datafolder = path / 'dim7' / 'data'
maxgrading_file = datafolder / 'maximal_gradings' / 'L6_22(1).maxgrading'

# the files must be loaded as binary files
with open(maxgrading_file, 'rb') as f:
    data = f.read()
    
    # unpickle the data into a Sage object
    mgr = loads(data)
print("The maximal grading in the classification basis loaded from a file:")
print(mgr)

isomclass_file = datafolder / 'isomorphism_classes' / 'L6_22(1)' / '1.0101' / 'c.isom_class'
with open(isomclass_file, 'rb') as f:
    data = f.read()
    # unpickle the data into a Sage object
    isomclass = loads(data)
# extract a representative of the isomorphism class
strat = isomclass.representative()
print("The stratification loaded from a file:")
print(strat)

# the lie algebra can be extracted from the grading
L = strat.lie_algebra()
print(L)
print("with the brackets:")
from itertools import combinations
for X,Y in combinations(L.basis(), 2):
    Z = L[X,Y]
    if Z:
        print("  [%s, %s] = %s"%(X,Y,Z)) 

# The lie algebras are also stored in the 'torsion_free' folder
lie_file = datafolder / 'torsion_free' / 'L6_22(1)' / 'lie_algebra'
with open(lie_file, 'rb') as f:
    data = f.read()
    # unpickle the data into a Sage object
    L2 = loads(data)
print("The Lie algebra from a file:")
print(L2)
print("Is identical to the previous Lie algebra as an object:", L == L2) 