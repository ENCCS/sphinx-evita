"""Configuration for pytest

Note
----
Borrowed from the sphinx-design project

"""
from __future__ import annotations
from pathlib import Path
from typing import Any, Optional, TYPE_CHECKING

import pytest
from docutils import nodes
from sphinx import version_info
if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp

pytest_plugins = "sphinx.testing.fixtures"

if version_info[:2] >= (7, 2):
    # see https://github.com/sphinx-doc/sphinx/pull/11526
    from pathlib import Path as sphinx_path  # noqa: N813
else:
    from sphinx.testing.path import path as sphinx_path  # type: ignore[no-redef]


class SphinxBuilder:
    def __init__(self, app: SphinxTestApp, src_path: Path):
        self.app = app
        self._src_path = src_path

    @property
    def src_path(self) -> Path:
        return self._src_path

    @property
    def out_path(self) -> Path:
        return Path(self.app.outdir)

    def build(self, assert_pass=True):
        self.app.build()
        if assert_pass:
            assert self.warnings == "", self.status
        return self

    @property
    def status(self):
        return self.app._status.getvalue()

    @property
    def warnings(self):
        return self.app._warning.getvalue()

    def get_doctree(
        self, docname: str, post_transforms: bool = False
    ) -> nodes.document:
        doctree = self.app.env.get_doctree(docname)
        if post_transforms:
            self.app.env.apply_post_transforms(doctree, docname)
        # make source path consistent for test comparisons
        for node in doctree.findall(include_self=True):
            if not (hasattr(node, "get") and node.get("source")):
                continue
            node["source"] = Path(node["source"]).relative_to(self.src_path).as_posix()
            if node["source"].endswith(".rst"):
                node["source"] = node["source"][:-4]
            elif node["source"].endswith(".md"):
                node["source"] = node["source"][:-3]
        # remove mathjax classes added by myst parser
        if doctree.children and isinstance(doctree.children[0], nodes.section):
            doctree.children[0]["classes"] = []
        return doctree


@pytest.fixture()
def sphinx_builder(tmp_path: Path, make_app, monkeypatch):
    def _create_project(
        buildername: str = "html", conf_kwargs: Optional[dict[str, Any]] = None
    ) -> SphinxBuilder:
        src_path = tmp_path / "srcdir"
        src_path.mkdir()
        conf_kwargs = conf_kwargs or {
            "extensions": ["myst_parser", "sphinx_evita"],
            "myst_enable_extensions": ["colon_fence"],
        }
        content = "\n".join(
            [f"{key} = {value!r}" for key, value in conf_kwargs.items()]
        )
        src_path.joinpath("conf.py").write_text(content, encoding="utf8")
        app = make_app(
            srcdir=sphinx_path(str(src_path.resolve())),  # noqa: PTH100
            buildername=buildername,
        )
        return SphinxBuilder(app, src_path)

    yield _create_project
