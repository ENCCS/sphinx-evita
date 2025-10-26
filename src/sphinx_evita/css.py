from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sphinx.application import Sphinx

from . import __version__


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_css_file("furo_ext_lesson.css")
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }