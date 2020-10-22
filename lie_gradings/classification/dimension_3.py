from lie_gradings.classification.classified_lie_algebra import ClassifiedNilpotentLieAlgebra
__all__ = ['L3_1', 'L3_2']


def L3_1(F):
    sc = {}
    return ClassifiedNilpotentLieAlgebra(F, 'L3_1', sc,
            names=['X_1', 'X_2', 'X_3'])


def L3_2(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L3_2', sc,
            names=['X_1', 'X_2', 'X_3'])
