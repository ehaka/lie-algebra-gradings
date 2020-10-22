# Computes isomorphism classes for gradings for every Lie algebra whose
# isomorphism class data is not already found in the data subfolder.

import sys
import pathlib
path = pathlib.Path().absolute()
sys.path.append(str(path.parent))

from lie_gradings.classification.lists import lie_algebra_isomorphism_classes
from dim7.isom_utilities import (grading_label, index_map_iterator, int_to_az,
                                 is_homomorphism, GradingIsomorphismClass)
from dim7.output_utilities import label_to_filename
import os
import os.path
from time import time

gradingspath = path / 'data' / 'torsion_free'
isompath = path / 'data' / 'isomorphism_classes'

try:
    os.mkdir(str(isompath))
except FileExistsError:
    pass

# Compute for dimensions 2...7
print("Computing missing isomorphism classes:")
totalstart = time()
for d in range(2, 7 + 1):
    print("Dimension %d:" % d)
    for L in lie_algebra_isomorphism_classes(QQbar, d):
        name = label_to_filename(L)
        savefolder = isompath / name
        progfile = savefolder / "INPROGRESS"

        if os.path.isdir(str(savefolder)):
            if not os.path.isfile(progfile):
                continue
        else:
            os.mkdir(savefolder)
            with open(progfile, 'w') as f:
                f.write("")

        # if any subfolders already exist, delete them
        for subfolder in os.scandir(str(savefolder)):
            if subfolder.is_dir():
                os.rmdir(str(savefolder / subfolder.name))

        print("  %s..." % name, end="")
        sys.stdout.flush()
        stime = time()

        # load all gradings to memory
        loadfolder = gradingspath / name
        if not os.path.isdir(str(savefolder)):
            print(" grading data missing!")
            continue

        gradings_bylabel = {}
        grading_count = 0
        for gfile in os.listdir(str(loadfolder)):
            if not gfile.endswith(".grading"):
                continue
            with open(str(loadfolder / gfile), 'rb') as f:
                data = f.read()
            gr = loads(data)
            grading_count += 1
            label = grading_label(gr)
            if label not in gradings_bylabel:
                gradings_bylabel[label] = []
            gradings_bylabel[label].append(gr)
        print(" loaded %d gradings..." % grading_count)

        for label in sorted(gradings_bylabel):
            # compute isomorphism classes
            gradings = gradings_bylabel[label]
            isom_classes = []
            for gr in gradings:
                if not any(gr in ic for ic in isom_classes):
                    # grading belongs to a new isomorphism class
                    ic = GradingIsomorphismClass(gr)
                    isom_classes.append(ic)

            # save isomorphism class to file
            classfolder = savefolder / label
            os.mkdir(classfolder)

            print("    |%s: %d gradings in %d isomorphism classes" % (label,
                                            len(gradings), len(isom_classes)))
            for k, ic in enumerate(isom_classes):
                savefile = classfolder / ("%s.isom_class" % int_to_az(k))
                with open(str(savefile), 'wb') as f:
                    f.write(dumps(ic))
        etime = time()
        os.remove(progfile)
        print("    |done in %.1f seconds" % (etime - stime))

totalend = time()
total = int(totalend - totalstart)
print("All missing Lie algebra grading isomorphism classes computed in %d seconds" % total)

