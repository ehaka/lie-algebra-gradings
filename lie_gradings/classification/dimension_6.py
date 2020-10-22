from lie_gradings.classification.classified_lie_algebra import ClassifiedNilpotentLieAlgebra
__all__ = ['L6_1', 'L6_2', 'L6_3', 'L6_4', 'L6_5', 'L6_6', 'L6_7', 'L6_8',
           'L6_9', 'L6_10', 'L6_11', 'L6_12', 'L6_13', 'L6_14', 'L6_15',
           'L6_16', 'L6_17', 'L6_18', 'L6_19', 'L6_20', 'L6_21', 'L6_22',
           'L6_23', 'L6_24', 'L6_25', 'L6_26', 'L6_27', 'L6_28']


def L6_1(F):
    sc = {}
    return ClassifiedNilpotentLieAlgebra(F, 'L6_1', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_2(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_2', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_3(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_3', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_4(F):
    sc = {
        ('X_1', 'X_2'): {'X_5': 1},
        ('X_3', 'X_4'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_4', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_5(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_5': 1},
        ('X_2', 'X_4'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_5', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_6(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_5': 1},
        ('X_2', 'X_3'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_6', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_7(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_7', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_8(F):
    sc = {
        ('X_1', 'X_2'): {'X_4': 1},
        ('X_1', 'X_3'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_8', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_9(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_2', 'X_3'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_9', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_10(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_6': 1},
        ('X_4', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_10', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_11(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_6': 1},
        ('X_2', 'X_3'): {'X_6': 1},
        ('X_2', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_11', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_12(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_6': 1},
        ('X_2', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_12', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_13(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_5': 1},
        ('X_1', 'X_5'): {'X_6': 1},
        ('X_2', 'X_4'): {'X_5': 1},
        ('X_3', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_13', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_14(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_5': 1},
        ('X_2', 'X_3'): {'X_5': 1},
        ('X_2', 'X_5'): {'X_6': 1},
        ('X_3', 'X_4'): {'X_6':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_14', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_15(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_5': 1},
        ('X_1', 'X_5'): {'X_6': 1},
        ('X_2', 'X_3'): {'X_5': 1},
        ('X_2', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_15', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_16(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_5': 1},
        ('X_2', 'X_5'): {'X_6': 1},
        ('X_3', 'X_4'): {'X_6':-1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_16', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_17(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_5': 1},
        ('X_1', 'X_5'): {'X_6': 1},
        ('X_2', 'X_3'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_17', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_18(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_5': 1},
        ('X_1', 'X_5'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_18', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_19(F, a):
    # classification in GAP follows Cicalo-de Graaf-Schneider 2012
    # instead of the slightly different de Graaf 2007
    # the only differences are:
    #   L6_19(0) -> L6_27
    #   L6_21(0) -> L6_28
    if a == F.zero():
        return L6_27(F)
    sc = {
        ('X_1', 'X_2'): {'X_4': 1},
        ('X_1', 'X_3'): {'X_5': 1},
        ('X_1', 'X_5'): {'X_6': 1},
        ('X_2', 'X_4'): {'X_6': 1},
        ('X_3', 'X_5'): {'X_6': a}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_19(%s)' % (a), sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_20(F):
    sc = {
        ('X_1', 'X_2'): {'X_4': 1},
        ('X_1', 'X_3'): {'X_5': 1},
        ('X_1', 'X_5'): {'X_6': 1},
        ('X_2', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_20', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_21(F, a):
    # classification in GAP follows Cicalo-de Graaf-Schneider 2012
    # instead of the slightly different de Graaf 2007
    # the only differences are:
    #   L6_19(0) -> L6_27
    #   L6_21(0) -> L6_28
    if a == F.zero():
        return L6_28(F)
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_6': 1},
        ('X_2', 'X_3'): {'X_5': 1},
        ('X_2', 'X_5'): {'X_6': a}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_21(%s)' % (a), sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_22(F, a):
    sc = {
        ('X_1', 'X_2'): {'X_5': 1},
        ('X_1', 'X_3'): {'X_6': 1},
        ('X_2', 'X_4'): {'X_6': a},
        ('X_3', 'X_4'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_22(%s)' % (a), sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_23(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_5': 1},
        ('X_1', 'X_4'): {'X_6': 1},
        ('X_2', 'X_4'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_23', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_24(F, a):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_5': 1},
        ('X_1', 'X_4'): {'X_6': a},
        ('X_2', 'X_3'): {'X_6': 1},
        ('X_2', 'X_4'): {'X_5': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_24(%s)' % (a), sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_25(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_5': 1},
        ('X_1', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_25', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_26(F):
    sc = {
        ('X_1', 'X_2'): {'X_4': 1},
        ('X_1', 'X_3'): {'X_5': 1},
        ('X_2', 'X_3'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_26', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_27(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_5': 1},
        ('X_2', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_27', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_28(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_5': 1},
        ('X_2', 'X_3'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_28', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_29(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_5': 1},
        ('X_1', 'X_5'): {'X_6': 1},
        ('X_2', 'X_4'): {'X_5': 1, 'X_6': 1},
        ('X_3', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_29', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_30(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_5': 1},
        ('X_1', 'X_5'): {'X_6': 1},
        ('X_2', 'X_3'): {'X_5': 1, 'X_6': 1},
        ('X_2', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_30', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_31(F, a):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_5': 1},
        ('X_2', 'X_3'): {'X_5': 1, 'X_6': a},
        ('X_2', 'X_5'): {'X_6': 1},
        ('X_3', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_31(%s)' % (a), sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_32(F, a):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_4'): {'X_5': 1},
        ('X_2', 'X_3'): {'X_6': a},
        ('X_2', 'X_5'): {'X_6': 1},
        ('X_3', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_32(%s)' % (a), sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_33(F):
    sc = {
        ('X_1', 'X_2'): {'X_4': 1},
        ('X_1', 'X_3'): {'X_5': 1},
        ('X_2', 'X_5'): {'X_6': 1},
        ('X_3', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_33', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_34(F):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_4': 1},
        ('X_1', 'X_5'): {'X_6': 1},
        ('X_2', 'X_3'): {'X_5': 1},
        ('X_2', 'X_4'): {'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_34', sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_35(F, a):
    sc = {
        ('X_1', 'X_2'): {'X_5': 1},
        ('X_1', 'X_3'): {'X_6': 1},
        ('X_2', 'X_4'): {'X_6': a},
        ('X_3', 'X_4'): {'X_5': 1, 'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_35(%s)' % (a), sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])


def L6_36(F, a):
    sc = {
        ('X_1', 'X_2'): {'X_3': 1},
        ('X_1', 'X_3'): {'X_5': 1},
        ('X_1', 'X_4'): {'X_6': a},
        ('X_2', 'X_3'): {'X_6': 1},
        ('X_2', 'X_4'): {'X_5': 1, 'X_6': 1}
    }
    return ClassifiedNilpotentLieAlgebra(F, 'L6_36(%s)' % (a), sc,
            names=['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6'])
