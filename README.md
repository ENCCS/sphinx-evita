# sphinx-evita
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

> [!NOTE]
> The official [EVITA template](https://github.com/ENCCS/evita-material-template/) is pre-configured to use this.