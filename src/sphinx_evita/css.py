from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sphinx.application import Sphinx

from . import __version__


def setup(app: Sphinx) -> dict[str, Any]:
    """
    - `evita_eu_funding_badge`: Add EU badge to the page footer. Supported values are
        `"funded"`, `"co-funded"`, `""` (default, empty string). Original files
        from sourced from
        [here](https://ec.europa.eu/regional_policy/information-sources/logo-download-center_en).
    """
    app.add_config_value(
        "evita_eu_funding_badge", default="", rebuild="html", types=str
    )

    app.add_css_file("furo_ext_lesson.css")

    app.connect("config-inited", add_evita_eu_funding_badge)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def add_evita_eu_funding_badge(app: Sphinx, config):
    match config.evita_eu_funding_badge:
        case "funded":
            app.add_css_file("EN_Funded.css")
        case "co-funded":
            app.add_css_file("EN_Co-funded.css")
        case _:
            pass
