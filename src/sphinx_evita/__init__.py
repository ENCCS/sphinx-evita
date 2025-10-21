from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sphinx.application import Sphinx

from importlib.metadata import version

__version__ = version("sphinx_evita")

def setup(app: Sphinx) -> dict[str, Any]:
    """Setup function for the sphinx-evita extension."""
    app.setup_extension(f"{__name__}.pdfembed")
    app.setup_extension(f"{__name__}.css")

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }