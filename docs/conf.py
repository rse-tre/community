# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "RSE TRE"
copyright = "2022-2023, RSE TRE"
author = "RSE TRE"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_reredirects",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# https://pydata-sphinx-theme.readthedocs.io/en/stable/

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

html_logo = "_static/uktre-logo.svg"
html_favicon = "_static/uktre-logo.svg"

# Redirect index pages to new uktre site, RTD will handle all other redirects
# https://documatt.gitlab.io/sphinx-reredirects/usage.html
redirects = {"index": "https://uktre.readthedocs.io/en/latest/"}

html_baseurl = "https://uktre.readthedocs.io/en/latest/"
