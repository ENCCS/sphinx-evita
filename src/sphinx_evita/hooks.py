from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sphinx.application import Sphinx

HERE = Path(__file__).parent


def is_evita_project() -> bool:
    """Determine if the current project is an EVITA project.

    Checks multiple environment variables to detect if the documentation is being
    built in an EVITA-related repository or organization. Returns True if any of
    the following conditions are met, either

    - `EVITA`: Explicitly set to "true" or "1" to indicate an EVITA project,

    or the function checks if "evita" appears in any of the environment variables
    (case-insensitive):

    - `CI_PROJECT_NAME`: GitLab CI project name (falls back to `GITHUB_REPOSITORY`)
    - `CI_PROJECT_NAMESPACE`: GitLab CI project namespace (falls back to `GITHUB_REPOSITORY_OWNER`)
    - `CI_REPOSITORY_URL`: GitLab CI repository URL (falls back to `READTHEDOCS_GIT_CLONE_URL`)

    Returns
    -------
    bool
        True if the project is identified as an EVITA project, False otherwise.

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
    git_url = os.getenv("CI_REPOSITORY_URL", os.getenv("READTHEDOCS_GIT_CLONE_URL", ""))

    return (
        evita
        or repo.lower().startswith("evita")
        or owner.lower().startswith("evita")
        or "evita" in git_url.lower()
    )


def config_branding(app: Sphinx, config):
    """Hook to set the HTML favicon and sidebar image"""
    config.html_favicon = str((HERE / "img" / "evita-150x150.png").resolve())

    config.html_theme_options = getattr(config, "html_theme_options", {}) | {
        "light_logo": "evita-logo-light.png",
        "dark_logo": "evita-logo-dark.png",
        "announcement": """\
<aside style="overflow-wrap: break-word; white-space: wrap !important;">
<b>⚠️ Disclaimer: </b>
<span style="font-size: 0.9rem">
    This material should be regarded as a "living tool" open for
    improvement and its content may be subject to modifications without
    notice. It has not yet undergone formal review by the EuroHPC JU and is shared
    for informational purposes only.
</span>
</aside>
    """,
    }
    # NOTE: the above announcment will be only kept during review phase.

    config.copyright = (
        getattr(config, "copyright", "")
        + """\
    🇪🇺 Funded by the European Union. Views and opinions expressed
    are however those of the author(s) only and do not necessarily reflect those of
    the European Union or the granting authority (European High-Performance Computing Joint Undertaking: EuroHPC JU).
    Neither the European Union nor the granting authority can be held responsible for them.
"""
    )


def config_theme(app: Sphinx, config):
    config.html_theme = "furo"
