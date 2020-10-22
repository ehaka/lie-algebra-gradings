from lie_gradings.classification.classified_lie_algebra import ClassifiedNilpotentLieAlgebra
__all__ = ['L5_1', 'L5_2', 'L5_3', 'L5_4', 'L5_5',
           'L5_6', 'L5_7', 'L5_8', 'L5_9']


def L5_1(F):
    sc = {}
    return ClassifiedNilpotentLieAlgebra(F, 'L5_1', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5'])


def L5_2(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L5_2', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5'])


def L5_3(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L5_3', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5'])


def L5_4(F):
    sc = {
        ('X_1', 'X_2'): {'X_5': 1},
        ('X_3', 'X_4'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L5_4', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5'])


def L5_5(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_5': 1},
        ('X_2', 'X_4'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L5_5', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5'])


def L5_6(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_5': 1},
        ('X_2', 'X_3'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L5_6', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5'])


def L5_7(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L5_7', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5'])


def L5_8(F):
    sc = {
        ('X_1', 'X_2'): {'X_4': 1},
        ('X_1', 'X_3'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L5_8', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5'])


def L5_9(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_2', 'X_3'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L5_9', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5'])
