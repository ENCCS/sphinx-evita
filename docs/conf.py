from sphinx.application import Sphinx
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "sphinx-evita"
copyright = "2026, EVITA project"
author = "EVITA project"
release = "0.1.0b0"

git_forge = "code.europa.eu"  # or "github.com"
git_user = "eurohpc-ju/evita"
git_repo_name = "sphinx-evita"  # auto-detected from dirname if blank
git_version = "main"
conf_py_path = "docs"
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_lesson", "sphinx_evita", "sphinx_design", "sphinxcontrib.bibtex"]

myst_enable_extensions = ["colon_fence", "attrs_inline"]
bibtex_bibfiles = ["references.bib"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
from pathlib import Path
from sphinx_evita import icons


# Auto-detect directory name. This can break, but useful as a default.
HERE = Path(__file__).parent
detected_repo_name = HERE.parent.name

git_repo_url = f"https://{git_forge}/{git_user}/{git_repo_name or detected_repo_name}"

html_theme = "alabaster"  # This should be overriden by sphinx_evita config-init hook
html_title = project
html_static_path = ["_static"]

html_css_files = ["overrides.css"]

# def setup(app):
#     from myst_parser._docs import MystExampleDirective
#     app.add_directive("myst-example", MystExampleDirective)


# Some theme options such as logo are defined by sphinx-evita extensions
html_theme_options = {
    # Gitlab
    "source_edit_link": f"{git_repo_url}/-/edit/{git_version}/{conf_py_path}/{{filename}}",
    "source_view_link": f"{git_repo_url}/-/blob/{git_version}/{conf_py_path}/{{filename}}?plain=1",
    # Github
    # "source_repository": git_repo_url,
    # "source_branch": git_version,
    # "source_directory": conf_py_path,
    "footer_icons": [
        {
            "name": git_forge,
            "url": git_repo_url,
            "html": icons.gitlab,
            "class": "",
        },
    ],
}


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
