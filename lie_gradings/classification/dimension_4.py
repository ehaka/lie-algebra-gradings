from lie_gradings.classification.classified_lie_algebra import ClassifiedNilpotentLieAlgebra
__all__ = ['L4_1', 'L4_2', 'L4_3']


def L4_1(F):
    sc = {}
    return ClassifiedNilpotentLieAlgebra(F, 'L4_1', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4'])


def L4_2(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L4_2', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4'])


def L4_3(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L4_3', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4'])
