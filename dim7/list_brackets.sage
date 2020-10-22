# Output a txt file with all Lie brackets for each presentation
# of a classified Lie algebra used to compute gradings.

import sys
import pathlib
path = pathlib.Path().absolute()
sys.path.append(str(path.parent))

from dim7.output_utilities import brackets_to_txt, label_to_filename

datapath = path / 'data' / 'torsion_free'
savepath = path / 'data' / 'brackets.txt'

from itertools import combinations
with open(str(savepath), 'w') as savefile:
    # clear the save file
    pass

from lie_gradings.classification.lists import lie_algebra_isomorphism_classes
    
print("Writing brackets to %s."%savefile)
for d in range(2, 7 + 1):
    w = 30
    dimlabel = "  DIMENSION %d  "%d
    a = (w - len(dimlabel)) // 2
    b = w - a - len(dimlabel)
    dimstr = "="*w + "\n" + "="*a + dimlabel + "="*b + "\n" + "="*w + "\n"
    with open(str(savepath), 'a') as savefile:
        savefile.write(dimstr)
    for L in lie_algebra_isomorphism_classes(QQbar, d):
        name = label_to_filename(L)
        try:
            with open(str(datapath / name / 'lie_algebra'), 'rb') as f:
                data = f.read()
            L = loads(data)

            labelstr = "%s:\n"%name
            bracketstr = brackets_to_txt(L)
            if bracketstr:
                bracketstr += "\n"

            with open(str(savepath), 'a') as savefile:
                savefile.write(labelstr)
                savefile.write(bracketstr)

        except IOError:
            print("ERROR: No 'lie_algebra' file found for %s." % name)

