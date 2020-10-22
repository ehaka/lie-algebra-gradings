# Apply some mostly automated (with some manual tweaks) simplifications to
# get nicer bases adapted to a maximal grading in dimensions 2...6.

import os
import sys
import pathlib
path = pathlib.Path().absolute().parent
sys.path.append(str(path))

from lie_gradings.classification.lists import lie_algebra_isomorphism_classes
from lie_gradings.gradings.grading import maximal_grading
from lie_gradings.gradings.utilities import in_new_basis
from dim7.output_utilities import label_to_filename, brackets_to_txt
from itertools import combinations

maxpath = path / 'dim7' / 'data' / 'maximal_gradings'
gradingspath = path / 'dim7' / 'data' / 'torsion_free'

try:
    os.mkdir(gradingspath)
except FileExistsError:
    pass


def write_to_file(L, L_newbasis):
    l_path = gradingspath / label_to_filename(L)
    progfile = l_path / "INPROGRESS"
    try:
        os.mkdir(l_path)
    except FileExistsError:
        pass
    with open(l_path / 'lie_algebra', 'wb') as f:
        f.write(dumps(L_newbasis))
    with open(progfile, 'w') as f:
        f.write("")


def sc_dict_textform(L):
    sc = dict(L.structure_coefficients())
    return {p:Z.monomial_coefficients() for p, Z in sc.items()}


print("Cleaning brackets:")
C = LieAlgebras(QQbar).FiniteDimensional().WithBasis().Nilpotent()
prev_lie_algs = []
for d in range(2, 7):
    names = ['Y_%d' % (k + 1) for k in range(d)]

    # the first Lie algebras are products with R
    dlist = lie_algebra_isomorphism_classes(QQbar, d)
    next_lie = []
    for L, (prevname, L_prev) in zip(dlist, prev_lie_algs):
        # copy structure coefficients from previous
        L_name = label_to_filename(L)
        print("  %s as a product %s x R" % (L_name, prevname))
        sc = sc_dict_textform(L_prev)
        L_new = LieAlgebra(QQbar, sc, names=names, category=L.category())
        next_lie.append((L_name, L_new))

        print(brackets_to_txt(L_new))
        write_to_file(L, L_new)

    for L in dlist[len(prev_lie_algs):]:
        # compute a cleaner basis
        L_name = label_to_filename(L)
        print("  %s" % L_name)
        with open(maxpath / ("%s.maxgrading" % L_name), 'rb') as f:
            mgr = loads(f.read())

        # start with a basis adapted to the maximal grading
        # include hash in varname to avoid problems with caching
        id = abs(hash(L))
        tempnames = ['tv%d%d' % (id, k) for k in range(d)]
        templie = mgr.lie_algebra_in_adapted_basis(tempnames, category=C)

        # special handling for L6_24(1): add a manual tilting of the 2d layer
        if L_name == 'L6_24(1)':
            k = 0
            for a in mgr:
                dim = len(mgr[a])
                if dim > 1:
                    break
                k += dim
            newbasis = list(templie.basis())
            newbasis[k+1] = newbasis[k] + newbasis[k + 1]
            templie = in_new_basis(templie, newbasis, tempnames)

        # attempt to order basis so that [X,Y]=Z+W implies X<Y and X,Y<Z,W
        order_prefs = []
        B = templie.basis()
        abelian_factors = set(B)
        nonabelian = set([])
        for X, Y in combinations(B, 2):
            Z = X.bracket(Y)
            if Z:
                abelian_factors.discard(X)
                abelian_factors.discard(Y)
                num_pos = 0
                num_neg = 0
                for zk in Z.to_vector():
                    if zk > 0:
                        num_pos += 1
                    elif zk < 0:
                        num_neg += 1
                if num_neg == 0 and num_pos > 0:
                    # prefer X<Y over Y<X
                    order_prefs.append((X, Y))
                elif num_pos == 0 and num_neg > 0:
                    # prefer Y<X over X<Y
                    order_prefs.append((Y, X))

                # prefer X<Zk and Y<Zk for each component Zk of Z
                for Zk in Z.monomials():
                    abelian_factors.discard(Zk)
                    order_prefs.append((X, Zk))
                    order_prefs.append((Y, Zk))

        # put abelian factors at the end
        nonabelian = [X for X in B if X not in abelian_factors]
        abelian_order = [(X, Y) for X in nonabelian for Y in abelian_factors]

        order_prefs = list(set(order_prefs))

        # find largest compatible subset of preferences
        n = len(order_prefs)

        for k in range(n):
            for pref_subset in combinations(order_prefs, n - k):
                try:
                    p = Poset((B, abelian_order + list(pref_subset)))
                    # preferences are compatible, reorder the basis
                    templie = in_new_basis(templie, p.list(), tempnames)
                    break
                except ValueError:
                    # preferences are imcompatible, try a different subset
                    continue
            else:
                # no set of n-k preferences is compatible, try with smaller set
                continue
            break
        
        # reorder the basis with a maximal grading
        new_mgr = maximal_grading(templie)
        templie = new_mgr.lie_algebra_in_adapted_basis(tempnames)

        # attempt to rescale basis elements to avoid unnecessary scalars
        m = VectorSpace(QQ, d)
        for k in range(d):
            newbasis = []
            B = templie.basis()
            for X, Y in combinations(B, 2):
                Z = X.bracket(Y)
                if Z:
                    zvec = m(Z.to_vector())
                    g = gcd(zvec)
                    if g > 1:
                        # rescale by g
                        newbasis = list(B)
                        for k, Zk in enumerate(B):
                            if Zk in Z.monomials():
                                newbasis[k] = Zk * g
                        templie = in_new_basis(templie, newbasis, tempnames)
                        break
            else:
                # no changes to the lie algebra
                break

        # consider also rescaling Y in [X,Y]=Z
        for k in range(d):
            newbasis = []
            B = list(templie.basis())
            for X, Y in combinations(B, 2):
                Z = X.bracket(Y)
                if Z:
                    zvec = m(Z.to_vector())
                    g = gcd(zvec)
                    if 0 < g and g < 1:
                        # rescale Y by 1/g
                        newbasis = list(B)
                        newbasis[B.index(Y)] = Y / g
                        templie = in_new_basis(templie, newbasis, tempnames)
                        break
            else:
                # no changes to the lie algebra
                break

        L_new = in_new_basis(templie, templie.basis(), names)
        L_new._test_jacobi_identity()
        next_lie.append((L_name, L_new))
        print(brackets_to_txt(L_new))
        write_to_file(L, L_new)

    prev_lie_algs = next_lie
