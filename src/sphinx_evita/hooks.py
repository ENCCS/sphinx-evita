from __future__ import annotations
import os
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sphinx.application import Sphinx

HERE = Path(__file__).parent


def is_evita_project() -> bool:
    """Determine if the current project is an EVITA project.

    Only add the hook if we think we are being built in a EVITA repository / org

    See also
    --------
    - https://docs.gitlab.com/ci/variables/predefined_variables/
    - https://docs.github.com/en/actions/reference/workflows-and-actions/variables

    """
    evita = os.getenv("EVITA") in ("true", "1")
    repo: str = os.getenv("CI_PROJECT_NAME", os.getenv("GITHUB_REPOSITORY", ""))
    owner: str = os.getenv(
        "CI_PROJECT_NAMESPACE", os.getenv("GITHUB_REPOSITORY_OWNER", "")
    )
    git_url = os.getenv("READTHEDOCS_GIT_CLONE_URL", "")

    return (
        evita
        or repo.lower().startswith("evita")
        or owner.lower().startswith("evita")
        or git_url.lower().startswith("evita")
    )


def config_branding(app: Sphinx, config):
    """Hook to set the HTML favicon and sidebar image"""
    config.html_favicon = str((HERE / "img" / "evita-150x150.png").resolve())
    config.html_theme_options = {
        "light_logo": "evita-logo-light.png",
        "dark_logo": "evita-logo-dark.png",
    }


def config_theme(app: Sphinx, config):
    config.html_theme = "furo"
