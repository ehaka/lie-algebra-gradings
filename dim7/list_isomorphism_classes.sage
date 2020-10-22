# Explores the 'data/isomorphism_classes' directory and outputs a txt listing
# of all isomorphism classes of gradings of Lie algebras

import sys
import pathlib
path = pathlib.Path().absolute()
sys.path.append(str(path.parent))

from dim7.output_utilities import label_to_filename
import os
import os.path

datapath = path / 'data' / 'isomorphism_classes'
savefile = path / 'data' / 'isom_classes.txt'

from itertools import combinations
with open(str(savefile), 'w') as f:
    # clear the save file
    pass

from lie_gradings.classification.lists import lie_algebra_isomorphism_classes

print("Writing list of isomorphism classes to %s."%savefile)
sortkey = lambda f:f.name
for d in range(2, 7 + 1):
    w = 30
    dimlabel = "  DIMENSION %d  " % d
    a = (w - len(dimlabel)) // 2
    b = w - a - len(dimlabel)
    dimstr = "="*w + "\n" + "="*a + dimlabel + "="*b + "\n" + "="*w + "\n"
    with open(str(savefile), 'a') as f:
        f.write(dimstr)

    for L in lie_algebra_isomorphism_classes(QQbar, d):
        name = label_to_filename(L)
        L_datapath = datapath / name
        progfile = L_datapath / "INPROGRESS"

        if not os.path.isdir(L_datapath) or os.path.isfile(progfile):
            print("ERROR: No data for Lie algebra %s." % name)
            continue

        labelstr = "%s:\n" % name
        datastr = ""
        for subfolder in sorted(os.scandir(L_datapath), key=sortkey):
            labels = []
            if not subfolder.is_dir():
                continue
            for file in sorted(os.scandir(L_datapath / subfolder),
                               key=sortkey):
                fformat = ".isom_class"
                if file.name.endswith(fformat):
                    label = file.name[:-len(fformat)]
                    labels.append("%s%s" % (subfolder.name, label))
            datastr += "  %s\n" % (", ".join(labels))
        if datastr:
            datastr += "\n"

        with open(str(savefile), 'a') as f:
            f.write(labelstr)
            f.write(datastr)

