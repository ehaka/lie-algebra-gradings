# Outputs the 'data/isomorphism_classes' directory into a html hierarchy.
use_mathjax = False

import sys
import pathlib
path = pathlib.Path().absolute()
sys.path.append(str(path.parent))

import os
import os.path

html_pre = r"""<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<link rel="stylesheet" type="text/css" href="classification-style.css">
</head>
<body>
"""

html_post = r"""</body>
</html>
"""

mathjax = r"""<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [['\\(','\\)']]
    },
    asciimath2jax: {
        ignoreClass: ".*",
        processClass: "has_am"
    },
    jax: ["input/AsciiMath"],
    extensions: ["asciimath2jax.js"],
    TeX: {
        positionToHash: false,
        equationNumbers: { autoNumber: "none", useLabelIds: true, },
        TagSide: "right",
        TagIndent: ".8em",
    },
    // HTML-CSS output Jax to be dropped for MathJax 3.0
    "HTML-CSS": {
        scale: 88,
        mtextFontInherit: true,
    },
    CommonHTML: {
        scale: 88,
        mtextFontInherit: true,
    },
});
</script><script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS_CHTML-full"></script>
"""

mgrpath = path / 'data' / 'maximal_gradings'
datapath = path / 'data' / 'isomorphism_classes'
savepath = path / 'data' / 'html'

try:
    os.mkdir(savepath)
except FileExistsError:
    pass

from dim7.output_utilities import (brackets_to_align,
                                   brackets_to_table,
                                   label_to_filename,
                                   isom_class_to_html_tablerow)
from dim7.isom_utilities import grading_label
from lie_gradings.classification.lists import lie_algebra_isomorphism_classes
from lie_gradings.gradings.grading import stratification


def sortkey(fname):
    k, vec = fname.name.split(".")
    return -int(k), vec


def indent_details(htmlstr, indent="    "):
    r"""Return a new version of the html where every instance of <details>
    increases indentation level.
    """
    rows = htmlstr.split("\n")
    indentlevel = 0
    newrows = []
    for row in rows:
        if "</details" in row:
            indentlevel -= 1
        newrows.append(indent * indentlevel + row)
        if "<details" in row:
            indentlevel += 1
    return "\n".join(newrows)


def output_grading(label, grading):
    pass


def output_expandable(label, contents, classname, id=None):
    r"""
    Returns the html string for a single expandable block

    INPUT:

    - ``label`` -- the label to show initially
    - ``contents`` -- a list of html strings to include as children
    - ``classname`` -- a string to use as the class identifier
    - ``id`` -- a string to use for the id
    """
    if id is None:
        idstr = ""
    else:
        idstr = 'id="%s" ' % id
    template = '<details %sclass="%s">\n<summary>%s</summary>\n%s</details>\n'
    return template % (idstr, classname, label, "\n".join(contents))


def dim7_type(name):
    digits = [str(i) for i in range(10)]
    i = 0
    while i < len(name) and name[i] in digits:
        i += 1
    return name[:i]

def output_dim7(lie_algs, cs, contains_carnot, contains_positivisable, 
                contains_nonpositivisable):
    # output a container with the lie algebras
    if len(lie_algs) == 1:
        return lie_algs[0]
    
    extratags = []
    cs_class = "central-series"
    if contains_carnot:
        extratags.append("S")
        cs_class += " carnot"
    if contains_positivisable:
        cs_class += " positivisable"
    if contains_nonpositivisable:
        extratags.append("NP")
        cs_class += " non-positivisable"
    cs_label = cs
    if extratags:
        cs_label += "   ---   (%s)" % (", ".join(extratags)) # currently unused
    
    # suppress extra labels. comment the following line to re-enable
    cs_label = cs
    return output_expandable(cs_label, lie_algs, cs_class)

print("Writing html files for gradings.")
for d in range(2, 7 + 1):
    if use_mathjax:
        dimfilename = 'dimension_%d_with_mathjax.html' % d
    else:
        dimfilename = 'dimension_%d.html' % d
    savefile = savepath / dimfilename

    title = "Gradings in dimension %d" % d
    htmlstr = html_pre % title

    print("Dimension %d:" % d)
    sys.stdout.flush()

    if d == 7:
        cs = ""
        
    for L in lie_algebra_isomorphism_classes(QQbar, d):
        name = label_to_filename(L)
        L_datapath = datapath / name
        progfile = L_datapath / "INPROGRESS"

        if d == 7:
            nextcs = dim7_type(name)
            if nextcs != cs:
                if cs:
                    htmlstr += output_dim7(lie_algs, cs, contains_carnot, 
                                            contains_positivisable, 
                                            contains_nonpositivisable)
                # start a new container
                cs = nextcs
                contains_carnot = False
                contains_positivisable = False
                contains_nonpositivisable = False
                lie_algs = []
            

        if not os.path.isdir(L_datapath) or os.path.isfile(progfile):
            print("ERROR: No data for Lie algebra %s." % name)
            continue

        print("  %s:" % name)
        sys.stdout.flush()

        try:
            with open(mgrpath / ('%s.maxgrading' % name), 'rb') as f:
                mgr = loads(f.read())
        except IOError:
            print("ERROR: No maximal grading data for Lie algebra %s." % name)
            continue

        lie_classname = "lie-algebra"
        lie_label = name

        # compute the type label of the stratification (if one exists)
        try:
            st = stratification(L)
            strattype = grading_label(st)
            lie_classname += " carnot"
            lie_label += "   ---   (S)" # currently unused
            if d == 7:
                contains_carnot = True
        except ValueError:
            strattype = ""

            # not stratifiable, test if positive
            if mgr.has_positive_realization():
                lie_classname += " positivisable"
                if d == 7:
                    contains_positivisable = True
            else:
                lie_classname += " non-positivisable"
                lie_label += "   ---   (NP)" # currently unused
                if d == 7:
                    contains_nonpositivisable = True

        children = []

        # add a child displaying the brackets
        liefile = path / 'data' / 'torsion_free' / name / 'lie_algebra'
        with open(str(liefile), 'rb') as f:
            L_data = f.read()
        L_adapted = loads(L_data)
        if use_mathjax:
            bracketstr = brackets_to_align(L_adapted, amp="&amp;")
            if bracketstr:
                children.append("<p>\\(\n%s\n\\)</p>\n" % bracketstr)
        else:
            bracketstr = brackets_to_table(L_adapted)
            if bracketstr:
                children.append("%s\n" % bracketstr)

        # add a child for each grading spectrum type
        for subfolder in sorted(os.scandir(L_datapath), key=sortkey):
            if not subfolder.is_dir():
                continue

            print("    |%s" % subfolder.name)
            sys.stdout.flush()

            gt_classname = "grading-type"
            gt_label = subfolder.name
            gt_positivisable = False
            if gt_label == strattype:
                gt_classname += " carnot"
                gt_label += "   ---   (S)" # currently unused

            classfolder = L_datapath / subfolder
            isom_classes = {}
            for file in os.scandir(classfolder):
                fformat = ".isom_class"
                if file.name.endswith(fformat):
                    with open(str(classfolder / file), 'rb') as f:
                        data = f.read()
                    ic = loads(data)
                    label = file.name[:-len(fformat)]
                    isom_classes[label] = ic

            grading_table = '<table class="grading-list">\n'
            for label in sorted(isom_classes):
                ic = isom_classes[label]
                # check if positivisable
                if not gt_positivisable:
                    rep = ic.representative()
                    if rep.has_positive_realization():
                        gt_positivisable = True
                        gt_classname += " positivisable"
                grading_table += isom_class_to_html_tablerow(label, ic, use_mathjax)
                grading_table += "\n"
            grading_table += "</table>\n"

            # suppress extra labels. comment the following line to re-enable
            gt_label = subfolder.name
            if not gt_positivisable:
                gt_classname += " non-positivisable"
            gt_str = output_expandable(gt_label, [grading_table], gt_classname)
            children.append(gt_str)  # end spectrum type
            
        # suppress extra labels. comment the following line to re-enable
        lie_label = name
        liestr = output_expandable(lie_label, children, lie_classname, name)
        if d == 7:
            lie_algs.append(liestr)
        else:
            htmlstr += liestr
            
    if d==7:
        # output also the last central series grouping
        htmlstr += output_dim7(lie_algs, cs, contains_carnot, 
                                            contains_positivisable, 
                                            contains_nonpositivisable)

    if use_mathjax:
        htmlstr += mathjax

    htmlstr += html_post
    htmlstr = indent_details(htmlstr)

    with open(str(savefile), 'w') as f:
        f.write(htmlstr)

