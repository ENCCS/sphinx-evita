from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable
    from .conftest import SphinxBuilder

content = """\

:::{pdfembed} ../../_static/slides/efficient-array-computing.pdf
:height: 530vh
:width: 100%
:::

"""

def test_build(
    sphinx_builder: Callable[..., SphinxBuilder], file_regression
):
    """Test that the pdfembed builds without warnings are used."""
    builder = sphinx_builder()
    builder.src_path.joinpath("index.md").write_text(content, encoding="utf8")
    builder.build()


def test_regression(
    sphinx_builder: Callable[..., SphinxBuilder], file_regression
):
    """Test that the defaults are used."""
    builder = sphinx_builder()
    builder.src_path.joinpath("index.md").write_text(content, encoding="utf8")
    builder.build(assert_pass=False)

    doctree = builder.get_doctree("index", post_transforms=False)
    file_regression.check(
        doctree.pformat(),
        basename="test_regression",
        extension=".xml",
        encoding="utf8",
    )
