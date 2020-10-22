from itertools import combinations, product
from sage.categories.sets_cat import Sets
from sage.combinat.permutation import Permutations
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE, richcmp


def int_to_az(i):
    r"""
    Convert a natural number to a word with letters a...z

    EXAMPLES::

        sage: import sys, pathlib
        sage: sys.path.append(str(pathlib.Path().absolute()))
        sage: from dim7.isom_utilities import int_to_az
        sage: int_to_az(0)
        'a'
        sage: int_to_az(5)
        'f'
        sage: int_to_az(25)
        'z'
        sage: int_to_az(26)
        'aa'
        sage: int_to_az(27)
        'ab'
        sage: int_to_az(51)
        'az'
        sage: int_to_az(52)
        'ba'

    Integers larger than
    """
    a = ord('a')
    n = ord('z') - ord('a') + 1
    s = ""
    while True:
        d = i % n
        s = chr(a + d) + s
        i -= d

        if i == 0:
            return s

        i = i // n - 1

def grading_label(gr):
    r"""
    Return the type for classification of gradings.

    INPUT:

    - ``gr`` -- a :class:`LieAlgebraGrading`

    The type is a string of the form ``k.n_1n_2...``, where k is the dimension
    of the grading group and n_i is the number of i-dimensional layers.

    EXAMPLES::

        sage: from lie_gradings.gradings.lie_algebra_grading import grading
        sage: from dim7.isom_utilities import grading_label
        sage: sc = {('X','Y'): {'Z': 1}, ('X','Z'): {'W': 1}}
        sage: L.<X,Y,Z,W> = LieAlgebra(QQ, sc)
        sage: layers = {(1,0): [X], (0,1): [Y], (1,1): [Z], (2,1): [W]}
        sage: gr1 = grading(L, layers)
        sage: grading_label(gr1)
        '2.4'
        sage: gr2 = grading(L, {1: [X,Y], 2: [Z], 3: [W]})
        sage: grading_label(gr2)
        '1.21'
        sage: gr3 = grading(L, {0: [X,Y,Z,W]}, magma=AdditiveAbelianGroup([]))
        sage: grading_label(gr3)
        '0.0001'
    """

    label = "%d." % len(gr.magma().gens())
    dims = [len(gr[a]) for a in gr]
    for k in range(1,max(dims)+1):
        label += str(dims.count(k))
    return label

def grading_label_alt(gr):
    r"""
    Return an alternate name for classification of gradings.

    INPUT:

    - ``gr`` -- a :class:`LieAlgebraGrading`

    The name is a string of the form ``k.abc...``, where k is the dimension
    of the grading group and a,b,c are the dimensions of the layers.

    EXAMPLES::

        sage: from lie_gradings.gradings.lie_algebra_grading import grading
        sage: from dim7.isom_utilities import grading_label
        sage: sc = {('X','Y'): {'Z': 1}, ('X','Z'): {'W': 1}}
        sage: L.<X,Y,Z,W> = LieAlgebra(QQ, sc)
        sage: layers = {(1,0): [X], (0,1): [Y], (1,1): [Z], (2,1): [W]}
        sage: gr1 = grading(L, layers)
        sage: grading_label_alt(gr1)
        '2.1111'
        sage: gr2 = grading(L, {1: [X,Y], 2: [Z], 3: [W]})
        sage: grading_label_alt(gr2)
        '1.112'
        sage: gr3 = grading(L, {0: [X,Y,Z,W]}, magma=AdditiveAbelianGroup([]))
        sage: grading_label_alt(gr3)
        '0.4'
    """

    label = "%d." % len(gr.magma().gens())
    dims = [str(len(gr[a])) for a in gr]
    label += "".join(sorted(dims))
    return label


def is_homomorphism(index_map):
    r"""
    Return whether an index map is a homomorphism where it is defined.

    EXAMPLES::

        sage: from dim7.isom_utilities import grading_label
        sage: is_homomorphism({0:1, 1:2})
        False
        sage: is_homomorphism({1:-1, 2:-2})
        True
        sage: is_homomorphism({1:0, 2:1})
        False
    """
    for a in index_map:
        for b in index_map:
            c = a + b
            if c in index_map:
                if index_map[c] != index_map[a] + index_map[b]:
                    return False
    return True


def index_map_iterator(gr1, gr2):
    r"""
    Return an iterator of all homomorphisms between weights of two gradings.

    INPUT:

    - ``gr1`` -- a :class:`LieAlgebraGrading`
    - ``gr2`` -- a :class:`LieAlgebraGrading`

    EXAMPLES::

        sage: from lie_gradings.gradings.lie_algebra_grading import grading
        sage: from dim7.isom_utilities import index_map_iterator
        sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z':1}})
        sage: gr = grading(L, {(1,0): [X], (0,1): [Y], (1,1):[Z]})
        sage: list(index_map_iterator(gr, gr))
        [{(0, 1): (0, 1), (1, 0): (1, 0), (1, 1): (1, 1)},
         {(0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (1, 1)}]
    """
    dims = {}
    for a in gr1:
        d = len(gr1[a])
        if d not in dims:
            dims[d] = [[], []]
        dims[d][0].append(a)
    for b in gr2:
        d = len(gr2[b])
        if d not in dims:
            raise ValueError("gradings do not have equal layer dimensions")
        dims[d][1].append(b)

    for d in dims:
        if len(dims[d][0]) != len(dims[d][1]):
            raise ValueError("gradings do not have equal layer dimensions")

    # iterate over all permutations of layers of equal dimensions
    perms = [Permutations(range(len(la))) for d, (la, lb) in dims.items()]
    for p in product(*perms):
        index_map = {}
        for perm, (da, db) in zip(p, dims.values()):
            for k, pk in enumerate(perm):
                index_map[da[k]] = db[pk]
        if is_homomorphism(index_map):
            yield index_map


class GradingIsomorphismClass(Parent):
    r"""
    Helper class to contain information about an isomorphism class of gradings.

    INPUT:

    - ``gr`` -- a :class:`LieAlgebraGrading`
    - ``compute_reduced`` -- (default:``False``) a boolean; if ``True`` the
      isomorphisms between gradings are computed and stored in reduced form

    Contains the following data:

    - a list of isomorphic gradings
    - a spanning tree of isomorphisms between the gradings in implicit form

    .. WARNING::

        The computations rely on the implicit isomorphism criterion: if the
        ideal of constraints for a linear map to be an isomorphism is a
        nontrivial ideal, then a solution is assumed to exist. This is in
        general true only over algebraically closed fields.

    EXAMPLES::

        sage: from lie_gradings.gradings.lie_algebra_grading import grading
        sage: from dim7.isom_utilities import GradingIsomorphismClass
        sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z':1}})
        sage: gr = grading(L, {(1,0): [X], (0,1): [Y], (1,1):[Z]})
        sage: grclass = GradingIsomorphismClass(gr)
        sage: TestSuite(grclass).run()
    """

    def __init__(self, gr, compute_reduced=False):
        self._gradings = [gr]
        self._isomorphisms = {}
        self._reduced = compute_reduced

        C = Sets()
        Parent.__init__(self, category=C)
        
    def __eq__(self, other):
        r"""
        Test equality of ``self`` and ``other``.
        
        EXAMPLES::
            
            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: from dim7.isom_utilities import GradingIsomorphismClass
            sage: L.<X,Y> = LieAlgebra(QQ, abelian=True)
            sage: gr = grading(L, {0: [X, Y]})
            sage: c1 = GradingIsomorphismClass(gr)
            sage: c2 = GradingIsomorphismClass(gr)
            sage: c1 == c2
            True
            sage: c1 == 5
            False
        """
        if isinstance(other, GradingIsomorphismClass):
            return self._gradings == other._gradings
        else:
            return super(GradingIsomorphismClass, self).__eq__(other)

    def _an_element_(self):
        return self.representative()

    def representative(self):
        r"""
        Return a representative grading of the isomorphism class.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: from dim7.isom_utilities import GradingIsomorphismClass
            sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z':1}})
            sage: gr = grading(L, {(1,0): [X], (0,1): [Y], (1,1):[Z]})
            sage: grclass = GradingIsomorphismClass(gr)
            sage: grclass.representative()
            Grading over Additive abelian group isomorphic to Z + Z of Lie
            algebra on 3 generators (X, Y, Z) over Rational Field with nonzero
            layers
              (1, 0) : (X,)
              (0, 1) : (Y,)
              (1, 1) : (Z,)
        """
        return self._gradings[0]

    def representatives(self):
        r"""
        Return the full list of known gradings of the isomorphism class.

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: from dim7.isom_utilities import GradingIsomorphismClass
            sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z':1}})
            sage: gr = grading(L, {(1,0): [X], (0,1): [Y], (1,1):[Z]})
            sage: grclass = GradingIsomorphismClass(gr)
            sage: grclass.representatives()
            [Grading over Additive abelian group isomorphic to Z + Z of Lie
            algebra on 3 generators (X, Y, Z) over Rational Field with nonzero
            layers
              (1, 0) : (X,)
              (0, 1) : (Y,)
              (1, 1) : (Z,)
            ]
        """
        return self._gradings

    def get_isomorphism(self, gr1, gr2):
        r"""
        Return a description of an isomorphism between two gradings in ``self``.

        INPUT:

        - ``gr1`` -- a :class:`LieAlgebraGrading` contained in the class
        - ``gr2`` -- a :class:`LieAlgebraGrading` contained in the class

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: from dim7.isom_utilities import GradingIsomorphismClass
            sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z':1}})
            sage: gr = grading(L, {(1,0): [X], (0,1): [Y], (1,1):[Z]})
            sage: grclass = GradingIsomorphismClass(gr)
            sage: gr2 = grading(L, {1: [X], 2: [Y], 3: [Z]})
            sage: gr2 in grclass
            True
            sage: d,I = grclass.get_isomorphism(gr, gr2)
            sage: for a,(b,A) in d.items(): print("%s -> %s: %s"%(a,b,A))
            (1, 0) -> 1: [a1_11]
            (0, 1) -> 2: [a2_11]
            (1, 1) -> 3: [a3_11]
            sage: for p in I.gens(): print(p)
            s_1*a1_11 - 1
            s_2*a2_11 - 1
            s_3*a3_11 - 1
            a3_11 - a1_11*a2_11
        """
        if gr1 not in self or gr2 not in self:
            raise ValueError("the gradings must be contained in the isomorphism class")

        i = self._gradings.index(gr1)
        j = self._gradings.index(gr2)
        if (i, j) in self._isomorphisms:
            return self._isomorphisms[(i, j)]

        if j < i:
            # swap order
            i, j = j, i
            gr1, gr2 = gr2, gr1

        # find an isomorphism path with an inefficient breadth-first algorithm
        # the keys of isomorphisms are pairs (a,b) with a<b
        def find_path(i, j):
            candidates = [[i]]
            while candidates:
                chain = candidates.pop()
                for (a, b) in self._isomorphisms:
                    if a == chain[-1]:
                        if b == j:
                            # path found
                            chain.append(b)
                            return chain
                        if j < b:
                            newchain = copy(chain)
                            newchain.append(b)
                            candidates.append(newchain)
                    if b == chain[-1]:
                        newchain = copy(chain)
                        newchain.append(a)
                        candidates.append(newchain)
            # no path exists
            return None

        # TODO: compose and invert isomorphisms of the path
        # to construct an isomorphism when one does not exist directly
        return NotImplemented("composition and inversion of isomorphisms not implemented")

    def __contains__(self, gr):
        r"""
        Test if a grading is contained in the isomorphism class.

        - ``gr`` -- a :class:`LieAlgebraGrading`

        EXAMPLES::

            sage: from lie_gradings.gradings.lie_algebra_grading import grading
            sage: from dim7.isom_utilities import GradingIsomorphismClass
            sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z':1}})
            sage: gr = grading(L, {(1,0): [X], (0,1): [Y], (1,1):[Z]})
            sage: grclass = GradingIsomorphismClass(gr)
            sage: len(grclass.representatives())
            1
            sage: gr2 = grading(L, {1: [X], 2: [Y], 3: [Z]})
            sage: gr2 in grclass
            True
            sage: len(grclass.representatives())
            2
            sage: gr3 = grading(L, {1: [X, Y], 2: [Z]})
            sage: gr3 in grclass
            False

        If the grading is contained, and is not already in the list of known
        representatives, then the grading is appended to the list::

            sage: L.<X,Y> = LieAlgebra(QQ, abelian=True)
            sage: gr = grading(L, {1: [X], 3: [Y]})
            sage: grclass = GradingIsomorphismClass(gr)
            sage: gr2 = grading(L, {3: [X], 5: [Y]})
            sage: gr2 in grclass.representatives()
            False
            sage: gr2 in grclass
            True
            sage: gr2 in grclass.representatives()
            True
        """
        if gr in self.representatives():
            return True

        rep = self.representative()
        try:
            for index_map in index_map_iterator(rep, gr):
                d, I = rep.isomorphism_equations(gr, index_map,
                                                 reduced=self._reduced)
                if 1 not in I:
                    # gradings are isomorphic
                    # append to representatives and store isomorphism
                    i = self._gradings.index(rep)
                    j = len(self._gradings)
                    self._gradings.append(gr)
                    # ensure _isomorphisms has keys (i,j) with i<j
                    self._isomorphisms[(i, j)] = (d, I)

                    return True
        except ValueError:
            # if the layer dimensions do not agree, a ValueError is raised
            pass

        return False
