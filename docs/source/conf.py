#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import datetime
import os
import sys

import mom6_tools

sys.path.insert(0, os.path.abspath('../..'))


# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'sphinx.ext.mathjax',  # for math equations
    'nbsphinx',
    'sphinx.ext.napoleon',
]

# Enable notebook execution
# https://nbsphinx.readthedocs.io/en/0.4.2/never-execute.html
nbsphinx_execute = 'auto'
# Allow errors in all notebooks by
nbsphinx_allow_errors = True

# Disable cell timeout
nbsphinx_timeout = -1

nbsphinx_kernel_name = 'python3'

extlinks = {
    'issue': ('https://github.com/NCAR/mom6-tools/issues/%s', 'GH#'),
    'pr': ('https://github.com/NCAR/mom6-tools/pull/%s', 'GH#'),
}

# Autosummary pages will be generated by sphinx-autogen instead of sphinx-build
autosummary_generate = []

# Otherwise, the Return parameter list looks different from the Parameters list
napoleon_use_rtype = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
html_static_path = ['../_build/html/_static']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
current_year = datetime.datetime.now().year
project = u'mom6-tools'
copyright = u'2018-{}, University Corporation for Atmospheric Research'.format(current_year)
author = u'mom6-tools developers'

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = mom6_tools.__version__.split('+')[0]
# The full version, including alpha/beta/rc tags.
release = mom6_tools.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '**.ipynb_checkpoints', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_logo = 'images/nsf.png'

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'mom6-tools-doc'


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [(master_doc, 'mom6-tools.tex', u'mom6-tools Documentation', author, 'manual')]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'mom6-tools', u'mom6-tools Documentation', [author], 1)]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        'mom6-tools',
        u'mom6-tools Documentation',
        author,
        'mom6-tools',
        'One line description of project.',
        'Miscellaneous',
    )
]


ipython_execlines = [
    'import numpy as np',
    'import pandas as pd',
    'import xarray as xr',
    'import mom6_tools',
]
