from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

from sphinx.util import logging

if TYPE_CHECKING:
    from typing import Final
    from sphinx.application import Sphinx

from importlib.metadata import version

LOGGER: Final[logging.SphinxLoggerAdapter] = logging.getLogger(__name__)
__version__ = version("sphinx_evita")


def setup(app: Sphinx) -> dict[str, Any]:
    """Setup function for the sphinx-evita extension."""
    app.connect("builder-inited", init_static_path)

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

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def init_static_path(app):
    """Add sphinx_evita/_static to resolve css files, logo etc."""
    static_path = Path(__file__).parent / "_static"
    app.config.html_static_path.append(str(static_path.resolve()))
