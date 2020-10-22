# Explores the 'data/isomorphism_classes' directory and condensed table
# with a row of data for each Lie algebra

import sys
import pathlib
path = pathlib.Path().absolute()
sys.path.append(str(path.parent))

from dim7.output_utilities import label_to_filename
import os
import os.path

maxpath = path / 'data' / 'maximal_gradings'
datapath = path / 'data' / 'isomorphism_classes'
savefile = path / 'data' / 'table.txt'

from itertools import combinations

from lie_gradings.classification.lists import lie_algebra_isomorphism_classes
from lie_gradings.gradings.grading import stratification


class DataContainer():

    def __init__(self, L):
        self.lie_algebra = L
        self.isom_classes = 0
        self.positivisable_classes = 0
        self.maxgrading_dimension = None
        self.stratifiable = None

print("Saving table of summary data to %s."%savefile)
sortkey = lambda f:f.name
table = []
for d in range(2, 7 + 1):
    print("Dimension %d:" % d)
    sys.stdout.flush()
    for L in lie_algebra_isomorphism_classes(QQbar, d):
        name = label_to_filename(L)
        L_datapath = datapath / name
        L_maxdatapath = maxpath / ("%s.maxgrading" % name)
        progfile = L_datapath / "INPROGRESS"

        if not os.path.isdir(L_datapath) or os.path.isfile(progfile):
            print("ERROR: No data for Lie algebra %s." % name)
            continue
        if not os.path.isfile(L_maxdatapath):
            print("ERROR: No maximal grading data for Lie algebra %s." % name)
            continue
        
        print("  %s:" % name)
        sys.stdout.flush()
        data = DataContainer(L)

        # count (positivisable) isomorphism classes of gradings
        for subfolder in sorted(os.scandir(L_datapath), key=sortkey):
            labels = []
            if not subfolder.is_dir():
                continue
            
            print("    |%s" % subfolder.name, end="")
            sys.stdout.flush()
            
            for file in sorted(os.scandir(L_datapath / subfolder),
                               key=sortkey):
                fformat = ".isom_class"
                
                if not file.name.endswith(fformat):
                    continue
                
                print("%s"%(file.name.split(".")[0]), end="")
                sys.stdout.flush()
                
                filepath = L_datapath / subfolder / file.name
                with open(str(filepath), 'rb') as f:
                    ic = loads(f.read())
                # test positivisability
                data.isom_classes += 1
                if ic.representative().has_positive_realization():
                    data.positivisable_classes += 1
                    print("(p)",end="")
                else:
                    print("(np)",end="")
                    pass
            print()

        # check dimension of maximal grading
        with open(str(L_maxdatapath), 'rb') as f:
            mgr = loads(f.read())
            data.maxgrading_dimension = len(mgr.magma().gens())

        # check if stratifiable
        try:
            strat = stratification(L)
            data.stratifiable = True
        except ValueError:
            data.stratifiable = False

        table.append(data)

textrow_elems = []
labels = ["Lie algebra", 
          "Dimension of maximal grading", 
          "Is stratifiable",
          "# isomorphism classes of gradings",
          "# isomorphism classes of positivisable gradings"]
maxwidths = [0, 0, 1, 0, 0]
for data in table:
    row = []

    # first column is the label
    name = str(label_to_filename(data.lie_algebra))
    row.append(name)
    maxwidths[0] = max(maxwidths[0], len(name))

    # second column is the dimension of the maximal grading
    dim = str(data.maxgrading_dimension)
    row.append(dim)
    maxwidths[1] = max(maxwidths[1], len(dim))

    # third column whether the Lie algebra is stratifiable
    strat = "y" if data.stratifiable else ""
    row.append(strat)

    # fourth column is number of isomorphism classes of gradings
    num = str(data.isom_classes)
    row.append(num)
    maxwidths[3] = max(maxwidths[3], len(num))

    # fifth column is number of isomorphism classes of positivisable gradings
    num = str(data.positivisable_classes)
    row.append(num)
    maxwidths[4] = max(maxwidths[4], len(num))

    textrow_elems.append(row)

formatstrs = ["{:>%d}" % w for w in maxwidths]
formatstr = "   ".join(formatstrs) + "\n"

# write all data to the savefile
with open(str(savefile), 'w') as f:
    f.write(formatstr.format(*labels))
    for row in textrow_elems:
        f.write(formatstr.format(*row))
