# Computes all torsion free gradings for every Lie algebra
# whose data is not already found in the data subfolder.

# The computation is done starting from the presentation of the Lie algebra
# saved to the file 'data/torsion_free/<CLASSIFICATION>/lie_algebra'
# if the file exists.
# If the file does not exist, a Lie algebra in a basis adapted to the
# maximal grading is saved to the file.

import sys
import pathlib
path = pathlib.Path().absolute().parent
sys.path.append(str(path))

from lie_gradings.classification.lists import lie_algebra_isomorphism_classes
from lie_gradings.gradings.grading import maximal_grading, torsion_free_gradings
from dim7.output_utilities import label_to_filename
import os
import os.path
from time import time

torsionpath = "data/torsion_free"
try:
    os.mkdir(torsionpath)
except FileExistsError:
    pass

# Compute for dimensions 2...7
print("Computing missing gradings:")
totalstart = time()
for d in range(2, 7 + 1):
    print("Dimension %d:" % d)
    for L in lie_algebra_isomorphism_classes(QQbar, d):
        name = label_to_filename(L)
        path = "%s/%s" % (torsionpath, name)
        progfile = "%s/INPROGRESS" % path

        if os.path.isdir(path):
            if not os.path.isfile(progfile):
                continue
        else:
            os.mkdir(path)
            with open(progfile, 'w') as f:
                f.write("")

        print("  %s..." % name, end="")
        sys.stdout.flush()
        stime = time()

        # load a Lie algebra if one exists
        liefile = path + "/lie_algebra"
        try:
            with open(liefile, 'rb') as f:
                L = loads(f.read())
        except IOError:
            # load a pre-existing maximal grading if possible
            maxgrading_file = "data/maximal_gradings/%s.maxgrading" % name
            try:
                with open(maxgrading_file, 'rb') as f:
                    data = f.read()
                mgr = loads(data)
            except IOError:
                # no precomputed data, compute a maximal grading
                mgr = maximal_grading(L)
                data = dumps(mgr)
                with open(maxgrading_file, 'wb') as f:
                    f.write(data)
            varnames = ['Y_%d' % (k + 1) for k in range(L.dimension())]
            L = mgr.lie_algebra_in_adapted_basis(varnames)

            # save the computed Lie algebra to the file
            data = dumps(L)
            with open(liefile, 'wb') as f:
                f.write(data)

        # compute torsion free gradings
        grlist = torsion_free_gradings(L)
        print(" %d gradings..." % len(grlist), end="")
        sys.stdout.flush()

        digits = len(str(len(grlist)))
        fnamestr = "/{:0%dd}.grading" % (digits)
        for k, gr in enumerate(grlist):
            fname = path + fnamestr.format(k + 1)
            data = dumps(gr)
            with open(fname, 'wb') as f:
                f.write(data)
        etime = time()
        os.remove(progfile)
        print(" computed and saved in %.1f seconds" % (etime - stime))

totalend = time()
total = int(totalend - totalstart)
print("All missing Lie algebra gradings computed in %d seconds" % total)
