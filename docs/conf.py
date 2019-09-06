from auxtest import __version__


# -- Project information -----------------------------------------------------
project = "auxtest"
copyright = "2019, Arne"
author = "Arne Recknagel"
release = __version__


# -- General configuration ---------------------------------------------------
templates_path = ["_templates"]
extensions = [
    "pallets_sphinx_themes",
    "sphinx_click.ext",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
]


# -- Autodoc configuration ---------------------------------------------------
autodoc_member_order = "bysource"


# -- Options for HTML output -------------------------------------------------
html_theme = "flask"  # flask jinja werkzeug click
html_static_path = ["_static"]
html_logo = "_static/cabbage-96.png"
