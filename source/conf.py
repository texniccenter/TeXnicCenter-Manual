# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TeXnicCenter'
copyright = '%Y, The TeXnicCenter Team'
author = 'The TeXnicCenter Team'
version = '3.0'
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []


# -- Misc configuration ---------------------------------------------------
#~ Enables nitpicky mode if True. In nitpicky mode, Sphinx will warn about all references where the target cannot be found. This is recommended for new projects as it ensures that all references are to valid targets. You can activate this mode temporarily using the --nitpicky command-line option. See nitpick_ignore for a way to mark missing references as “known missing”.
nitpicky = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster' #proper responsive design (phones), default Sphinx theme
#~ html_theme = 'agogo' #used for Version 2.x, but not responsive
#~ html_theme = 'sphinx_rtd_theme' #requires 'pip install sphinx-rtd-theme', responsive, but some tables extend beyond the border
html_static_path = ['_static']

html_logo = 'images/TeXnicCenter.png'
html_favicon = 'images/TeXnicCenter.ico'
html_copy_source = False
html_show_sourcelink = False
html_show_sphinx = False


# -- Options for HTML Help output -------------------------------------------------
htmlhelp_basename = 'TeXnicCenter'

# -- Options for LaTeX output -------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble':  r'',
    'extrapackages':  r'\usepackage{microtype}',
    'babel' : r'\usepackage[english]{babel}',
    'fontpkg' : r'\usepackage{lmodern}',
    'fncychap' : '',
}


# -- Local Extensions  -------------------------------------------------
import sys

sys.path.append('.')

from sphinx import addnodes
from docutils.parsers import rst
from docutils.parsers.rst import roles
import docutils.nodes
from util import setup as util

def parse_placeholder(env, sig, signode):
    first = sig[0]
    arg = sig
  
    if first == '%' or first == '$':
        signode += docutils.nodes.generated(first, first)
        arg = sig[1:]

    signode += addnodes.desc_name(sig, arg)

    return sig

def parse_cmd(evn, sig, signode):
    first = sig[0]

    if first == '/':
        w = sig.split()

        option = w[0]
        name = option[1:]

        signode += addnodes.desc_name(option, option)

        for arg in w[1:]:
            arg = ' ' + arg
            signode += docutils.nodes.emphasis(arg, arg)

        sig = option
    else:
        signode += docutils.nodes.emphasis(sig, sig)

    return sig


def setup(app):
    app.add_crossref_type('tab', 'tab', ref_nodeclass = docutils.nodes.emphasis)
    app.add_crossref_type('dialog', 'dialog',  ref_nodeclass = docutils.nodes.emphasis)
    app.add_generic_role('button', docutils.nodes.emphasis)
    app.add_generic_role('control', docutils.nodes.emphasis)
    app.add_object_type('cmd', 'cmd', 'pair: %s; command-line argument', parse_cmd)
    app.add_object_type('placeholder', 'placeholder', 'pair: %s; placeholder', parse_placeholder)
    
    #~ Our own 'util' package contains defintions for key stroke, key presses, keyboard shortcuts
    #~ That util/setup.py cannot access our global variable latex_elements, so we return the preamble.
    ExtraTeX = util.setup(app)
    if ('preamble' in latex_elements):
        latex_elements['preamble'] += ExtraTeX
    else:
        latex_elements['preamble'] = ExtraTeX

