from sphinx.application import Sphinx
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "sphinx-evita"
copyright = "2025, EVITA project"
author = "EVITA project"
release = "0.1.0b0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_lesson", "sphinx_evita", "sphinx_design", "sphinxcontrib.bibtex"]

myst_enable_extensions = ["colon_fence", "attrs_inline"]
bibtex_bibfiles = ["references.bib"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"  # This should be overriden by sphinx_evita config-init hook
html_title = project
html_static_path = ["_static"]

html_css_files = ["overrides.css"]

# def setup(app):
#     from myst_parser._docs import MystExampleDirective
#     app.add_directive("myst-example", MystExampleDirective)


def setup(app: Sphinx):
    """Add functions to the Sphinx setup."""
    from myst_parser._docs import (
        MystAdmonitionDirective,
        MystExampleDirective,
        MystLexer,
    )

    app.add_directive("myst-example", MystExampleDirective)
    app.add_directive("myst-admonitions", MystAdmonitionDirective)
    app.add_lexer("myst", MystLexer)
