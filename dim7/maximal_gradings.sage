# Computes a maximal grading for every Lie algebra
# whose data is not already found in the data subfolder.

import sys
import pathlib
path = pathlib.Path().absolute().parent
sys.path.append(str(path))

from lie_gradings.classification.lists import lie_algebra_isomorphism_classes
from lie_gradings.gradings.grading import maximal_grading
from dim7.output_utilities import label_to_filename
import os.path
from time import time

maxpath = "data/maximal_gradings"
try:
    os.mkdir(maxpath)
except FileExistsError:
    pass

# Compute for dimensions 2...7
print("Computing missing maximal gradings:")
totalstart = time()

for d in range(2, 7 + 1):
    print("Dimension %d:" % d)
    for L in lie_algebra_isomorphism_classes(QQbar, d):
        name = label_to_filename(L)
        fname = "%s.maxgrading" % name
        path = "%s/%s" % (maxpath, fname)

        if not os.path.isfile(path):
            # maximal grading not yet computed
            print("  %s..." % name, end="")
            sys.stdout.flush()
            stime = time()
            mgr = maximal_grading(L)
            data = dumps(mgr)
            with open(path, 'wb') as f:
                f.write(data)
            etime = time()
            print(" computed and saved in %.1f seconds" % (etime - stime))

totalend = time()
total = int(totalend - totalstart)
print("All missing Lie algebra maximal gradings computed in %d seconds" % total)
