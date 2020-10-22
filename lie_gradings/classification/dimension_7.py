from sage.rings.rational_field import QQ
from lie_gradings.classification.classified_lie_algebra import ClassifiedNilpotentLieAlgebra
__all__ = ['L123457A', 'L123457B', 'L123457C', 'L123457D', 'L123457E',
           'L123457F', 'L123457G', 'L123457H', 'L123457I',
           'L12357A', 'L12357B', 'L12357C',
           'L12457A', 'L12457B', 'L12457C', 'L12457D', 'L12457E',
           'L12457F', 'L12457G', 'L12457H', 'L12457I', 'L12457J',
           'L12457K', 'L12457L', 'L12457M', 'L12457N',
           'L13457A', 'L13457B', 'L13457C', 'L13457D',
           'L13457E', 'L13457F', 'L13457G', 'L13457I',
           'L1357A', 'L1357B', 'L1357C', 'L1357D', 'L1357E', 'L1357F', 'L1357G',
           'L1357H', 'L1357I', 'L1357J', 'L1357K', 'L1357L', 'L1357M', 'L1357N',
           'L1357O', 'L1357P', 'L1357Q', 'L1357R', 'L1357S',
           'L137A', 'L137B', 'L137C', 'L137D',
           'L1457A', 'L1457B', 'L147A', 'L147B', 'L147D', 'L147E',
           'L157',
           'L17',
           'L23457A', 'L23457B', 'L23457C', 'L23457D',
           'L23457E', 'L23457F', 'L23457G',
           'L2357A', 'L2357B', 'L2357C', 'L2357D',
           'L2457A', 'L2457B', 'L2457C', 'L2457D', 'L2457E', 'L2457F', 'L2457G',
           'L2457H', 'L2457I', 'L2457J', 'L2457K', 'L2457L', 'L2457M',
           'L247A', 'L247B', 'L247C', 'L247D', 'L247E', 'L247F', 'L247G',
           'L247H', 'L247I', 'L247J', 'L247K', 'L247L', 'L247M', 'L247N',
           'L247O', 'L247P', 'L247Q', 'L247R',
           'L257A', 'L257B', 'L257C', 'L257D', 'L257E', 'L257F',
           'L257G', 'L257H', 'L257I', 'L257J', 'L257K', 'L257L',
           'L27A', 'L27B', 'L357A', 'L357B', 'L357C',
           'L37A', 'L37B', 'L37C', 'L37D']


# Carnot: rank 4, step 2
def L37A(F):
    sc = {
    ('X_1', 'X_2'): {'X_5': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '37A', sc,

            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 4 step 2
def L37B(F):
    sc = {
    ('X_1', 'X_2'): {'X_5': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '37B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 4 step 2
def L37C(F):
    sc = {
    ('X_1', 'X_2'): {'X_5': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '37C', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 4 step 2
def L37D(F):
    sc = {
    ('X_1', 'X_2'): {'X_5': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '37D', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 3
def L357A(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_2', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '357A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 3
def L357B(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '357B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 3
def L357C(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '357C', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 5 step 2
def L27A(F):
    sc = {
    ('X_1', 'X_2'): {'X_6': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_3', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '27A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot: rank 5, step 2
def L27B(F):
    sc = {
    ('X_1', 'X_2'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '27B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank step 3
def L257A(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '257A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 4 step 3
def L257B(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '257B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 4 step 3
def L257C(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_2', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '257C', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank step 3
def L257D(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '257D', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank step 3
def L257E(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_4', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '257E', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank step 3
def L257F(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_4', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '257F', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank step 3
def L257G(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_4', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '257G', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank step 3
def L257H(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_4', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '257H', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank step 3
def L257I(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_7': 1},
    ('X_1', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '257I', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank step 3
def L257J(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_7': 1},
    ('X_2', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '257J', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank step 3
def L257K(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_7': 1},
    ('X_4', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '257K', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank step 3
def L257L(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_7': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_4', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '257L', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 3
def L247A(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 3
def L247B(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_3', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 3
def L247C(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_3', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247C', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 3
def L247D(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247D', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 3
def L247E(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247E', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 3
def L247F(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_5'): {'X_6': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247F', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 3
def L247G(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1},
    ('X_3', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247G', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 3
def L247H(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1},
    ('X_3', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247H', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 3
def L247I(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_2', 'X_5'): {'X_6': 1},
    ('X_3', 'X_4'): {'X_6': 1},
    ('X_3', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247I', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 3
def L247J(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1},
    ('X_3', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247J', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 3
def L247K(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1},
    ('X_3', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247K', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 3
def L247L(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247L', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 3
def L247M(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_3', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247M', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 3
def L247N(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_7': 1},
    ('X_2', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247N', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 3
def L247O(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_7': 1},
    ('X_3', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247O', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 3
def L247P(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247P', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non  Carnot rank 3 step 3
def L247Q(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247Q', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 3
def L247R(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_3', 'X_4'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '247R', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank 3 step 4
def L2457A(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2457A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2457B(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2457B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2457C(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2457C', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2457D(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2457D', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2457E(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2457E', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2457F(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2457F', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2457G(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2457G', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2457H(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2457H', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2457I(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2457I', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2457J(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1, 'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2457J', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2457K(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2457K', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2457L(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2457L', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2457M(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2457M', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L2357A(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1, 'X_6': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2357A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2357B(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2357B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2357C(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2357C', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank 3 step 4
def L2357D(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_6': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '2357D', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank  step 5
def L23457A(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '23457A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank  step 5
def L23457B(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_2', 'X_5'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_6':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '23457B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot rank  step 5
def L23457C(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '23457C', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non  Carnot rank  step 5
def L23457D(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '23457D', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non  Carnot rank  step 5
def L23457E(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_5': 1, 'X_7': 1},
    ('X_2', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '23457E', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non  Carnot rank  step 5
def L23457F(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_2', 'X_3'): {'X_5': 1, 'X_7': 1},
    ('X_2', 'X_5'): {'X_6': 1},
    ('X_3', 'X_4'): {'X_6':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '23457F', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non  Carnot rank  step 5
def L23457G(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '23457G', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#  Carnot rank  step 2
def L17(F):
    sc = {
    ('X_1', 'X_2'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1},
    ('X_5', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '17', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non  Carnot rank  step 3
def L157(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_7': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_5', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '157', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non  Carnot rank  step 3
def L147A(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '147A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non  Carnot rank  step 3
def L147B(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_2', 'X_6'): {'X_7': 1},
    ('X_3', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '147B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#  Carnot rank  step 3
def L147D(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_6':-1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_6'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-2}
    }
    return ClassifiedNilpotentLieAlgebra(F, '147D', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#  Carnot rank  step 3, with parameter a\neq 0,1;, when a=0,1 isomorphic to 247P
# 147C is also isomorphic to 147E with a=1
def L147E(F, a):
    if a == 0 or a == 1:
        return L247P(F)
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_3'): {'X_6':-1},
    ('X_1', 'X_5'): {'X_7':-1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_6'): {'X_7': a},
    ('X_3', 'X_4'): {'X_7': 1 - a}
    }
    L =  ClassifiedNilpotentLieAlgebra(F, '147E(%s)'%a, sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])
    L._param = a
    return L


# non Carnot rank  step 4
def L1457A(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_5', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1457A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1457B(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_7': 1},
    ('X_5', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1457B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#  Carnot rank  step 3
def L137A(F):
    sc = {
    ('X_1', 'X_2'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_6': 1},
    ('X_3', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '137A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 3
def L137B(F):
    sc = {
    ('X_1', 'X_2'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_6': 1},
    ('X_3', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '137B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#  Carnot rank  step 3
def L137C(F):
    sc = {
    ('X_1', 'X_2'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_3', 'X_5'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '137C', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 3
def L137D(F):
    sc = {
    ('X_1', 'X_2'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_3', 'X_5'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '137D', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357A(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_6'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357B(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_3', 'X_6'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357C(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1},
    ('X_3', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357C', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357D(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357D', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357E(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_4', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357E', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357F(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_4', 'X_6'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357F', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357G(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357G', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357H(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_2', 'X_6'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357H', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357I(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_4', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357I', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357J(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_7': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_4', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357J', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357K(F):
    return L1357M(F, QQ(1) / 2)


# non Carnot rank  step 4
def L1357L(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_7': 1},
    ('X_2', 'X_4'): {'X_5': 1},
    ('X_2', 'X_6'): {'X_7': QQ(1) / 2},
    ('X_3', 'X_4'): {'X_7': QQ(1) / 2}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357L', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4 parameter a\neq 0, when a=0 isomorphic to 2357B
# when a=1/2 isomorphic to 1357K
def L1357M(F, a):
    if a == 0:
        return L2357B(F)
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_4'): {'X_5': 1},
    ('X_2', 'X_6'): {'X_7': a},
    ('X_3', 'X_4'): {'X_7': 1 - a}
    }
    if a == QQ(1) / 2:
        label = '1357K'
    else:
        label = '1357M(%s)'%a
    L = ClassifiedNilpotentLieAlgebra(F, label, sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])
    L._param = a
    return L


# non Carnot rank  step 4
def L1357N(F, a):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_7': a},
    ('X_2', 'X_4'): {'X_5': 1},
    ('X_3', 'X_4'): {'X_7': 1},
    ('X_4', 'X_6'): {'X_7': 1}
    }
    L = ClassifiedNilpotentLieAlgebra(F, '1357N(%s)'%a, sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])
    L._param = a
    return L


# non Carnot rank  step 4
def L1357O(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_5': 1},
    ('X_2', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357O', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357P(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_5': 1},
    ('X_2', 'X_6'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357P', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357Q(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357Q', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4
def L1357R(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '1357R', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 4 with parameter a\neq 1, when a=1 we get 2357D
def L1357S(F, a):
    if a == 1:
        return L2357D(F)
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_2', 'X_6'): {'X_7': a},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    L = ClassifiedNilpotentLieAlgebra(F, '1357S(%s)'%a, sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])
    L._param = a
    return L


# non Carnot rank  step 5
def L13457A(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '13457A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot rank  step 5
def L13457B(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_7': 1},
    ('X_2', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '13457B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L13457C(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '13457C', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L13457D(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_2', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '13457D', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L13457E(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '13457E', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L13457F(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '13457F', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L13457G(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '13457G', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L13457I(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_2', 'X_6'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '13457I', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12457A(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_6': 1},
    ('X_3', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12457A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12457B(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_6': 1, 'X_7': 1},
    ('X_3', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12457B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12457C(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_6': 1},
    ('X_2', 'X_6'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12457C', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12457D(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_6': 1},
    ('X_2', 'X_6'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12457D', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12457E(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_6': 1},
    ('X_3', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12457E', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12457F(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_6': 1},
    ('X_2', 'X_6'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12457F', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12457G(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_6': 1},
    ('X_1', 'X_5'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_6': 1},
    ('X_2', 'X_6'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12457G', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12457H(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12457H', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12457I(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12457I', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12457J(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12457J', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12457K(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_3', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12457K', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12457L(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_6'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1},
    ('X_3', 'X_5'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12457L', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# with parameter a,  12457M is obtained by taking a=0
def L12457M(F):
    return L12457N(F, 0)


def L12457N(F, a):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_1', 'X_4'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': a},
    ('X_2', 'X_6'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7': 1},
    ('X_3', 'X_5'): {'X_7':-1}
    }
    if a == 0:
        label = '12457M'
    else:
        label = '12457N(%s)'%a
    L = ClassifiedNilpotentLieAlgebra(F, label, sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])
    L._param = a
    return L


#
def L12357A(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_3', 'X_4'): {'X_6':-1},
    ('X_3', 'X_5'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12357A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12357B(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1, 'X_7': 1},
    ('X_3', 'X_4'): {'X_6':-1},
    ('X_3', 'X_5'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12357B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L12357C(F):
    sc = {
    ('X_1', 'X_2'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_6':-1},
    ('X_3', 'X_5'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '12357C', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# Carnot step 6
def L123457A(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '123457A', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# non Carnot step 6
def L123457B(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '123457B', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L123457C(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '123457C', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L123457D(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '123457D', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L123457E(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1, 'X_7': 1},
    ('X_2', 'X_4'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '123457E', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L123457F(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_6': 1},
    ('X_2', 'X_4'): {'X_7': 1},
    ('X_2', 'X_5'): {'X_7': 1},
    ('X_3', 'X_4'): {'X_7':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '123457F', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


#
def L123457G(F):
    return L123457I(F, 1)


#
def L123457H(F):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1, 'X_7': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, '123457H', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])


# with parameter a, if a=1, then  we get 123457G
def L123457I(F, a):
    sc = {
    ('X_1', 'X_2'): {'X_3': 1},
    ('X_1', 'X_3'): {'X_4': 1},
    ('X_1', 'X_4'): {'X_5': 1},
    ('X_1', 'X_5'): {'X_6': 1},
    ('X_1', 'X_6'): {'X_7': 1},
    ('X_2', 'X_3'): {'X_5': 1},
    ('X_2', 'X_4'): {'X_6': 1},
    ('X_2', 'X_5'): {'X_7': a},
    ('X_3', 'X_4'): {'X_7': 1 - a}
    }
    if a == 1:
        label = '123457G'
    else:
        label = '123457I(%s)'%a
    L = ClassifiedNilpotentLieAlgebra(F, label, sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7'])
    L._param = a
    return L
