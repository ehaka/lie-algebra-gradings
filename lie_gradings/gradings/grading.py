from itertools import combinations
from sage.arith.functions import lcm
from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup
from sage.matrix.constructor import matrix
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module import FreeModule
from sage.modules.free_module_element import vector
from sage.rings.integer_ring import ZZ
from sage.structure.element import get_coercion_model

from lie_gradings.gradings.utilities import jordan_decomposition
from lie_gradings.gradings.lie_algebra_grading import grading

__all__ = ['maximal_grading', 'torsion_free_gradings', 'stratification']


def maximal_grading(L):
    r"""
    Return a maximal grading of a Lie algebra defined over an
    algebraically closed field.

    A maximal grading of a Lie algebra `\mathfrak{g}` is the finest
    possible grading of `\mathfrak{g}` over torsion free abelian groups.
    If `\mathfrak{g} = \bigoplus_{n\in \mathbb{Z}^k} \mathfrak{g}_n`
    is a maximal grading, then there exists no other grading
    `\mathfrak{g} = \bigoplus_{a\in A} \mathfrak{g}_a` over a torsion
    free abelian group `A` such that every `\mathfrak{g}_a` is contained
    in some `\mathfrak{g}_n`.

    EXAMPLES:

    A maximal grading of an abelian Lie algebra puts each basis element
    into an independent layer::

        sage: import sys, pathlib
        sage: sys.path.append(str(pathlib.Path().absolute()))
        sage: from lie_gradings.gradings.grading import maximal_grading
        sage: L = LieAlgebra(QQbar, 4, abelian=True)
        sage: maximal_grading(L)
        Grading over Additive abelian group isomorphic to Z + Z + Z + Z
        of Abelian Lie algebra on 4 generators (L[0], L[1], L[2], L[3])
        over Algebraic Field with nonzero layers
          (1, 0, 0, 0) : (L[3],)
          (0, 1, 0, 0) : (L[2],)
          (0, 0, 1, 0) : (L[1],)
          (0, 0, 0, 1) : (L[0],)

    A maximal grading of a free nilpotent Lie algebra decomposes the Lie
    algebra based on how many times each generator appears in the
    defining Lie bracket::

        sage: L = LieAlgebra(QQbar, 3, step=3)
        sage: maximal_grading(L)
        Grading over Additive abelian group isomorphic to Z + Z + Z of
        Free Nilpotent Lie algebra on 14 generators (X_1, X_2, X_3,
        X_12, X_13, X_23, X_112, X_113, X_122, X_123, X_132, X_133,
        X_223, X_233) over Algebraic Field with nonzero layers
          (1, 0, 0) : (X_1,)
          (0, 1, 0) : (X_2,)
          (1, 1, 0) : (X_12,)
          (1, 2, 0) : (X_122,)
          (2, 1, 0) : (X_112,)
          (0, 0, 1) : (X_3,)
          (0, 1, 1) : (X_23,)
          (0, 1, 2) : (X_233,)
          (0, 2, 1) : (X_223,)
          (1, 0, 1) : (X_13,)
          (1, 0, 2) : (X_133,)
          (1, 1, 1) : (X_123, X_132)
          (2, 0, 1) : (X_113,)
    """

    # define utilities to convert from matrices to vectors and back
    R = L.base_ring()
    n = L.dimension()
    MS = MatrixSpace(R, n, n)

    def matrix_to_vec(A):
        return vector(R, sum((list(Ar) for Ar in A.rows()), []))

    db = L.derivations_basis()

    def derivation_lincomb(vec):
        return sum((vk * dk for vk, dk in zip(vec, db)), MS.zero())

    # iteratively construct larger and larger tori of derivations
    t = []
    while True:
        # compute the centralizer of the torus in the derivation algebra
        ker = FreeModule(R, len(db))
        for der in t:
            # form the matrix of ad(der) with rows
            # the images of basis derivations
            A = matrix([matrix_to_vec(der * X - X * der) for X in db])
            ker = ker.intersection(A.left_kernel())
        cb = [derivation_lincomb(v) for v in ker.basis()]

        # check the basis of the centralizer for semisimple parts outside of t
        gl = FreeModule(R, n * n)
        t_submodule = gl.submodule([matrix_to_vec(der) for der in t])
        for A in cb:
            As, An = jordan_decomposition(A)
            if matrix_to_vec(As) not in t_submodule:
                # extend the torus by As
                t.append(As)
                break
        else:
            # no new elements found, so the torus is maximal
            break

    # compute the eigenspace intersections to get the concrete grading
    common_eigenspaces = [([], FreeModule(R, n))]
    for A in t:
        new_eigenspaces = []
        eig = A.right_eigenspaces()
        for ev, V in common_eigenspaces:
            for ew, W in eig:
                VW = V.intersection(W)
                if VW.dimension() > 0:
                    new_eigenspaces.append((ev + [ew], VW))
        common_eigenspaces = new_eigenspaces

    if not t:
        # zero dimensional maximal torus
        # the only grading is the trivial grading
        magma = AdditiveAbelianGroup([])
        layers = {magma.zero():L.basis().list()}
        return grading(L, layers, magma=magma)

    # define a grading with layers indexed by tuples of eigenvalues
    cm = get_coercion_model()
    all_eigenvalues = sum((ev for ev, V in common_eigenspaces), [])
    k = len(common_eigenspaces[0][0])
    evR = cm.common_parent(*all_eigenvalues)
    layers = {tuple(ev):[L.from_vector(v) for v in V.basis()]
                        for ev, V in common_eigenspaces}
    magma = evR.cartesian_product(*[evR] * (k - 1))
    gr = grading(L, layers, magma=magma)

    # convert to a grading over Z^k
    return gr.universal_realization()


def torsion_free_gradings(L):
    r"""
    Return a complete list of gradings of the Lie algebra over torsion
    free abelian groups.

    The list is guaranteed to be complete in the following sense:
    If `\mathfrak{g} = \bigoplus_{a\in A} \mathfrak{g}_a` is any grading
    of the Lie algebra `\mathfrak{g}` over a torsion free abelian group
    `A`, then there exists
    - a grading `\mathfrak{g} = \bigoplus_{n\in \mathbb{Z}^m} \mathfrak{g}_n`,
    - an automorphism `\Phi\in\mathrm{Aut}(\mathfrak{g})`, and
    - a homomorphism `\varphi\colon\mathbb{Z}^m\to A`
    such that the grading `\mathfrak{g} = \bigoplus_{n\in \mathbb{Z}^m} \Phi(\mathfrak{g}_{\varphi(n)})`
    is exactly the same as the original `A`-grading.
    However, the list is not guaranteed to be reduced up to
    automorphism, so the above choices are not in general unique.

    EXAMPLES:

    We list all gradings of the Heisenberg Lie algebra over torsion free
    abelian groups::

        sage: from lie_gradings.gradings.grading import torsion_free_gradings
        sage: L = lie_algebras.Heisenberg(QQ, 1)
        sage: torsion_free_gradings(L)
        [Grading over Additive abelian group isomorphic to Z + Z of Heisenberg algebra of rank 1 over Rational Field with nonzero layers
           (1, 0) : (p1,)
           (0, 1) : (q1,)
           (1, 1) : (z,)
         ,
         Grading over Additive abelian group isomorphic to Z of Heisenberg algebra of rank 1 over Rational Field with nonzero layers
           (1) : (p1, z)
           (0) : (q1,)
         ,
         Grading over Additive abelian group isomorphic to Z of Heisenberg algebra of rank 1 over Rational Field with nonzero layers
           (1) : (q1, z)
           (0) : (p1,)
         ,
         Grading over Additive abelian group isomorphic to Z of Heisenberg algebra of rank 1 over Rational Field with nonzero layers
           (1) : (p1, q1)
           (2) : (z,)
         ,
         Grading over Trivial group of Heisenberg algebra of rank 1 over Rational Field with nonzero layers
           () : (p1, q1, z)
         ]
    """
    maxgrading = maximal_grading(L)
    V = FreeModule(ZZ, len(maxgrading.magma().gens()))
    weights = maxgrading.layers().keys()

    # The torsion-free gradings are enumerated by torsion-free quotients
    # of the grading group of the maximal grading.
    diffset = set([tuple(b - a) for a, b in combinations(weights, 2)])
    subspaces = []
    for d in range(len(diffset) + 1):
        for B in combinations(diffset, d):
            W = V.submodule(B)
            if W not in subspaces:
                subspaces.append(W)

    # for each subspace, define the quotient grading
    projected_gradings = []
    for W in subspaces:
        Q = V.quotient(W)

        # check if quotient is not torsion-free
        if any(qi > 0 for qi in Q.invariants()):
            continue

        quot_layers = {}
        for n in weights:
            pi_n = tuple(Q(V(tuple(n))))
            if pi_n not in quot_layers:
                quot_layers[pi_n] = []
            quot_layers[pi_n].extend(maxgrading.layers()[n])

        # expand away denominators to get an integer vector grading
        A = AdditiveAbelianGroup(Q.invariants())
        denoms = [pi_n_k.denominator() for pi_n in quot_layers
                                       for pi_n_k in pi_n]
        mult = lcm(denoms)
        proj_layers = {tuple(mult * pi_nk for pi_nk in pi_n):l
                       for pi_n, l in quot_layers.items()}
        proj_grading = grading(L, proj_layers, magma=A, projections=True)
        projected_gradings.append(proj_grading)
    return projected_gradings


def stratification(L):
    r"""
    Return a stratification of the Lie algebra if one exists.

    INPUT:

    - ``L`` -- a Lie algebra

    OUTPUT:

    A grading of the Lie algebra `\mathfrak{g}` over the integers such
    that the layer `\mathfrak{g}_1` generates the full Lie algebra.

    EXAMPLES::

    A stratification for a free nilpotent Lie algebra is the
    one based on the length of the defining bracket::

        sage: from lie_gradings.gradings.grading import stratification
        sage: from lie_gradings.gradings.utilities import in_new_basis
        sage: L = LieAlgebra(QQ, 3, step=3)
        sage: strat = stratification(L)
        sage: strat
        Grading over Additive abelian group isomorphic to Z of Free Nilpotent
        Lie algebra on 14 generators (X_1, X_2, X_3, X_12, X_13, X_23, X_112,
        X_113, X_122, X_123, X_132, X_133, X_223, X_233) over Rational Field
        with nonzero layers
          (1) : (X_1, X_2, X_3)
          (2) : (X_12, X_13, X_23)
          (3) : (X_112, X_113, X_122, X_123, X_132, X_133, X_223, X_233)

    The main use case is when the original basis of the stratifiable Lie
    algebra is not adapted to a stratification. Consider the following
    quotient Lie algebra::

        sage: X_1, X_2, X_3 = L.basis().list()[:3]
        sage: Q = L.quotient(L[X_2, X_3])
        sage: Q
        Lie algebra quotient L/I of dimension 10 over Rational Field where
        L: Free Nilpotent Lie algebra on 14 generators (X_1, X_2, X_3, X_12, X_13, X_23, X_112, X_113, X_122, X_123, X_132, X_133, X_223, X_233) over Rational Field
        I: Ideal (X_23)

    We switch to a basis which does not define a stratification::

        sage: Y_1 = Q(X_1)
        sage: Y_2 = Q(X_2) + Q[X_1, X_2]
        sage: Y_3 = Q(X_3)
        sage: basis = [Y_1, Y_2, Y_3] + Q.basis().list()[3:]
        sage: Y_labels = ["Y_%d"%(k+1) for k in range(len(basis))]
        sage: K = in_new_basis(Q, basis,Y_labels)
        sage: K.inject_variables()
        Defining Y_1, Y_2, Y_3, Y_4, Y_5, Y_6, Y_7, Y_8, Y_9, Y_10
        sage: K[Y_2, Y_3]
        Y_9
        sage: K[[Y_1, Y_3], Y_2]
        Y_9

    We may reconstruct a stratification in the new basis without
    any knowledge of the original stratification::

        sage: stratification(K)
        Grading over Additive abelian group isomorphic to Z of Nilpotent Lie
        algebra on 10 generators (Y_1, Y_2, Y_3, Y_4, Y_5, Y_6, Y_7, Y_8, Y_9,
        Y_10) over Rational Field with nonzero layers
          (1) : (Y_1, Y_2 - Y_4, Y_3)
          (2) : (Y_4, Y_5)
          (3) : (Y_10, Y_6, Y_7, Y_8, Y_9)
        sage: K[Y_1, Y_2 - Y_4]
        Y_4
        sage: K[Y_1, Y_3]
        Y_5
        sage: K[Y_2 - Y_4, Y_3]
        0

    A non-stratifiable Lie algebra raises an error::

        sage: L = LieAlgebra(QQ, {('X_1','X_3'): {'X_4': 1},
        ....:                     ('X_1','X_4'): {'X_5': 1},
        ....:                     ('X_2','X_3'): {'X_5': 1}},
        ....:                    names='X_1,X_2,X_3,X_4,X_5')
        sage: stratification(L)
        Traceback (most recent call last):
        ...
        ValueError: Lie algebra on 5 generators (X_1, X_2, X_3, X_4,
        X_5) over Rational Field is not a stratifiable Lie algebra
    """
    lcs = L.lower_central_series(submodule=True)
    quots = [V.quotient(W) for V, W in zip(lcs, lcs[1:])]

    # find a basis adapted to the filtration by the lower central series
    adapted_basis = []
    weights = []
    for k, q in enumerate(quots):
        weights += [k + 1] * q.dimension()

        for v in q.basis():
            b = q.lift(v)
            adapted_basis.append(b)

    # define a submodule to compute structural
    # coefficients in the filtration adapted basis
    try:
        m = L.module()
    except AttributeError:
        m = FreeModule(L.base_ring(), L.dimension())
    sm = m.submodule_with_basis(adapted_basis)

    # form the linear system Ax=b of constraints from the Leibniz rule
    paramspace = [(k, h) for k in range(L.dimension())
                         for h in range(L.dimension())
                         if weights[h] > weights[k]]
    Arows = []
    bvec = []
    zerovec = m.zero()

    for i in range(L.dimension()):
        Y_i = adapted_basis[i]
        w_i = weights[i]
        for j in range(i + 1, L.dimension()):
            Y_j = adapted_basis[j]
            w_j = weights[j]
            Y_ij = L.bracket(Y_i, Y_j)
            c_ij = sm.coordinate_vector(Y_ij.to_vector())

            bcomp = L.zero()
            for k in range(L.dimension()):
                w_k = weights[k]
                Y_k = adapted_basis[k]
                bcomp += (w_k - w_i - w_j) * c_ij[k] * Y_k
            bv = bcomp.to_vector()

            Acomp = {}
            for k, h in paramspace:
                w_k = weights[k]
                Y_h = adapted_basis[h]
                if k == i:
                    Acomp[(k, h)] = L.bracket(Y_h, Y_j).to_vector()
                elif k == j:
                    Acomp[(k, h)] = L.bracket(Y_i, Y_h).to_vector()
                elif w_k >= w_i + w_j:
                    Acomp[(k, h)] = -c_ij[k] * Y_h

            for r in range(L.dimension()):
                Arows.append([Acomp.get((k, h), zerovec)[r]
                              for k, h in paramspace])
                bvec.append(bv[r])

    A = matrix(L.base_ring(), Arows)
    b = vector(L.base_ring(), bvec)

    # solve the linear system Ax=b if possible
    try:
        coeffs_flat = A.solve_right(b)
    except ValueError:
        raise ValueError("%s is not a stratifiable Lie algebra" % L)

    coeffs = {(k, h):ckh for (k, h), ckh
            in zip(paramspace, coeffs_flat)}

    # define the matrix of the derivation determined by the solution
    # in the adapted basis
    cols = []
    for k in range(L.dimension()):
        w_k = weights[k]
        Y_k = adapted_basis[k]
        hspace = [h for (l, h) in paramspace if l == k]
        Yk_im = w_k * Y_k + sum((coeffs[(k, h)] * adapted_basis[h]
                            for h in hspace), L.zero())
        cols.append(sm.coordinate_vector(Yk_im.to_vector()))

    der = matrix(L.base_ring(), cols).transpose()

    # the layers of the stratification are V_k = ker(der - kI)
    layers = {}
    for k in range(len(quots)):
        degree = k + 1
        B = der - degree * matrix.identity(L.dimension())
        adapted_kernel = B.right_kernel()

        # convert back to the original basis
        Vk_basis = [sm.from_vector(X)
                    for X in adapted_kernel.basis()]
        layers[(degree,)] = [L.from_vector(v) for v in
                             m.submodule(Vk_basis).basis()]

    return grading(L, layers, magma=AdditiveAbelianGroup([0]), projections=True)

