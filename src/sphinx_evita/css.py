from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sphinx.application import Sphinx

from . import __version__


def setup(app: Sphinx) -> dict[str, Any]:
    app.connect('builder-inited', init_static_path)
    app.add_css_file("furo_ext_lesson.css")
    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

def init_static_path(app):
    """Add our custom CSS to the headers."""
    static_path = Path(__file__).parent / '_static'
    app.config.html_static_path.append(str(static_path.resolve()))
