# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "RSE TRE"
copyright = "2022, RSE TRE"
author = "RSE TRE"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = ["linkify"]
myst_linkify_fuzzy_links = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# https://pydata-sphinx-theme.readthedocs.io/en/stable/

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

html_logo = "_static/banana-dance-dancing-banana.gif"
html_favicon = "_static/banana-dance-dancing-banana.gif"
