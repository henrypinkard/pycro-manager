# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# sys.path.insert(0, os.path.abspath('../../pycromanager/'))
sys.path.insert(0, os.path.abspath("../../"))
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "pycro-manager"
copyright = "2020, Henry Pinkard"
author = "Henry Pinkard"

# The full version, including alpha/beta/rc tags
# release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "nbsphinx", "sphinxcontrib.googleanalytics"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# this is needed for read the docs
master_doc = "index"

# dont look for errors in notebook cells
nbsphinx_allow_errors = True

# this is to make constructor docstrings show up
autoclass_content = "both"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'collapse_navigation': True,
    'navigation_depth': 10,
}

html_title = "Documentation"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# Prevent nbsphinx from executing the notebooks
nbsphinx_execute = 'never'



googleanalytics_id = 'G-8MC4VCD0JR'  # Replace with your actual GA4 measurement ID
googleanalytics_enabled = True
