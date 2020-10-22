from itertools import combinations
from sage.algebras.lie_algebras.lie_algebra import LieAlgebra
from sage.arith.misc import gcd
from sage.categories.lie_algebras import LieAlgebras
from sage.combinat.integer_vector import IntegerVectors
from sage.matrix.constructor import matrix
from sage.modules.free_module import FreeModule

__all__ = ['in_new_basis', 'jordan_decomposition']


def in_new_basis(L, basis, names, check=True, category=None):
    r"""
    Return an isomorphic copy of the Lie algebra in a different basis.

    INPUT:

    - ``L`` -- the Lie algebra
    - ``basis`` -- a list of elements of the Lie algebra
    - ``names`` -- a list of strings to use as names for the new basis
    - ``check`` -- (default:``True``) a boolean; if ``True``, verify
      that the list ``basis`` is indeed a basis of the Lie algebra
    - ``category`` -- (default:``None``) a subcategory of
      :class:`FiniteDimensionalLieAlgebrasWithBasis` to apply to the
      new Lie algebra.

    EXAMPLES:

    The method may be used to relabel the elements::

        sage: import sys, pathlib
        sage: sys.path.append(str(pathlib.Path().absolute()))
        sage: from lie_gradings.gradings.utilities import in_new_basis
        sage: L.<X,Y> = LieAlgebra(QQ, {('X','Y'): {'Y': 1}})
        sage: K.<A,B> = in_new_basis(L, [X, Y])
        sage: K[A,B]
        B

    The new Lie algebra inherits nilpotency::

        sage: L = lie_algebras.Heisenberg(QQ, 1)
        sage: X,Y,Z = L.basis()
        sage: L.category()
        Category of finite dimensional nilpotent lie algebras with basis over Rational Field
        sage: K.<A,B,C> = in_new_basis(L, [X + Y, Y - X, Z])
        sage: K[A,B]
        2*C
        sage: K[[A,B],A]
        0
        sage: K.is_nilpotent()
        True
        sage: K.category()
        Category of finite dimensional nilpotent lie algebras with basis over Rational Field

    Some properties such as being stratified may in general be lost when
    changing the basis, and are therefore not preserved::

        sage: L.<X,Y,Z> = LieAlgebra(QQ, 2, step=2)
        sage: L.category()
        Category of finite dimensional stratified lie algebras with basis over Rational Field
        sage: K.<A,B,C> = in_new_basis(L, [Z, X, Y])
        sage: K.category()
        Category of finite dimensional nilpotent lie algebras with basis over Rational Field

    If the property is known to be preserved, an extra category may
    be passed to the method::

        sage: C = L.category()
        sage: K.<A,B,C> = in_new_basis(L, [Z, X, Y], category=C)
        sage: K.category()
        Category of finite dimensional stratified lie algebras with basis over Rational Field
    """
    try:
        m = L.module()
    except AttributeError:
        m = FreeModule(L.base_ring(), L.dimension())
    sm = m.submodule_with_basis([X.to_vector() for X in basis])

    if check:
        # check that new basis is a basis
        A = matrix([X.to_vector() for X in basis])
        if not A.is_invertible():
            raise ValueError(
                "%s is not a basis of the Lie algebra" % basis)

    # form dictionary of structure coefficients in the new basis
    sc = {}
    for (X, nX), (Y, nY) in combinations(zip(basis, names), 2):
        Z = X.bracket(Y)
        zvec = sm.coordinate_vector(Z.to_vector())
        sc[(nX, nY)] = {nW: c for nW, c in zip(names, zvec)}

    C = LieAlgebras(L.base_ring()).FiniteDimensional().WithBasis()
    C = C.or_subcategory(category)
    if L.is_nilpotent():
        C = C.Nilpotent()

    return LieAlgebra(L.base_ring(), sc, names=names, category=C)


def jordan_decomposition(A):
    r"""
    Return the Jordan decomposition of the matrix ``A``.

    INPUT:

    - ``A`` -- a matrix

    OUTPUT:

    A pair of matrices ``(A_s, A_n)`` such that `A_s` is a semisimple matrix,
    `A_n` is a nilpotent matrix, `A = A_s + A_n`, and the matrices `A_s` and
    `A_n` commute.

    EXAMPLE:

    The Jordan decomposition of a matrix in Jordan normal form is the
    decomposition into its diagonal and strictly upper-triangular parts::

        sage: from lie_gradings.gradings.utilities import jordan_decomposition
        sage: J12 = matrix.jordan_block(1,2)
        sage: J21 = matrix.jordan_block(2,1)
        sage: A = matrix.block_diagonal(J12, J21); A
        [1 1|0]
        [0 1|0]
        [---+-]
        [0 0|2]
        sage: jordan_decomposition(A)
        (
        [1 0 0]  [0 1 0]
        [0 1 0]  [0 0 0]
        [0 0 2], [0 0 0]
        )
        sage: A = matrix.jordan_block(1,4); A
        [1 1 0 0]
        [0 1 1 0]
        [0 0 1 1]
        [0 0 0 1]
        sage: jordan_decomposition(A)
        (
        [1 0 0 0]  [0 1 0 0]
        [0 1 0 0]  [0 0 1 0]
        [0 0 1 0]  [0 0 0 1]
        [0 0 0 1], [0 0 0 0]
        )

    For semisimple and nilpotent matrices, the Jordan decomposition is itself::

        sage: As = matrix([[0, -1], [1, 0]])
        sage: jordan_decomposition(As)
        (
        [ 0 -1]  [0 0]
        [ 1  0], [0 0]
        )
        sage: An = matrix([[0, 1], [0, 0]])
        sage: jordan_decomposition(An)
        (
        [0 0]  [0 1]
        [0 0], [0 0]
        )

    For a general matrix, the Jordan decomposition is much less clear::

        sage: A = matrix([[24, 6, -14], [-66, -28, 84], [-18, -12, 36]])
        sage: As,An = jordan_decomposition(A)
        sage: As,An
        (
        [ 12   0   0]  [ 12   6 -14]
        [-84 -37 105]  [ 18   9 -21]
        [-36 -21  57], [ 18   9 -21]
        )
        sage: A.jordan_form(), As.jordan_form(), An.jordan_form()
        (
                    [ 8| 0| 0]
        [ 8| 0  0]  [--+--+--]  [0 1|0]
        [--+-----]  [ 0|12| 0]  [0 0|0]
        [ 0|12  1]  [--+--+--]  [---+-]
        [ 0| 0 12], [ 0| 0|12], [0 0|0]
        )
        sage: As * An - An * As
        [0 0 0]
        [0 0 0]
        [0 0 0]

    ALGORITHM:

        The following is Algorithm JordanDecomposition from Appendix A.2 of
        Willem A. de Graaf. Lie Algebras: Theory and Algorithms.
        North-Holland Mathematical Library. (2000). Elsevier Science B.V..

        The Jordan decomposition of an endomorphism of a finite dimensional
        vector space is computed by the following steps:

        1. Compute the minimal polynomial `f` of the matrix `A`.
        2. Let `h` be the product of irreducible factors of `f`, which may be
           computed by dividing `f` by the gcd with its derivative.
        3. Compute polynomials `p,q` such that `ph + qh' = 1`. Set `A_k = A`.
        4. If `h(A_k)=0`, then `A_k` is the semisimple part of the Jordan
           decomposition, so the Jordan decomposition is `A = A_k + (A-A_k)`.
        5. Otherwise, replace `A_k` by `A_k - h(A_k)q(A_k)` and repeat from 4.
    """
    f = A.minpoly()
    h = f / f.gcd(f.derivative())
    d, p, q = h.xgcd(h.derivative())

    # in case d = gcd(h, h') is not 1, normalize
    q = q / d

    Ak = A
    while h(Ak) != 0:
        Ak = Ak - h(Ak) * q(Ak)
    return (Ak, A - Ak)
