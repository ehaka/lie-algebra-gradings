from lie_gradings.classification.dimension_1 import *
from lie_gradings.classification.dimension_2 import *
from lie_gradings.classification.dimension_3 import *
from lie_gradings.classification.dimension_4 import *
from lie_gradings.classification.dimension_5 import *
from lie_gradings.classification.dimension_6 import *
from lie_gradings.classification.dimension_7 import *

from sage.functions.other import sqrt
from sage.rings.qqbar import QQbar
from sage.rings.rational_field import QQ

__all__ = ['lie_algebra_isomorphism_classes']


def lie_algebra_isomorphism_classes(F, dim):
    r"""
    Return a list of isomorphism classes of Lie algebras.

    INPUT:

    - ``F`` -- the base field of the Lie algebras
    - ``dim`` -- the dimension of Lie algebras to list

    The full listing is implemented for the fields of rationals ``QQ``
    and algebraic numbers ``QQbar`` up to dimension 6.

    For dimension 7, the returned list is incomplete due to existence
    of one parameter families of Lie algebras, but contains at least one
    representative from each family.
    """
    if F not in [QQ, QQbar]:
        return NotImplemented

    if dim == 1:
        return [L1_1(F)]
    if dim == 2:
        return [L2_1(F)]
    if dim == 3:
        return [L3_1(F), L3_2(F)]
    if dim == 4:
        return [L4_1(F), L4_2(F), L4_3(F)]
    if dim == 5:
        return [L5_1(F), L5_2(F), L5_3(F), L5_4(F), L5_5(F),
                L5_6(F), L5_7(F), L5_8(F), L5_9(F)]
    if dim == 6:
        l = [L6_1(F), L6_2(F), L6_3(F), L6_4(F), L6_5(F), L6_6(F), L6_7(F),
             L6_8(F), L6_9(F), L6_10(F), L6_11(F), L6_12(F), L6_13(F),
             L6_14(F), L6_15(F), L6_16(F), L6_17(F), L6_18(F), L6_19(F, -1)]
        if F == QQ:
            l += [L6_19(F, 1)]
        l += [L6_20(F), L6_21(F, -1)]
        if F == QQ:
            l += [L6_21(F, 1)]
        l += [L6_22(F, 0), L6_22(F, 1)]
        if F == QQ:
            l += [L6_22(F, -1)]
        l += [L6_23(F)]
        l += [L6_24(F, 0), L6_24(F, 1)]
        if F == QQ:
            l += [L6_24(F, -1)]
        l += [L6_25(F), L6_26(F), L6_27(F), L6_28(F)]
        return l

    if dim == 7:
        if F == QQ:
            return NotImplemented

        i = QQbar.gens()[0]

        l = [L37A(F), L37B(F), L37C(F), L37D(F)]
        l += [L357A(F), L357B(F), L357C(F)]
        l += [L27A(F), L27B(F)]
        l += [L257A(F), L257B(F), L257C(F), L257D(F), L257E(F), L257F(F),
              L257G(F), L257H(F), L257I(F), L257J(F), L257K(F), L257L(F)]
        l += [L247A(F), L247B(F), L247C(F), L247D(F), L247E(F), L247F(F),
              L247G(F), L247H(F), L247I(F), L247J(F), L247K(F), L247L(F),
              L247M(F), L247N(F), L247O(F), L247P(F), L247Q(F), L247R(F)]
        l += [L2457A(F), L2457B(F), L2457C(F), L2457D(F), L2457E(F),
              L2457F(F), L2457G(F), L2457H(F), L2457I(F),
              L2457J(F), L2457K(F), L2457L(F), L2457M(F)]
        l += [L2357A(F), L2357B(F), L2357C(F), L2357D(F)]
        l += [L23457A(F), L23457B(F), L23457C(F), L23457D(F),
              L23457E(F), L23457F(F), L23457G(F)]
        l += [L17(F)]
        l += [L157(F)]

        # 147 has a family
        # 147C = 147E(0) = 147E(1) = 247P
        l += [L147A(F), L147B(F), L147D(F)]
        l += [L147E(F, 2)]  # singular value 147E(2)=147E(1/2)=147E(-1)
        # complex singular value same as 1/2-sqrt(3)/2*i
        l += [L147E(F, QQbar(1) / 2 + QQbar(sqrt(3)) / 2 * i)]
        # non-singular value
        # 147E(3)=147E(1/3)=147E(2/3)=147E(3/2)= 147E(-1/2)=147E(-2)
        l += [L147E(F, 3)]
        # non-singular value
        # 147E(5)=147E(1/5)=147E(4/5)=147E(5/4)= 147E(-1/4)=147E(-4)
        l += [L147E(F, 5)]

        l += [L1457A(F), L1457B(F)]
        l += [L137A(F), L137B(F), L137C(F), L137D(F)]

        # 1357 has a family
        l += [L1357A(F), L1357B(F), L1357C(F), L1357D(F), L1357E(F), L1357F(F),
              L1357G(F), L1357H(F), L1357I(F), L1357J(F), L1357K(F), L1357L(F)]
        # 1357M(a)=1357M(a') iff a=a'
        # 1357M(0)=2357B
        l += [L1357M(F, 1)]  # singular value
        l += [L1357M(F, 2)]  # singular value
        l += [L1357M(F, -1)]  # singular value
        # l += [L1357M(F, QQbar(1) / 2)]  # singular value, same as 1357K
        l += [L1357M(F, -QQbar(1) / 3)]  # singular value
        # complex singular value
        l += [L1357M(F, QQbar(1) / 2 - QQbar(sqrt(3)) / 2 * i)]
        # complex singular value
        l += [L1357M(F, QQbar(1) / 2 + QQbar(sqrt(3)) / 2 * i)]
        l += [L1357M(F, 3)]  # non singular value
        l += [L1357M(F, 5)]  # non singular value
        # 1357N(a)=1357N(a') iff a=a'
        l += [L1357N(F, 0)]  # singular value
        l += [L1357N(F, 1)]  # singular value
        l += [L1357N(F, 3)]  # non singular value
        l += [L1357N(F, 5)]  # non singular value
        l += [L1357O(F), L1357P(F), L1357Q(F), L1357R(F)]
        # 1357S(a)=1357S(a') iff a*a'=1
        # 1357S(1)=2357D
        l += [L1357S(F, 0)]  # singular value
        l += [L1357S(F, QQbar(1) / 2)]  # singular value
        l += [L1357S(F, -1)]  # singular value
        # complex singular value
        l += [L1357S(F, QQbar(1) / 2 - QQbar(sqrt(3)) / 2 * i)]
        # complex singular value
        l += [L1357S(F, QQbar(1) / 2 + QQbar(sqrt(3)) / 2 * i)]
        l += [L1357S(F, 3)]  # non singular value
        l += [L1357S(F, 5)]  # non singular value

        # 13457
        # 13457H in Seeley is not a Lie algebra
        l += [L13457A(F), L13457B(F), L13457C(F), L13457D(F),
              L13457E(F), L13457F(F), L13457G(F), L13457I(F)]

        # 12457 has a family
        l += [L12457A(F), L12457B(F), L12457C(F), L12457D(F), L12457E(F),
              L12457F(F), L12457G(F), L12457H(F), L12457I(F),
              L12457J(F), L12457K(F), L12457L(F), L12457M(F)]
        # 12457N(a)=12457N(a') iff a=a' or a=-a'
        # l += [L12457N(F, 0)]  # singular value, same as 12457M
        l += [L12457N(F, 1)]  # non singular value
        l += [L12457N(F, 3)]  # non singular value
        l += [L12457N(F, 5)]  # non singular value

        l += [L12357A(F), L12357B(F), L12357C(F)]

        # 123457 has a family
        l += [L123457A(F), L123457B(F), L123457C(F), L123457D(F),
              L123457E(F), L123457F(F), L123457G(F), L123457H(F)]
        # 123457I(a)=123457I(a') iff a=a'
        l += [L123457I(F, 0)]  # non singular value
        #l += [L123457I(F, 1)]  # singular value, same as 123457G
        l += [L123457I(F, 2)]  # singular value
        l += [L123457I(F, 3)]  # singular value
        l += [L123457I(F, -1)]  # singular value
        # complex singular value
        l += [L123457I(F, QQbar(1) / 2 - QQbar(sqrt(3)) / 2 * i)]
        # complex singular value
        l += [L123457I(F, QQbar(1) / 2 + QQbar(sqrt(3)) / 2 * i)]
        return l

    return NotImplemented
