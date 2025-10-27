from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sphinx.application import Sphinx

from sphinx_lesson.directives import _BaseCRDirective as Base
from . import __version__


class Recommendation(Base):
    extra_classes = ["seealso"]


def setup(app: Sphinx) -> dict[str, Any]:
    DIRECTIVES = [Recommendation]
    for obj in DIRECTIVES:
        app.add_directive(obj.get_cssname(), obj)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }