from lie_gradings.classification.classified_lie_algebra import ClassifiedNilpotentLieAlgebra
__all__ = ['L2_1']


def L2_1(F):
    sc = {}
    return ClassifiedNilpotentLieAlgebra(F, 'L2_1', sc, names=['X_1', 'X_2'])
