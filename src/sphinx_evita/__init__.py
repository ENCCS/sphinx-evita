from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

from sphinx.util import logging

if TYPE_CHECKING:
    from typing import Final

    from sphinx.application import Sphinx

from importlib.metadata import version

__version__ = version("sphinx_evita")

LOGGER: Final[logging.SphinxLoggerAdapter] = logging.getLogger(__name__)
STATIC_PATH = Path(__file__).parent / "_static"


def setup(app: Sphinx) -> dict[str, Any]:
    """
    Implementation
    ==============
    The main powerhorse of this extension is {func}`sphinx_evita.setup`.
    It does the following:

    1. Connects the {func}`sphinx_evita.init_static_path` function to the `builder-inited` event.
       This ensures that static files (like CSS or JavaScript) are properly
       linked when the HTML page loads.

    2. Sets up three sub-extensions:
       - {mod}`sphinx_evita.pdfembed`: exposes the `pdfembed` directive.
       - {mod}`sphinx_evita.directives`: defines some more custom Sphinx directives for
       the extension.
       - {mod}`sphinx_evita.css`: links extra CSS stylesheets.

    3. Checks if the current project is an EVITA project using the
       {func}`sphinx_evita.hooks.is_evita_project` function.
       If it is, it configures branding and
       theme settings by connecting the {func}`sphinx_evita.hooks.config_branding` and
       {func}`sphinx_evita.hooks.config_theme` functions to the `config-inited` event.
       If not, it logs a warning. Which means that certain `conf.py` values gets
       overwritten.

    Finally it returns a dictionary with metadata about the extension, including its
    version and flags indicating that it is safe for parallel reading and
    writing.

    :::{seealso}
    <https://www.sphinx-doc.org/en/master/extdev/event_callbacks.html>
    :::

    Configuration
    -------------
    The *extension* also declares certain configuration values meant for
    Sphinx `conf.py`,

    ```{eval-rst}
    .. autodoc2-docstring:: sphinx_evita.pdfembed.setup
       :parser: myst
    ```
    ```{eval-rst}
    .. autodoc2-docstring:: sphinx_evita.css.setup
       :parser: myst
    ```

    """

    app.setup_extension(f"{__name__}.pdfembed")
    app.setup_extension(f"{__name__}.directives")
    app.setup_extension(f"{__name__}.css")

    from . import hooks

    if hooks.is_evita_project():
        LOGGER.info(
            "Detected the current repository as an EVITA project. "
            "Configuring branding and theme"
        )
        app.connect("config-inited", hooks.config_branding)
        app.connect("config-inited", hooks.config_theme)
    else:
        LOGGER.warning(
            "Extension enabled, but the current repostory was not detected"
            " as an EVITA project. Branding and theme will not be configured"
            " by sphinx_evita. See documentation for "
            " sphinx_evita.hooks.is_evita_project() for more details."
        )

    app.connect("builder-inited", init_static_path)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def init_static_path(app: Sphinx):
    """Add sphinx_evita/_static to resolve css files, logo etc."""
    app.config.html_static_path.append(str(STATIC_PATH.resolve()))
