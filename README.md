# sphinx-evita

[![PyPI](https://img.shields.io/pypi/v/sphinx-evita)](https://pypi.org/project/sphinx-evita/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/ENCCS/sphinx-evita/build.yaml?branch=main)](https://github.com/ENCCS/sphinx-evita/actions)
[![Documentation Status](https://readthedocs.org/projects/sphinx-evita/badge/?version=latest)](https://sphinx-evita.readthedocs.io/en/latest/?badge=latest)

> [!warning]
> Early access preview. See [disclaimer below](#disclaimer).

<!--begin-description-->
Sphinx plugins and theme customizations for the EVITA project.

## Purpose

This package includes customizations primarily meant for authoring modules in the [EVITA](https://www.evitahpc.eu) project.
The implementation is however general purpose and maybe reused for any project, which uses:

- [sphinx-lesson](https://coderefinery.github.io/sphinx-lesson) based markup for writing content, and
- [furo](https://pradyunsg.me/furo/) as the theme

## Installation

Install into your python environment with:

```console
pip install sphinx-evita
```

Then in the Sphinx conf.py file add:

```py
...
extensions = [
    # other extensions
    "sphinx_evita",
]
```

<!--end-description-->

> [!note]
> The official [EVITA module template](https://code.europa.eu/eurohpc-ju/evita/module-template/) is pre-configured to use this.

## Disclaimer

🇪🇺 Funded by the European Union. Views and opinions expressed
are however those of the author(s) only and do not necessarily reflect those of
the European Union or the granting authority (European High-Performance Computing Joint Undertaking: EuroHPC JU).
Neither the European Union nor the granting authority can be held responsible for them.

**Early access preview**: This material should be regarded as a "living tool" open for
improvement and its content may be subject to modifications without
notice. It has not yet undergone formal review by the EuroHPC JU and is shared
for informational purposes only.