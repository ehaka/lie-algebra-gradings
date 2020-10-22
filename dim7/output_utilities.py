from itertools import combinations
from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup
from sage.misc.latex import latex
from sage.rings.qqbar import QQbar
from lie_gradings.gradings.grading import maximal_grading, stratification


def label_to_filename(L):
    r"""
    Return a filename compatible label for the Lie algebra.

    INPUT:

    - ``L`` -- a :class:`ClassifiedNilpotentLieAlgebra`
    """
    fname = L._classification
    fname = fname.replace(" ", "")
    # check for special characters
    if "/" not in fname and "." not in fname:
        return fname

    # return a numerical approximation of the parameter instead
    base = fname.split("(")[0]
    approx = L._param.numerical_approx(digits=2)
    fname = "%s(%s)" % (base, approx)
    fname = fname.replace(" ", "")
    return fname


def grading_to_array(gr, amp="&amp;"):
    r"""
    Return a latex array describing the grading.

    INPUT:

    - ``gr`` -- a class:`LieAlgebraGrading`
    - ``amp`` -- a string to use as the ampersand symbol in the output
    """
    layers = [a for a in gr]
    layerstrs = [str(a) for a in gr]
    if len(gr.magma().gens()) == 1:
        layerstrs = [a.replace("(", "").replace(")", "") for a in layerstrs]
    elif len(gr.magma().gens()) == 0:
        layerstrs = [a.replace("()", "0") for a in layerstrs]
    latexstr = "\\begin{array}{%s}" % ("c"*(2 * len(layers) + 1))
    cstr = " %s \\oplus %s " % (amp, amp)
    layerlabels = ["V_{%s}" % a for a in layerstrs]
    latexstr += cstr.join(layerlabels)
    latexstr += "\\\\"
    layerformat = "\\langle %s \\rangle"
    layerstrings = [layerformat % (", ".join([str(X) for X in gr[a]]))
                    for a in layers]
    latexstr += cstr.join(layerstrings)

    latexstr += "\\end{array}"

    return latexstr


def grading_to_html_table(gr):
    r"""
    Return a html table describing the grading.

    INPUT:

    - ``gr`` -- a class:`LieAlgebraGrading`
    """

    layers = [a for a in gr]
    layerstrs = [str(a) for a in gr]
    if len(gr.magma().gens()) == 1:
        layerstrs = [a.replace("(", "").replace(")", "") for a in layerstrs]
    elif len(gr.magma().gens()) == 0:
        layerstrs = [a.replace("()", "0") for a in layerstrs]
    htmlstr = '<table class="gradingarray"><tr>'
    for a in layerstrs:
        htmlstr += '<td> %s </td>' % a
    htmlstr += '</tr><tr>'
    for a in layers:
        lstr = ", ".join([str(X) for X in gr[a]])
        htmlstr += '<td> &lt;%s&gt; </td>' % lstr
    htmlstr += '</tr></table>'

    return htmlstr


def brackets_to_align(L, amp="&amp;"):
    r"""
    Return a latex align* environment enumerating all Lie brackets.

    INPUT:

    - ``L`` -- a Lie algebra
    - ``amp`` -- a string to use as the ampersand symbol in the output
    """
    rows = []
    for X, Y in combinations(L.basis(), 2):
        Z = X.bracket(Y)
        if Z:
            row = "[%s, %s] %s = %s" % (latex(X), latex(Y), amp, latex(Z))
            rows.append(row)
    if not rows:
        return ""
    latexstr = "\\begin{align*}\n"
    latexstr += "\\\\\n".join(rows)
    latexstr += "\\end{align*}"
    QQbar.options(display_format=disp)
    return latexstr


def brackets_to_table(L):
    r"""
    Return a html table enumerating all Lie brackets.

    INPUT:

    - ``L`` -- a Lie algebra
    """
    # if the base ring is QQbar, display coefficients as radicals
    disp = QQbar.options('display_format')
    QQbar.options(display_format="radical")

    rows = []
    for X, Y in combinations(L.basis(), 2):
        Z = X.bracket(Y)
        if Z:
            rows.append((X, Y, Z))
    if not rows:
        return ""

    htmlstr = '<table class="brackets">\n'
    for (X, Y, Z) in rows:
        htmlstr += '<tr>'
        htmlstr += '<td class="brkt">[%s, %s]</td>' % (X, Y)
        htmlstr += '<td class="eq">=</td>'
        htmlstr += '<td class="res">%s</td>' % Z
        htmlstr += '</tr>\n'
    htmlstr += '</table>'
    return htmlstr


def brackets_to_txt(L):
    r"""
    Return a text string enumerating all Lie brackets.

    INPUT:

    - ``L`` -- a Lie algebra
    """
    # if the base ring is QQbar, display coefficients as radicals
    disp = QQbar.options('display_format')
    QQbar.options(display_format="radical")

    bracketstr = ""
    for X, Y in combinations(L.basis(), 2):
        Z = X.bracket(Y)
        if Z:
            bracketstr += "  [%s, %s] = %s\n" % (X, Y, Z)
    QQbar.options(display_format=disp)
    return bracketstr


def isom_class_to_html_tablerow(label, ic, mathjax):
    r"""
    Return a html table row describing a labelled isomorphism class of gradings.

    INPUT:

    - ``label`` -- a string identifier
    - ``ic`` -- a :class:`GradingIsomorphismClass`
    - ``mathjax`` -- a boolean; whether to output the table as mathjax or not
    """
    # if the base ring is QQbar, display coefficients as radicals
    disp = QQbar.options('display_format')
    QQbar.options(display_format="radical")

    indent = " "*4
    classname = "grading"
    # test if stratification or positivisable
    L = ic.representative().lie_algebra()
    try:
        st = stratification(L)
        strat = True
    except ValueError:
        strat = False
    if strat and st in ic:
        classname += " stratification positive"
    else:
        if ic.representative().has_positive_realization():
            classname += " positive"
        else:
            classname += " nonpositive"

    tablerow = '<tr class="%s">\n' % classname
    tablerow += indent + '<td class="label">%s</td>\n' % label
    if mathjax:
        icstr = "\\(%s\\)" % grading_to_array(ic.representative(), amp="&amp;")
    else:
        icstr = grading_to_html_table(ic.representative())
    tablerow += indent + '<td>%s</td>\n' % icstr
    tablerow += "</tr>"
    QQbar.options(display_format=disp)
    return tablerow
