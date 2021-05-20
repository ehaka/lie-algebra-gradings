from itertools import combinations, combinations_with_replacement, product
from sage.arith.functions import lcm
from sage.arith.misc import gcd
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups
from sage.categories.lie_algebras import LieAlgebras
from sage.categories.sets_cat import Sets
from sage.combinat.integer_vector import IntegerVectors
from sage.combinat.posets.posets import Poset
from sage.geometry.polyhedron.constructor import Polyhedron
from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup
from sage.matrix.constructor import matrix
from sage.misc.cachefunc import cached_method
from sage.misc.latex import latex
from sage.modules.free_module import FreeModule, VectorSpace
from sage.modules.free_module_element import vector
from sage.numerical.mip import MixedIntegerLinearProgram
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.rings.polynomial.term_order import TermOrder
from sage.structure.element import get_coercion_model
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.ring import SR

from lie_gradings.gradings.utilities import in_new_basis

__all__ = ['grading']


def grading(L, layers, magma=None, projections=False, check=True):
    r"""
    Return a grading of the Lie algebra over an additive magma.

    A grading of a Lie algebra `\mathfrak{g}` over an additive magma `A`
    is a direct sum decomposition `\mathfrak{g} = \bigoplus_{a \in A}
    \mathfrak{g}_a`, where each `\mathfrak{g}_a` is a subspace of the
    Lie algebra and the decomposition is compatible with the Lie bracket
    through the inclusion `[\mathfrak{g}_a, \mathfrak{g}_b] \subset
    \mathfrak{g}_{a+b}`.

    INPUT:

    - ``L`` -- a Lie algebra
    - ``layers`` -- a dictionary ``{a: B}`` or list of pairs ``(a, B)``
      where the keys are elements ``a`` of an abelian magma and values
      are lists ``B`` of Lie algebra elements giving a basis of the
      subspace `\mathfrak{g}_a`
    - ``magma`` -- (default:``None``) an additive magma; if ``None``,
      the magma will be inferred from the keys of ``layers``
    - ``projections`` -- (default:``False``); if set to ``True``, then it is
      assumed that every isomorphic grading is the pushforward grading
      by a homomorphism of weights
    - ``check`` -- (default:``True``) a boolean; if ``True``, verify
      that the layers span the full Lie algebra, are disjoint, and
      respect the bracket

    EXAMPLES:

    A grading over the abelian group `\mathbb{Z}_2\times\mathbb{Z}`::

        sage: import sys, pathlib
        sage: sys.path.append(str(pathlib.Path().absolute()))
        sage: from lie_gradings.gradings.lie_algebra_grading import grading
        sage: sc = {('X','Y'): {'Z': 1}, ('X','Z'): {'W': 1}}
        sage: L.<X,Y,Z,W> = LieAlgebra(QQ, sc)
        sage: layers = {(1,0): [X], (0,1): [Y,W], (1,1): [Z]}
        sage: A = AdditiveAbelianGroup([2, 0])
        sage: gr = grading(L, layers, magma = A)
        sage: gr
        Grading over Additive abelian group isomorphic to Z/2 + Z of Lie
        algebra on 4 generators (X, Y, Z, W) over Rational Field with
        nonzero layers
          (0, 1) : (W, Y)
          (1, 0) : (X,)
          (1, 1) : (Z,)
    """
    return LieAlgebraGrading(layers, lie_algebra=L, magma=magma,
                             projections=projections, check=check)


class LieAlgebraGrading(Parent, UniqueRepresentation):
    r"""
    A grading of a Lie algebra over an additive magma.

    A grading of a Lie algebra `\mathfrak{g}` over an additive magma `A` is a
    direct sum decomposition `\mathfrak{g} = \bigoplus_{a\in A} \mathfrak{g}_a`,
    where each `\mathfrak{g}_a` is a subspace of the Lie algebra and the
    decomposition is compatible with the Lie bracket through the inclusion
    `[\mathfrak{g}_a, \mathfrak{g}_b] \subset \mathfrak{g}_{a+b}`.

    INPUT:

    - ``layers`` -- a dictionary ``{a: B}`` or list of pairs ``(a, B)`` where
      the keys are elements ``a`` of an abelian magma and values are lists ``B``
      of Lie algebra elements giving a basis of the subspace `\mathfrak{g}_a`
    - ``lie_algebra`` -- (default:``None``) a finite dimensional Lie algebra
      with basis; if ``None``, the Lie algebra will be inferred from the values
      of the dictionary ``layers``
    - ``magma`` -- (default:``None``) an additive magma; if ``None``, the magma
      will be inferred from the keys of the dictionary ``layers``
    - ``check`` -- (default:``True``) a boolean; if ``True``, verify that the
      layers span the full Lie algebra, are disjoint, and respect the bracket

    EXAMPLES:

    We define a grading of the non-abelian 2-dimensional Lie algebra over the
    integers::

        sage: from lie_gradings.gradings.lie_algebra_grading import grading
        sage: L.<X,Y> = LieAlgebra(QQ, {('X','Y'): {'Y': 1}})
        sage: grading(L, {0: [X], 1: [Y]})
        Grading over Integer Ring of Lie algebra on 2 generators (X, Y) over
        Rational Field with nonzero layers
          1 : (Y,)
          0 : (X,)

    The grading does not have to consist of only elements of the basis::

        sage: grading(L, {0: [X + 2*Y], 1: [5*Y]})
        Grading over Integer Ring of Lie algebra on 2 generators (X, Y) over
        Rational Field with nonzero layers
          1 : (5*Y,)
          0 : (X + 2*Y,)

    A grading can be defined over any additive magma::

        sage: sc = {('X','Y'): {'Z': 1}, ('X','Z'): {'W': 1}}
        sage: L.<X,Y,Z,W> = LieAlgebra(QQ, sc)
        sage: A = AdditiveAbelianGroup([2, 0])
        sage: gr = grading(L, {(1,0): [X], (0,1): [Y,W], (1,1): [Z]}, magma = A)
        sage: gr
        Grading over Additive abelian group isomorphic to Z/2 + Z of Lie algebra
        on 4 generators (X, Y, Z, W) over Rational Field with nonzero layers
          (0, 1) : (W, Y)
          (1, 0) : (X,)
          (1, 1) : (Z,)

    If the keys of the layer dictionary correspond to the same element of the
    indexing magma, the layers are combined::

        sage: layers = {(1,0): [X], (0,1): [Y], (1,1): [Z], (2,1): [W]}
        sage: gr2 = grading(L, layers, magma = A)
        sage: gr2
        Grading over Additive abelian group isomorphic to Z/2 + Z of Lie algebra
        on 4 generators (X, Y, Z, W) over Rational Field with nonzero layers
          (0, 1) : (W, Y)
          (1, 0) : (X,)
          (1, 1) : (Z,)
        sage: gr == gr2
        True

    If the indexing is over tuples, by default it is assumed that the grading
    is over a free additive abelian group::

        sage: layers = {(1,0): [X], (0,1): [Y], (1,1): [Z], (2,1): [W]}
        sage: gr = grading(L, layers); gr
        Grading over Additive abelian group isomorphic to Z + Z of Lie algebra
        on 4 generators (X, Y, Z, W) over Rational Field with nonzero layers
          (1, 0) : (X,)
          (0, 1) : (Y,)
          (1, 1) : (Z,)
          (2, 1) : (W,)

    The layers may be accessed with Python list syntax::

        sage: gr[(1,1)]
        (Z,)

    Empty layers may also be retrieved as long as the element belongs to
    the correct magma::

        sage: gr[(1,2)]
        ()
        sage: gr[(1,1,1)]
        Traceback (most recent call last):
        ...
        IndexError: (1, 1, 1) is not an element of Additive abelian group isomorphic to Z + Z

    TESTS:

    Test a grading where `a<c` if `a+b=c` is not a partial order::

        sage: L.<X_1, X_2, X_12, X_112, X_122> = LieAlgebra(QQ, 2, step=3)
        sage: gr = grading(L, {-1: [X_2, X_122], 0: [X_12], 1: [X_1, X_112]})
        sage: TestSuite(gr).run()

    Run test suites::

        sage: sc = {('X','Y'): {'Z': 1}, ('X','Z'): {'W': 1}}
        sage: L.<X,Y,Z,W> = LieAlgebra(QQ, sc)
        sage: A = AdditiveAbelianGroup([2,0])
        sage: gr = grading(L, {(1,0): [X], (0,1): [Y,W], (1,1): [Z]}, magma = A)
        sage: TestSuite(gr).run()
    """

    @staticmethod
    def __classcall_private__(cls, layers, lie_algebra=None, magma=None,
                             projections=False, check=True, sc=None, **kwds):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y> = LieAlgebra(QQ, {('X','Y'): {'Y': 1}})
            sage: gr1 = grading(L, {0: [X], 2: [Y]}, magma=GF(2))
            sage: gr2 = grading(L, {0: [X, Y]}, magma=GF(2))
            sage: gr1 is gr2
            True
        """
        if not layers:
            raise ValueError("a grading must have layers")

        layers = dict(layers)
        if not magma:
            # infer indexing magma from layer indices
            if (all(isinstance(a, tuple) for a in layers.keys())
                or all(isinstance(a, list) for a in layers.keys())):
                # if everything is a tuple or list, assume Z^k
                k = next(iter(layers.keys()))
                magma = AdditiveAbelianGroup([0] * len(k))
            else:
                cm = get_coercion_model()
                magma = cm.common_parent(*layers.keys())
        if not lie_algebra:
            # infer Lie algebra being graded from layer elements
            cm = get_coercion_model()
            layer_elems = sum((list(layer) for layer in layers.values()), [])
            lie_algebra = cm.common_parent(*layer_elems)

        # combine layers with identical keys after coercion to magma
        newlayers = {}
        for a in layers:
            if not layers[a]:
                # remove empty layers
                continue
            ma = magma(a)
            if ma not in newlayers:
                newlayers[ma] = []
            newlayers[ma].extend((lie_algebra(X) for X in layers[a]))

        strkey = lambda s: str(s)
        layertuple = tuple((a, tuple(sorted(newlayers[a], key=strkey)))
                           for a in sorted(newlayers, key=strkey))

        # Lie algebras are hashed based on their string representation,
        # so if the only way two gradings differ is in the internal structure
        # of the Lie algebras, UniqueRepresentation may fail.
        # Include the structure coefficients when possible to mitigate this.
        try:
            sc = lie_algebra.structure_coefficients()
        except AttributeError:
            sc = None

        return super(LieAlgebraGrading, cls).__classcall__(cls, layertuple,
                            lie_algebra, magma, projections, check, sc, **kwds)

    def __init__(self, layers, lie_algebra, magma,
                 projections, check, sc, **kwds):
        r"""
        Initialize ``self``.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y> = LieAlgebra(QQ, {('X','Y'): {'Y': 1}})
            sage: gr = grading(L, {0: [X], 1: [Y]})
            sage: TestSuite(gr).run()
        """

        self._L = lie_algebra
        self._A = magma
        self._layers = dict(layers)
        self._projections = projections

        if check:
            # verify validity of grading
            self._test_direct_sum()
            self._test_grading()

        # if it is well defined, initialize the poset of weights
        # where a<c if a!=0 and there exists b!=0 such that a+b=c
        els = tuple(self._layers.keys())
        rels = [(a, c) for a in els for b in els
                for c in els if a + b == c and a and b]
        try:
            self._weight_poset = Poset([els, rels])
        except ValueError:
            self._weight_poset = None

        C = Sets()
        Parent.__init__(self, base=self._L.base_ring(), category=C)

    def __iter__(self):
        r"""
        Iterate over the layers of the grading.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z': 1}})
            sage: gr = grading(L, {2: [X], 4: [Y], 6: [Z]})
            sage: [a for a in gr]
            [2, 4, 6]

        TESTS:

            Verify that elements are not iterated through twice
            even if they are successors at two different depths::

                sage: sc = {('X_1','X_2'): {'X_3':1},
                ....:       ('X_1','X_3'): {'X_6':1},
                ....:       ('X_4','X_5'): {'X_6':1}}
                sage: L.<X_1,X_2,X_3,X_4,X_5,X_6> = LieAlgebra(QQ, sc)
                sage: layers = {(0,1,0): [X_1], (0,0,1): [X_2],
                ....:           (0,1,1): [X_3], (0,2,1): [X_6],
                ....:          (-1,2,1): [X_4], (1,0,0): [X_5]}
                sage: magma = AdditiveAbelianGroup([0,0,0])
                sage: gr = grading(L, layers, magma)
                sage: len([a for a in gr]) == 6
                True
        """
        if self._weight_poset is None:
            for a in sorted(self._layers.keys()):
                yield a
            return

        for a in self._weight_poset:
            yield a

    def __contains__(self, a):
        r"""
        Check if ``a`` is a layer of the grading.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z': 1}})
            sage: gr = grading(L, {1: [X], 2: [Y], 3: [Z]})
            sage: 1 in gr
            True
            sage: 3 in gr
            True
            sage: 5 in gr
            False
            sage: 1/2 in gr
            False
        """
        return a in self._A and self._A(a) in self._layers

    def __getitem__(self, a):
        r"""
        Return the layer indexed by the element ``a`` of the grading magma.

        INPUT:

        - ``a`` -- an element of the additive magma the grading is defined over

        EXAMPLES:

        Convenience notation to get the layer indexed by an element::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y> = LieAlgebra(QQ, {('X','Y'): {'Y': 1}})
            sage: gr = grading(L, {0: [X], 1: [Y]})
            sage: gr[0]
            (X,)

        If the element belongs to the grading magma, but no such layer exists,
        the empty list is returned, corresponding to `\mathfrak{g}_a = \{0\}`::

            sage: gr[3]
            ()

        If the element is not in the grading magma, an error is raised::

            sage: gr[sqrt(2)]
            Traceback (most recent call last):
            ...
            IndexError: sqrt(2) is not an element of Integer Ring
        """
        if a not in self:
            if a not in self._A:
                raise IndexError("%s is not an element of %s" % (a, self._A))
            return ()
        return self._layers[self._A(a)]

    def _repr_(self):
        r"""
        Return a string representation of ``self``.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y> = LieAlgebra(QQ, {('X','Y'): {'Y': 1}})
            sage: grading(L, {0: [X], 1: [Y]})
            Grading over Integer Ring of Lie algebra on 2 generators (X, Y) over
            Rational Field with nonzero layers
              1 : (Y,)
              0 : (X,)
        """
        str = "Grading over %s of %s with nonzero layers\n" % (self._A, self._L)
        for a in self:
            la = self._layers[a]
            str += "  %s : %s\n" % (a, la)
        return str

    def _latex_(self):
        r"""
        Return a latex representation of ``self``.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Y': 1}})
            sage: latex(grading(L, {0: [X], 1: [Y,Z]}))
            \langle X \rangle \oplus \langle Y, Z \rangle
        """
        layer_strs = []
        for a, la in self._layers.items():
            layer_str = ", ".join(latex(X) for X in la)
            layer_strs.append("\\langle %s \\rangle" % layer_str)
        return " \\oplus ".join(layer_strs)

    def _an_element_(self):
        r"""
        Return an element of the ``self``.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Y': 1}})
            sage: gr = grading(L, {0: [X], 1: [Y,Z]})
            sage: a = gr.an_element(); a
            0
            sage: gr[a]
            (X,)
        """
        return list(self._layers.keys())[0]

    def lie_algebra(self):
        r"""
        Return the underlying Lie algebra.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y> = LieAlgebra(QQ, {('X','Y'): {'Y': 1}})
            sage: gr = grading(L, {0: [X], 1: [Y]})
            sage: gr.lie_algebra() == L
            True
        """
        return self._L

    def has_equal_layers(self, other):
        r"""
        Return if ``self`` has the same layers as ``other`` ignoring indexing.

        INPUT:

        - ``other`` -- a :class:`LieAlgebraGrading`

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z': 1}})
            sage: gr1 = grading(L, {1: [X], 2: [Y], 3: [Z]})
            sage: gr2 = grading(L, {(1,0): [X], (0,1): [Y], (1,1): [Z]})
            sage: gr1.has_equal_layers(gr2)
            True

        The basis in which the layer is described is irrelevant::

            sage: gr1 = grading(L, {0: [X], 1: [Y+Z, Y-Z]})
            sage: gr2 = grading(L, {0: [X], 1: [Y, Z]})
            sage: gr1.has_equal_layers(gr2)
            True

        The gradings must have the same underlying Lie algebra::

            sage: K.<A,B,C> = LieAlgebra(QQ, {('C','A'): {'B': 1}})
            sage: gr3 = grading(K, {0: [A], 1: [B, C]})
            sage: gr1.has_equal_layers(gr3)
            Traceback (most recent call last):
            ...
            ValueError: the gradings must have the same Lie algebra
        """
        if self._L != other._L:
            raise ValueError("the gradings must have the same Lie algebra")
        layer_modules = [self.layer_module(a) for a in self]
        for a in other:
            m = other.layer_module(a)
            if m not in layer_modules:
                return False

        return True

    def magma(self):
        r"""
        Return the magma indexing the layers.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y> = LieAlgebra(QQ, {('X','Y'): {'Y': 1}})
            sage: gr = grading(L, {0: [X], 1: [Y]})
            sage: gr.magma()
            Integer Ring
            sage: gr2 = grading(L, {0: [X], 1/2: [Y]})
            sage: gr2.magma()
            Rational Field
        """
        return self._A

    def layers(self):
        r"""
        Return the dictionary of layers of the grading.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y> = LieAlgebra(QQ, {('X','Y'): {'Y': 1}})
            sage: gr = grading(L, {0: [X], 1: [Y]})
            sage: gr.layers()
            {0: (X,), 1: (Y,)}
        """
        return self._layers

    @cached_method
    def layer_module(self, a):
        r"""
        Return layer ``a`` as a submodule of the module of the Lie algebra.

        INPUT:

        - ``a`` -- a layer of the grading

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z': 1}})
            sage: gr = grading(L, {1: [X,Y], 2: [Z]})
            sage: gr.layer_module(1)
            Sparse vector space of degree 3 and dimension 2 over Rational Field
            User basis matrix:
            [1 0 0]
            [0 1 0]
        """
        m = self._L.module()
        return m.submodule_with_basis([X.to_vector() for X in self[a]])

    def get_layer(self, X):
        r"""lueError: the dimension of the layer (X,) does not match the dimension of the layer (X, Z)
        Return the layer containing the vector ``X``.

        INPUT:

        - ``X`` -- an element of the Lie algebra

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y> = LieAlgebra(QQ, {('X','Y'): {'Y': 1}})
            sage: gr = grading(L, {0: [X], 1: [Y]})
            sage: gr.get_layer(X)
            0
            sage: gr.get_layer(Y)
            1
            sage: gr.get_layer(X+Y)
            Traceback (most recent call last):
            ...
            ValueError: the element X + Y is not contained in any single layer
        """
        v = X.to_vector()
        for a in self:
            if v in self.layer_module(a):
                return a
        raise ValueError("the element %s is not contained in any single layer" % X)

    def generating_weights(self):
        r"""
        Return a subset of weights generating all other weights.

        A set of elements `a_1,\ldots a_k` of the grading magma is called
        generating, if each layer `\mathfrak{g}_{a_k}` of the grading is
        non-zero, and for every other non-zero layer `\mathfrak{g}_{b}`, the
        element `b` is contained in the submagma of weights generated by
        `a_1,\ldots a_k`. That is, every such element `b` can be written as
        repeated pairwise addition, e.g., `b = (a_1+a_2) + ((a_2+a_3)+a_4)`
        with all the layers `\mathfrak{g}_{a_1+a_2}` etc nonzero.

        EXAMPLES:

        If the relation `a<c` whenever `a+b=c` defines a partial order on the
        weights, then the minimal elements with respect to the partial order
        form a minimal generating set::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y,Z,W> = LieAlgebra(QQ, {('X','Y'): {'Z': 1}})
            sage: lrs = {1: [X], sqrt(2): [Y], 1+sqrt(2): [Z], 3+sqrt(2): [W]}
            sage: gr = grading(L, lrs, magma=AA)
            sage: gr.generating_weights()
            [1, 1.414213562373095?, 4.414213562373095?]

        Otherwise, the returned generating set is the full set of weights::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: sc = {('X','Y'): {'Z': 1}, ('X','Z'): {'W': 1}}
            sage: L.<X,Y,Z,W> = LieAlgebra(QQ, sc)
            sage: layers = {(1,0): [X], (0,1): [Y,W], (1,1): [Z]}
            sage: A = AdditiveAbelianGroup([2, 0])
            sage: gr = grading(L, layers, magma = A)
            sage: gr.generating_weights()
            [(0, 1), (1, 0), (1, 1)]
        """
        if self._weight_poset is None:
            return [a for a in self]
        else:
            return sorted(self._weight_poset.minimal_elements())

    def is_refinement(self, grading):
        r"""
        Return whether ``self`` is a refinement of another grading.

        Returns ``True`` if all layers of the comparison grading ``grading``
        are unions of the layers of ``self`` and ``False`` otherwise.

        INPUT:

        - ``grading`` -- the other grading to compare to

        EXAMPLES:

        A maximal grading is a refinement of all other gradings over torsion
        free abelian groups::

            sage: from lie_gradings.gradings.grading import maximal_grading, torsion_free_gradings
            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y,Z> = LieAlgebra(ZZ, {('X','Y'): {'Z':1}})
            sage: maxgrading = maximal_grading(L)
            sage: gradings = torsion_free_gradings(L)
            sage: all(maxgrading.is_refinement(gr) for gr in gradings)
            True

        Not all gradings are comparable in either direction::

            sage: gr1 = grading(L, {0: [X], 1: [Y, Z]})
            sage: gr2 = grading(L, {0: [Y], 1: [X, Z]})
            sage: gr1.is_refinement(gr2)
            False
            sage: gr2.is_refinement(gr1)
            False

        Every grading is a refinement of itself::

            sage: gr1.is_refinement(gr1)
            True

        The layers of the gradings do not have to be given in the same basis::

            sage: gr1 = grading(L, {0: [X, Y, Z]})
            sage: gr2 = grading(L, {0: [Y], 1: [X+Z, Z]})
            sage: gr2.is_refinement(gr1)
            True

        Trying to compare gradings of different Lie algebras raises an error::
            sage: L2.<A,B,C> = LieAlgebra(QQ, 3, abelian=True)
            sage: gr3 = grading(L2, {0: [A, B, C]})
            sage: gr1.is_refinement(gr3)
            Traceback (most recent call last):
            ...
            ValueError: gradings of different Lie algebras cannot be compared
        """
        if self._L != grading._L:
            raise ValueError("gradings of different Lie algebras cannot be compared")

        # define subspaces spanned by layers
        m = self._L.module()
        spaces = [m.submodule(X.to_vector() for X in l)
                  for l in self._layers.values()]
        otherspaces = [m.submodule(X.to_vector() for X in l)
                       for l in grading._layers.values()]
        for sm in spaces:
            if not any(sm.is_submodule(sm2) for sm2 in otherspaces):
                return False
        return True

    def lie_algebra_in_adapted_basis(self, names, simplify_basis=True,
                                     category=None):
        r"""
        Return an isomorphic copy of the underlying Lie algebra with a
        basis that is adapted to the grading.

        INPUT:

        - ``names`` -- list of strings to use as names for the new basis
        - ``simply_basis`` -- (default:``True``) a boolean; if ``True`` attempt
          to find a basis with simpler structure coefficients

        EXAMPLES:

        We compute a change of basis through defining a grading::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y,Z> = LieAlgebra(ZZ, {('X','Y'): {'Y':1, 'Z':1}})
            sage: gr = grading(L, {0: [X], 1: [Y, Y+Z]}); gr
            Grading over Integer Ring of Lie algebra on 3 generators (X, Y, Z)
            over Integer Ring with nonzero layers
              1 : (Y, Y + Z)
              0 : (X,)
            sage: K.<A,B,C> = gr.lie_algebra_in_adapted_basis(); K
            Lie algebra on 3 generators (A, B, C) over Integer Ring
            sage: K[A,C]
            -B
        """
        basis = []
        for a in self:
            la = self[a]
            basis.extend(la)

        R = self._L.base_ring()
        C = LieAlgebras(R).FiniteDimensional().WithBasis()
        C = C.or_subcategory(category)

        return in_new_basis(self._L, basis, names, category=C)

    @cached_method
    def has_positive_realization(self):
        r"""
        Return whether the grading has a realization over the positive integers.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L = lie_algebras.Heisenberg(QQ, 1)
            sage: X,Y,Z = L.basis()
            sage: A = AdditiveAbelianGroup([0,0])
            sage: layers = {(1,0): [X], (0,1): [Y], (1,1): [Z]}
            sage: gr = grading(L, layers, magma=A)
            sage: gr.has_positive_realization()
            True
        """
        try:
            if self._projections:
                # if there is torsion, there is no integer realization
                if any(a != 0 for a in self._A.invariants()):
                    return False

                # grading is positivisable iff zero
                # is not in the convex hull of weights
                p = Polyhedron([tuple(a) for a in self])
                return not (tuple(self._A.zero()) in p)
        except:
            pass

        # if projection property is not known, compute a universal realization
        gr = self.universal_realization()
        return gr.has_positive_realization()

    @cached_method
    def to_positive_grading(self, optimize_weights=True):
        r"""
        Return a grading with identical layers, but indexed over the positive
        integers.

        INPUT:

        - ``optimize_weights`` -- (default:``True``) a boolean; if ``True``,
          the returned positive realization has the smallest possible max weight

        EXAMPLES:

        We compute a positive grading for the Heisenberg Lie algebra::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L = lie_algebras.Heisenberg(QQ, 1)
            sage: X,Y,Z = L.basis()
            sage: A = AdditiveAbelianGroup([0,0])
            sage: layers = {(1,0):[X], (0,2):[Y], (1,2):[Z]}
            sage: gr = grading(L, layers, magma=A, projections=True)
            sage: gr.to_positive_grading()
            Grading over Integer Ring of Heisenberg algebra of rank 1 over
            Rational Field with nonzero layers
              1 : (p1,)
              2 : (q1,)
              3 : (z,)

        Not all gradings can be indexed over the positive integers. A simple
        example is found in the product of the Heisenberg algebra with itself::

            sage: sc = {('A','B'): {'C': 1}, ('X','Y'): {'Z': 1}}
            sage: L.<A,B,C,X,Y,Z> = LieAlgebra(QQ, sc)
            sage: layers = {(1,0):[X], (-1,0):[A], (0,1):[Y, C], (1,1):[Z, B]}
            sage: gr = grading(L, layers, magma=AdditiveAbelianGroup([0,0]))
            sage: gr.to_positive_grading()
            Traceback (most recent call last):
            ...
            ValueError: grading does not have a realization over positive integers

        Not optimizing the weights gives a much quicker computation but
        unnecessarily large weights::

            sage: from lie_gradings.gradings.grading import maximal_grading
            sage: L = LieAlgebra(QQ, 3, step=3)
            sage: gr = maximal_grading(L)
            sage: gr.to_positive_grading(optimize_weights=False)
            Grading over Integer Ring of Free Nilpotent Lie algebra
            on 14 generators (X_1, X_2, X_3, X_12, X_13, X_23,
            X_112, X_113, X_122, X_123, X_132, X_133, X_223, X_233)
            over Rational Field with nonzero layers
              36 : (X_3,)
              30 : (X_2,)
              66 : (X_23,)
              96 : (X_223,)
              102 : (X_233,)
              28 : (X_1,)
              58 : (X_12,)
              86 : (X_112,)
              88 : (X_122,)
              64 : (X_13,)
              92 : (X_113,)
              94 : (X_123, X_132)
              100 : (X_133,)
        """
        ugr = self.universal_realization()
        if ugr.has_positive_realization() != True:
             raise ValueError("grading does not have a realization over positive integers")

        # define a linear problem solver
        if optimize_weights:
            p = MixedIntegerLinearProgram(solver="PPL")
            v = p.new_variable(integer=True)
            obj = p.new_variable()
            p.set_objective(-obj[0])
        else:
            p = MixedIntegerLinearProgram()
            v = p.new_variable()
            p.set_objective(None)

        # define a helper function for inner products
        def ip(w, a):
            return sum(wk * ak for wk, ak in zip(w, a))

        # add positivity constraints
        for a in ugr:
            tup = tuple(a)
            constr = sum(ck * v[k] for k, ck in enumerate(tup))
            p.add_constraint(constr >= 1)
            if optimize_weights:
                p.add_constraint(obj[0] >= constr)
        K = len(tup)

        # compute a norm bound for weights and weight differences
        M = 0
        for a in ugr:
            anorm = max(abs(ak) for ak in a)
            if anorm > M:
                M = anorm
        for a, b in combinations(ugr, 2):
            abnorm = max(abs(ak) for ak in a - b)
            if abnorm > M:
                M = abnorm
        M = M + 1

        if optimize_weights:
            # compute a priori bounds for the solution
            N = len(ugr._layers)
            C = 2 * (1 + N * 2 ** N) * M ** K + M ** (K + 1)

            # add constraints for distinct weights
            vvec = [v[k] for k in range(K)]
            d = p.new_variable(binary=True)
            for (i, a), (j, b) in combinations(enumerate(ugr), 2):
                dif = ip(vvec, a - b)
                p.add_constraint(dif - (C + 1) * d[i, j], min=-C)
                p.add_constraint(dif - (C + 1) * d[i, j], max=-1)

            # solve the linear problem
            p.solve()
            sol = p.get_values(v)
            w = [ZZ(sol[k]) for k in range(K)]
        else:
            # solve and perturb
            p.solve()
            sol = p.get_values(v)
            w = vector(QQ, [QQ(sol[k]) for k in range(K)])

            # expand to an integer solution and rescale
            scale = 1 / gcd(w)
            scale = lcm(scale, M ** K)
            w = scale * w + vector([M ** k for k in range(K)])

        # return the pushforward grading
        newlayers = {ip(w, a):ugr[a] for a in ugr}
        return grading(ugr._L, newlayers, magma=ZZ)

    @cached_method
    def to_integer_grading(self, require_identical=True):
        r"""
        Return a grading indexed over the integers, mimicking the layers as
        closely as possible.

        INPUT:

        - ``require_identical`` -- (default:``True``) a boolean; if ``True``,
          the grading over the integers will have exactly the same layers as
          the original, or an error will be raised. Otherwise layers will be
          combined as necessary.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y,Z,W> = LieAlgebra(QQ, {('X','Y'): {'Z': 1}})
            sage: lrs = {1: [X], sqrt(2): [Y], 1+sqrt(2): [Z], 2+sqrt(2): [W]}
            sage: gr = grading(L, lrs, magma=AA)
            sage: gr.to_integer_grading()
            Grading over Integer Ring of Lie algebra on 4 generators
            (X, Y, Z, W) over Rational Field with nonzero layers
              1 : (X,)
              2 : (Y,)
              3 : (Z,)
              4 : (W,)
        """
        if self._A == ZZ:
            return self

        zk_grading = self.universal_realization()
        if any(a != 0 for a in zk_grading.magma().invariants()):
            if require_identical:
                raise ValueError("gradings does not have a realization over the integers")
            zk_grading = zk_grading.torsion_free_coarsening()

        # form difference set of weights
        diffset = set(a - b for a, b in combinations(zk_grading._layers, 2))

        # find simplest projection which is not orthogonal to any element
        # of the difference set, i.e. does not combine any layers
        k = len(zk_grading._A.gens())
        n = 1
        while True:
            for iv in IntegerVectors(n, k, min_part=1):
                if gcd(iv) > 1:
                    # multiple of something tested earlier
                    continue
                for d in diffset:
                    innerprod = sum(ivk * dk for ivk, dk in zip(iv, d))
                    if not innerprod:
                        break
                else:
                    # direction not orthogonal to any element of the diff set
                    # define projection grading
                    newlayers = {sum(ivk * ak for ivk, ak in zip(iv, a)):
                            zk_grading._layers[a] for a in zk_grading._layers}
                    return grading(self._L, newlayers, magma=ZZ)
            n += 1

    @cached_method
    def torsion_free_coarsening(self):
        r"""
        Return a coarsening of the grading indexed over a torsion free group.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: sc = {('X','Y'): {'Z': 1}, ('X','Z'): {'W': 1}}
            sage: L.<X,Y,Z,W> = LieAlgebra(QQ, sc)
            sage: layers = {(1,0): [X], (0,1): [Y,W], (1,1): [Z]}
            sage: A = AdditiveAbelianGroup([2, 0])
            sage: gr = grading(L, layers, magma = A)
            sage: gr.torsion_free_coarsening()
            Grading over Additive abelian group isomorphic to Z of Lie algebra
            on 4 generators (X, Y, Z, W) over Rational Field with nonzero layers
              (1) : (W, Y, Z)
              (0) : (X,)
        """
        ugr = self.universal_realization()
        tfcomps = [i for i, inv in enumerate(ugr._A.invariants()) if inv == 0]
        newlayers = {}
        for a in ugr:
            ta = tuple(a)
            b = tuple(ta[i] for i in tfcomps)
            if b not in newlayers:
                newlayers[b] = []
            newlayers[b].extend(ugr[a])
        A = AdditiveAbelianGroup([0] * len(tfcomps))
        return grading(self._L, newlayers, magma=A)

    @cached_method
    def universal_realization(self):
        r"""
        Return the universal realization of the grading.

        EXAMPLES:

        The universal realization of a grading preserves only those relations
        `a+b=c` where `0\neq [\mathfrak{g}_a,\mathfrak{g}_b] = \mathfrak{g}_c`::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: L.<X,Y,Z,W> = LieAlgebra(QQ, {('X','Y'): {'Z': 1}})
            sage: lrs = {1: [X], sqrt(2): [Y], 1+sqrt(2): [Z], 3+sqrt(2): [W]}
            sage: gr = grading(L, lrs, magma=AA)
            sage: gr.universal_realization()
            Grading over Additive abelian group isomorphic to Z + Z + Z
            of Lie algebra on 4 generators (X, Y, Z, W) over Rational Field
            with nonzero layers
              (1, 0, 0) : (W,)
              (0, 1, 0) : (Y,)
              (0, 0, 1) : (X,)
              (0, 1, 1) : (Z,)

        A universal realization can have torsion::

            sage: sc = {('X','Y'): {'Z': 1}, ('X','Z'): {'W': 1}}
            sage: L.<X,Y,Z,W> = LieAlgebra(QQ, sc)
            sage: layers = {(1,0): [X], (0,1): [Y,W], (1,1): [Z]}
            sage: A = AdditiveAbelianGroup([2, 0])
            sage: gr = grading(L, layers, magma = A)
            sage: gr.universal_realization()
            Grading over Additive abelian group isomorphic to Z/2 + Z
            of Lie algebra on 4 generators (X, Y, Z, W) over Rational Field
            with nonzero layers
              (0, 1) : (W, Y)
              (1, 0) : (X,)
              (1, 1) : (Z,)

        The grading must be defined over an additive abelian group::

            sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z': 1}})
            sage: A = CommutativeAdditiveSemigroups().example(); A
            An example of a commutative monoid: the free commutative monoid
            generated by ('a', 'b', 'c', 'd')
            sage: a,b,c,d=A.additive_semigroup_generators()
            sage: gr = grading(L, {a:[X],b:[Y],a+b:[Z]})
            sage: gr.universal_realization()
            Traceback (most recent call last):
            ...
            ValueError: the grading must be defined over an additive abelian group
        """
        if self._A not in CommutativeAdditiveGroups():
            raise ValueError("the grading must be defined over an additive abelian group")

        # form a linear system over Z of the relations between the weights
        # reversing the list leads to a cleaner quotient
        weights = list(reversed([a for a in self]))
        V = FreeModule(ZZ, len(weights))
        relations = []
        for i, j in combinations_with_replacement(range(len(weights)), 2):
            c = weights[i] + weights[j]
            if c in self:
                # add relation
                h = weights.index(c)
                rel = [0] * len(weights)
                rel[i] += 1
                rel[j] += 1
                rel[h] -= 1
                relations.append(V(rel))

        # quotient out by the relations to get a well defined grading
        Q = V.quotient(relations)

        layer_labels = [tuple(Q(x)) for x in V.basis()]

        newgrading = {}
        for a, label in zip(weights, layer_labels):
            if label not in newgrading:
                newgrading[label] = []
            newgrading[label].extend(self[a])

        k = len(Q.gens())
        invs = Q.invariants()
        return grading(self._L, newgrading, magma=AdditiveAbelianGroup(invs),
                       projections=True)

    def isomorphism_equations(self, other, weight_map, reduced=False):
        r"""
        Return an implicit isomorphism to another grading for a specified
        map between the weights.

        INPUT:

        - ``other`` -- the target :class:`LieAlgebraGrading`
        - ``weight_map`` -- a dictionary {a:b}, meaning that self[a] should get
          mapped to other[b]. Must be a homomorphism on weights.
        - ``reduced`` -- (default:``True``) a boolean; if ``True``, dependent
          variables will be attempted to be eliminated from the descriptions
          of the layer maps.

        OUTPUT:

        A pair ({a: (b,A)}, I) of a dictionary and an ideal, where

        - a are the weights of self
        - b are the image weights ``weight_map[a]``
        - A is a matrix of the map self[a] -> other[b] in the respective bases
          given in terms of polynomial indeterminates
        - I is an ideal of restrictions on the indeterminates

        The ideal I is defined in a polynomial ring with variables of the form
        s_i and ai_jk. The ai_jk are the variables appearing in the coefficients
        of the matrices and the s_i variables are dummy variables used to
        capture the requirement that the matrices be invertible.

        EXAMPLES:

        By default, all the matrices have indeterminate coefficients::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: sc = {('X','Y'): {'Z': 1}}
            sage: L.<X,Y,Z> = LieAlgebra(QQ, sc)
            sage: gr1 = grading(L, {1: [X], 2: [Y], 3: [Z]})
            sage: gr2 = grading(L, {1: [Y], 2: [X], 3: [Z]})
            sage: weightmap = {1:1, 2:2, 3:3}
            sage: d,I = gr1.isomorphism_equations(gr2, weightmap)
            sage: d[1][1]
            [a1_11]
            sage: d[2][1]
            [a2_11]
            sage: d[3][1]
            [a3_11]
            sage: I
            Ideal (s_1*a1_11 - 1, s_2*a2_11 - 1, s_3*a3_11 - 1,
            a3_11 + a1_11*a2_11) of Multivariate Polynomial Ring
            in s_1, s_2, s_3, a1_11, a2_11, a3_11 over Rational Field

        Using reduced=``True`` attempts to find a simplified system
        with fewer variables::

            sage: d,I = gr1.isomorphism_equations(gr2, weightmap, reduced=True)
            sage: d[1][1]
            [a1_11]
            sage: d[2][1]
            [a2_11]
            sage: d[3][1]
            [-a1_11*a2_11]
            sage: I
            Ideal (s_1*a1_11 - 1, s_2*a2_11 - 1, -s_3*a1_11*a2_11 - 1) of
            Multivariate Polynomial Ring in s_1, s_2, s_3, a1_11, a2_11
            over Rational Field

        If the layer dimensions do not match an error is raised::

            sage: gr1.isomorphism_equations(gr2, {1:2, 2:3, 3:4})
            Traceback (most recent call last):
            ...
            ValueError: the dimension of the layer (Z,) does not match the dimension of the layer ()

        If there is no isomorphism of the Lie algebra mapping the layers in
        the correct way, then the constraints of the ideal are impossible::

            sage: L.<A,B,C,X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z': 1}})
            sage: gr1 = grading(L, {0: [X,Y,Z], 1: [A,B,C]})
            sage: gr2 = grading(L, {0: [X,A,B], 1: [Y,Z,C]})
            sage: d,I = gr1.isomorphism_equations(gr2, {0:0, 1:1})
            sage: d[0][1]
            [a2_11 a2_12 a2_13]
            [a2_21 a2_22 a2_23]
            [a2_31 a2_32 a2_33]
            sage: d[1][1]
            [a1_11 a1_12 a1_13]
            [a1_21 a1_22 a1_23]
            [a1_31 a1_32 a1_33]
            sage: 1 in I
            True

        In such a case, the reduced form gives zero maps::

            sage: d,I = gr1.isomorphism_equations(gr2, {0:0, 1:1}, reduced=True)
            sage: d[0][1]
            [0 0 0]
            [0 0 0]
            [0 0 0]
        """
        # define variables for the generic maps of each layer
        # in the polynomial ring, use a block term order separating the layers
        anames = []
        invnames = []
        dims = []
        to_blocks = []
        i = 1

        # these parameters control how the term order is constructed
        # and hence how the system will be reduced
        reverse_blocks = False
        order_type = 'negdeglex'

        # ensure the weight_map dictionary contains elements of the correct type
        self_A = self.magma()
        other_A = other.magma()
        weight_map = {self_A(a):other_A(b) for a, b in weight_map.items()}

        for a in self:
            b = weight_map[a]
            a_basis = self[a]
            b_basis = other[b]
            n = len(a_basis)
            if n != len(b_basis):
                raise ValueError("the dimension of the layer %s does not match the dimension of the layer %s" % (a_basis, b_basis))
            newvars = ['a%d_%d%d' % (i, r + 1, c + 1) for r in range(n)
                                                      for c in range(n)]
            if reverse_blocks:
                anames = newvars + anames
                invnames = ['s_%d' % i] + invnames
                dims = [n] + dims
                to_blocks = TermOrder(order_type, n * n) + toblocks
            else:
                invnames.append('s_%d' % i)
                anames += newvars
                dims.append(n)
                to_blocks.append(TermOrder(order_type, n * n))

            i += 1

        m = len(invnames)
        s_to = TermOrder('degrevlex', m)
        to = sum(to_blocks, s_to)
        PR = PolynomialRing(self._L.base_ring(), invnames + anames, order=to)

        # use the polynomial ring variables to define indeterminate matrices
        invvars = PR.gens()[:m]
        inv_eqs = []
        i = m
        A_list = []
        a_blocks = []
        for iv, d in zip(invvars, dims):
            avars = PR.gens()[i:i + d * d]
            A = matrix(PR, d, d, avars)
            # add the constraint that A must be invertible
            inveq = iv * A.det() - 1
            if reverse_blocks:
                A_list = [A] + A_list
                inv_eqs = [inveq] + inv_eqs
                a_blocks = [avars] + a_blocks
            else:
                A_list.append(A)
                inv_eqs.append(inveq)
                a_blocks.append(avars)
            i += d * d

        isom_maps = {a: (weight_map[a], A) for a, A in zip(self, A_list)}

        adapted_basis = sum((list(enumerate(self[a])) for a in self), [])
        # compute constraints from all brackets of the Lie algebra
        constraints = []
        for (i, X), (j, Y) in combinations(adapted_basis, 2):
            aX = self.get_layer(X)
            aY = self.get_layer(Y)
            imX = isom_maps[aX][1].column(i)
            imY = isom_maps[aY][1].column(j)

            # write the bracket [X,Y] in the adapted basis and compute im[X,Y]
            Z = X.bracket(Y)
            aZ = aX + aY
            if aZ not in self:
                # by assumption the weight_map is a homomorphism, so both
                # self[aZ] and other[weight_map[aZ]] are zero spaces
                # and there is no constraint
                continue
            Zc = self.layer_module(aZ).coordinate_vector(Z.to_vector())
            A = isom_maps[aZ][1]
            imZ = sum(zk * A.column(k) for k, zk in enumerate(Zc))

            # compute the bracket [imX,imY]
            bX = weight_map[aX]
            bY = weight_map[aY]
            bZ = weight_map[aZ]
            bZ_module = other.layer_module(bZ)
            V = FreeModule(PR, len(other[bZ]))
            imXY = V.zero()
            for k, imxk in enumerate(imX):
                for h, imyh in enumerate(imY):
                    brkt = other[bX][k].bracket(other[bY][h])
                    brktvec = V(bZ_module.coordinate_vector(brkt.to_vector()))
                    imXY += imxk * imyh * brktvec

            # add the constraint [imX,imY] = im[X,Y]
            constraints.extend((eq for eq in imZ - imXY if eq))

        I = PR.ideal(inv_eqs + constraints)

        if reduced:
            # use the ideal I to eliminate variables if possible
            substitutions = {}
            for ak in PR.gens()[m:]:
                ak_reduced = I.reduce(ak)
                if ak_reduced != ak:
                    substitutions[ak] = ak_reduced

            # compute a reduced polynomial ring and ideal
            new_to_blocks = []
            for to, avars in zip(to_blocks, a_blocks):
                new_count = len([a for a in avars if a not in substitutions])
                if new_count > 0:
                    new_to_blocks.append(TermOrder(order_type, new_count))
            new_to = sum(new_to_blocks, s_to)
            PR_reduced = PR.remove_var(*substitutions, order=new_to)

            eqs_reduced = []
            for eq in I.gens():
                eq_reduced = eq.subs(substitutions)
                if eq_reduced:
                    # block order breaks the default coercion, so cast via SR
                    new_eq = PR_reduced(SR(eq_reduced))
                    if new_eq not in eqs_reduced:
                        eqs_reduced.append(new_eq)
            I = PR_reduced.ideal(eqs_reduced)

            for a in self:
                b, A = isom_maps[a]
                Asub = A.subs(substitutions)
                # block order breaks the default coercion, so cast via SR
                A_reduced = matrix([[PR_reduced(SR(aij)) for aij in ai]
                                    for ai in Asub.rows()])
                isom_maps[a] = (b, A_reduced)

        return isom_maps, I

    def _test_direct_sum(self, **options):
        r"""
        Test that the layers are disjoint and span the Lie algebra.

        INPUT:

        - ``options`` -- any keyword arguments accepted by :meth:`_tester`.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: sc = {('X','Y'): {'Z': 1}, ('X','Z'): {'W': 1}}
            sage: L.<X,Y,Z,W> = LieAlgebra(QQ, sc)
            sage: gr = grading(L, {0: [Y], 1: [X, Z], 2: [W]}, check=False)
            sage: gr._test_direct_sum()
            sage: gr = grading(L, {0: [Y-W], 1: [X+Y, Z+W], 2: [W]}, check=False)
            sage: gr._test_direct_sum()
            sage: gr = grading(L, {0: [Y], 1: [Z], 2: [W]}, check=False)
            sage: gr._test_direct_sum()
            Traceback (most recent call last):
            ...
            AssertionError: the elements of the layers are not a basis of the Lie algebra
            sage: gr = grading(L, {1: [X,Y], 2: [Z], 3: [X+Y, W]}, check=False)
            sage: gr._test_direct_sum()
            Traceback (most recent call last):
            ...
            AssertionError: the elements of the layers are not a basis of the Lie algebra
            sage: L.<X,Y,Z,W> = LieAlgebra(ZZ, sc)
            sage: gr = grading(L, {1: [2*X,Y], 2: [Z], 3: [W]}, check=False)
            sage: gr._test_direct_sum()
            Traceback (most recent call last):
            ...
            AssertionError: the elements of the layers are not a basis of the Lie algebra


        See the documentation for :class:`TestSuite` for more information.
        """
        tester = self._tester(**options)
        rows = []
        for layer in self._layers.values():
            for X in layer:
                rows.append(X.to_vector())
        A = matrix(self._L.base_ring(), rows)
        tester.assertTrue(A.is_invertible(),
            msg="the elements of the layers are not a basis of the Lie algebra")

    def _test_grading(self, **options):
        r"""
        Test that the Lie bracket respects the grading.

        INPUT:

        - ``options`` -- any keyword arguments accepted by :meth:`_tester`.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: sc = {('X','Y'): {'Z': 1}, ('X','Z'): {'W': 1}}
            sage: L.<X,Y,Z,W> = LieAlgebra(QQ, sc)
            sage: A = Zmod(2)
            sage: gr = grading(L, {1: [X, Z], 0: [Y, W]}, magma=A, check=False)
            sage: gr._test_grading()
            sage: K.<X,Y> = LieAlgebra(QQ, {('X','Y'): {'Y': 1}})
            sage: A = AdditiveAbelianGroup([0, 0])
            sage: gr2 = grading(K, {(1,0):[X], (0,1):[Y]}, magma=A, check=False)
            sage: gr2._test_grading()
            Traceback (most recent call last):
            ...
            AssertionError: Lie bracket [Y, X] is not in the layer (1, 1)

        See the documentation for :class:`TestSuite` for more information.
        """
        tester = self._tester(**options)

        for a, b in combinations_with_replacement(self._layers, 2):
            ab_basis = self._layers.get(a + b, [])
            ab = self._L.module().submodule([X.to_vector() for X in ab_basis])
            for X in self._layers[a]:
                for Y in self._layers[b]:
                    Z = X.bracket(Y)
                    tester.assertTrue(Z.to_vector() in ab,
                        msg="Lie bracket [%s, %s] is not in the layer %s" %
                        (X, Y, a + b))
