from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sphinx.application import Sphinx

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

from . import __version__


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_node(
        pdfembed,
        html=(html_visit_pdfembed, None),
        latex=(latex_visit_pdfembed, None),
        # Optionally add for other builders
    )
    app.add_directive("pdfembed", PDFEmbedDirective)
    app.add_config_value("pdfembed_html_tag", "object", "html")

    return {"version": __version__, "parallel_read_safe": True, "parallel_write_safe": True}


logger = logging.getLogger(__name__)


class pdfembed(nodes.General, nodes.Element):
    pass


def align_spec(argument) -> str:
    # Allow left, center, right
    return directives.choice(argument, ("left", "center", "right"))


class PDFEmbedDirective(SphinxDirective):
    """
    Directive to embed a PDF via iframe.
    """

    has_content = False
    required_arguments = 1  # The PDF file path
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "height": directives.unchanged,
        "width": directives.unchanged,
        "align": align_spec,
        "id": directives.unchanged,
        "title": directives.unchanged,
        "frameborder": directives.unchanged,
        "scrolling": directives.unchanged,
        "style": directives.unchanged,
    }

    def run(self):
        node = pdfembed()

        # Set the node src to the path from the built HTML.
        # Note: assumes the PDF is copied to _static directory.
        node["src"] = self.arguments[0].strip()
        node["height"] = self.options.get("height", "550vh")
        node["width"] = self.options.get("width", "100%")
        node["align"] = self.options.get("align", "center")
        # node["id"] = self.options.get("id", f"pdf-{uuid.uuid4()}")
        node["title"] = self.options.get("title", "PDF")
        node["frameborder"] = self.options.get("frameborder", "1")
        node["scrolling"] = self.options.get("scrolling", "auto")
        node["style"] = self.options.get("style", "border:1px solid #666CCC")
        return [node]


def html_visit_pdfembed(self, node):
    """Embed in HTML using object or iframe."""
    match getattr(self.builder.config, "pdfembed_html_tag", "object").lower():
        case "iframe":
            # Compose the <iframe> tag
            tag = (
                f'<iframe class="pdfembed" '
                # f'id="{node["id"]}" '
                f'style="{node["style"]}" '
                f'title="{node["title"]}" '
                f'src="{node["src"]}" '
                f'frameborder="{node["frameborder"]}" '
                f'scrolling="{node["scrolling"]}" '
                f'height="{node["height"]}" '
                f'width="{node["width"]}" '
                f'align="{node["align"]}">'
                f"</iframe>"
            )
        case _:
            # Compose the <object> tag
            tag = (
                '<div class="pdfembed">'
                f"<object "
                # f'id="{node["id"]}" '
                f'style="{node["style"]}" '
                f'data="{node["src"]}" '
                f'type="application/pdf" '
                f'height="{node["height"]}" '
                f'width="{node["width"]}" '
                f'title="{node["title"]}" '
                f'align="{node["align"]}">'
                f'<p class="warning">Your browser does not support PDFs. '
                f'<a href="{node["src"]}">Download the PDF</a>.</p>'
                f"</object>"
                "</div>"
            )

    self.body.append(tag)
    raise nodes.SkipNode


def latex_visit_pdfembed(self, node):
    r"""Embed PDF using \includepdf. Assumes user loads pdfpages package in preamble."""
    width = node.get("width", r"0.9\linewidth")
    height = node.get("height", r"0.8\textheight")
    src = node["src"]
    embed = f"\\includepdf[pages=-,width={width},height={height}]{{{src}}}\n"
    self.body.append(embed)
    raise nodes.SkipNode
