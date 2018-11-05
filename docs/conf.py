#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('../src/'))

import auxtest


# -- Project information -----------------------------------------------------
project = 'auxtest'
copyright = "2018, Arne Recknagel"
author = 'Arne Recknagel'
version = auxtest.__version__
release = auxtest.__version__


# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
]
templates_path = ['.templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['.static']
htmlhelp_basename = 'auxtestdoc'


# -- Options for LaTeX output ------------------------------------------------
latex_documents = [
    (master_doc,
     'auxtest.tex',
     'auxtest Documentation',
     'Arne Recknagel',
     'manual'),
]


# -- Options for manual page output ------------------------------------------
man_pages = [
    (master_doc,
     'auxtest',
     'auxtest Documentation',
     [author],
     1)
]


# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    (master_doc,
     '''auxtest''',
     '''auxtest Documentation''',
     author,
     '''auxtest''',
     '''Offer a REST-API to compare major city temperatures.''',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------
todo_include_todos = True
