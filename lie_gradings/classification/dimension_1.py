from lie_gradings.classification.classified_lie_algebra import ClassifiedNilpotentLieAlgebra
__all__ = ['L1_1']


def L1_1(F):
    sc = {}
    return ClassifiedNilpotentLieAlgebra(F, 'L1_1', sc, names=['X_1'])
