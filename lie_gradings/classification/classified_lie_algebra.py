from sage.algebras.lie_algebras.nilpotent_lie_algebra import NilpotentLieAlgebra_dense
from sage.algebras.lie_algebras.structure_coefficients import LieAlgebraWithStructureCoefficients
from sage.categories.lie_algebras import LieAlgebras
from sage.structure.indexed_generators import standardize_names_index_set


class ClassifiedNilpotentLieAlgebra(NilpotentLieAlgebra_dense):
    r"""
    Base class for a Lie algebra with a specified label.

    EXAMPLES::

        sage: import sys, pathlib
        sage: sys.path.append(str(pathlib.Path().absolute()))
        sage: from lie_gradings.classification.dimension_6 import L6_16, L6_19
        sage: L = L6_16(QQ)
        sage: L
        Lie algebra L6_16 over Rational Field
        sage: L = L6_19(GF(3), 1)
        sage: L
        Lie algebra L6_19(1) over Finite Field of size 3
    """

    @staticmethod
    def __classcall_private__(cls, R, classification, s_coeff, names,
                              index_set=None, category=None, **kwds):
        r"""
        Normalize input to ensure a unique representation.
        """
        names, index_set = standardize_names_index_set(names, index_set)
        s_coeff = LieAlgebraWithStructureCoefficients._standardize_s_coeff(
            s_coeff, index_set)

        cat = LieAlgebras(R).FiniteDimensional().WithBasis().Nilpotent()
        category = cat.or_subcategory(category)

        return super(ClassifiedNilpotentLieAlgebra, cls).__classcall__(
            cls, R, classification, s_coeff, names,
            index_set, category=category, **kwds)

    def __init__(self, R, classification, s_coeff, names,
                 index_set, step=None, **kwds):
        self._classification = classification
        NilpotentLieAlgebra_dense.__init__(self, R, s_coeff,
                                           names, index_set, **kwds)

    def _repr_(self):
        r"""
        Return a string representation of ``self``.
        """
        return "Lie algebra %s over %s" % (self._classification,
                                           self.base_ring())
