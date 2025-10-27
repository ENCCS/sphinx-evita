# Reference for module authors

(overview-of-directives)=
## Overview of directives

There are some directives defined in 
[MyST markdown](https://mystmd.org/guide/admonitions) and
[sphinx-lesson](https://coderefinery.github.io/sphinx-lesson/directives/)
to highlight blocks within the course materials. Some of these are:

- core admonitions: `note`, `hint`, `important`, `attention`, `caution`,`warning`, `danger`, ...
- sphinx-lesson admonitions: `discussion`, `demo`, `exercises`, `solution`, `homework`, `instructor-note`, `type-along` ...

The core admonition types are defined in Sphinx and MyST-Parser:

```{myst-admonitions} attention, caution, danger, error, hint, important, note, seealso, tip, warning
```

and these core admonitions take no argument and do not allow custom titles out of the box. More on the core MyST admonitions can be [read here](https://myst-parser.readthedocs.io/en/latest/syntax/admonitions.html#admonitions). 

These directives are extensions on top of the vanilla Markdown syntax. When a markdown cell in a Jupyter notebook contains the following markup for a `tip` admonition it renders into a rectangle with a green heading:

::::{myst-example}

:::{tip}
Let's give readers a helpful hint!
:::

::::

## Admonitions

All supported admonitions are showcased below. They are also classified into 5 groups.

### Internal

This is meant for the instructor and meant to be ignored by the learner.

:::{instructor-note}

This episode includes

- 20 min lecture
- 20 min exercises
:::

**NOTE**: The admonition above is named `instructor-note`.

### Information

These are passive directives from the perspective of the learner.

:::{prerequisites}
- Knowledge of X
- Course on Y
:::

:::{recommendation}

It is recommended to use the CUDA version > 10.0.

:::

:::{objectives}

- learning objective 1
- learning objective 2

:::

:::{questions}

- What does the tool X do?
- How can we use tool X in an HPC cluster?

:::

:::{discussion}

- How large is the data you are working with?
- Are you experiencing performance bottlenecks when you try to analyse it?

:::


:::{note}
Here we emphasize an important point from the section.
:::



:::{demo}

Code for demonstration
Due to the faster pace, we do not expect learners to type-along.

:::




:::{seealso}

- Blog by X
- Course on Y by Z

:::


:::{keypoints}

- summary 1
- summary 2

:::


### Success

These admonitions require active participation from the reader

:::{important}

You should follow the instructions step-by-step.

:::


:::{hint}

In this exercise, you can use A instead of B.

:::



:::{tip}

In this exercise, you can use A instead of B.

:::

:::{exercise}

Description of exercise
- Do this
- then do this
- finally observe what happens when you do this.

:::


:::{solution}

Here is the solution for the above exercise.

:::


:::{homework}

Here are the homework assignments for this episode.

:::


:::{type-along}

This is a type-along live-coding session.
We go at a slower pace to allow learners to follow along.

```python
import this
```

:::

**NOTE**: The admonition above is named `type-along`

### Warning

:::{warning}

Do not remove the following line.

:::


:::{caution}

Do not remove the following line.

:::


### Error

:::{error}

Here is an error!

:::

:::{attention}

Here is a crucial detail. Pay attention to this.

:::


:::{danger}

Here is a danger, a potential pitfall!

:::



## Extending admontions

### Custom titles

All sphinx-lesson admonitions support custom titles.

::::{myst-example}

:::{discussion} Discussion: Semantic versioning v/s calendar versioning

- Which versioning scheme do you prefer?
- What are the pros and cons of either schemes?
:::

::::

### Making a drop-down admonition

In this example, we show how an exercise admonition can be 
customized. This is done by adding a `:class: dropdown` *argument*
as shown below. This renders as a admonition with a
**Click to show** button.

::::{myst-example}

:::{exercise} Advanced exercise
:class: dropdown

If you have finished the previous exercise, try to do...

:::

::::

### Nested admonition

Nesting admonitions are supported in all directives. In fact, it is
recommended to nest the `solution` admonition within an `exercise`
admonition.

:::::{myst-example}

::::{exercise}

1. Task A
1. Task B

:::{solution}

1. This is how to do Task A ...
1. This is how to do Task B ...

:::
::::
:::::

## Cross-references and Bibliography

To include cross-references, markdown links are used. Refer to
[myst-parser documentation to learn how to acheive this](https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html).
Here is an example of a link to a section heading in this page:


:::{myst-example}

[Here](#overview-of-directives) are all directives that are currently
supported.

:::

For citing publications, webpages, books etc. as bibliography, the 
the `conf.py` file should include the extension [sphinxcontrib-bibtex](https://pypi.org/project/sphinxcontrib-bibtex/)
and the name of a BibTeX file,

```py
extensions = [
  # other extensions
  "sphinxcontrib.bibtex"
]
bibtex_bibfiles = ["references.bib"]
```

Then within the module articles be cited inline as follows:

:::{myst-example}

The learnings from the Software Carpentry project were crucial
in developing this style of teaching {cite}`wilson2016`.

:::

Finally the articles can be listed using the `bibliography` 
directive. Preferably this should be done at the bottom of the 
page.

::::{myst-example}

### References

:::{bibliography}
:::
::::

## Badges

Here is a badge of a module from Zenodo:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14844443.svg)](https://doi.org/10.5281/zenodo.14844443)

We can design other badges with different colors. See: <https://shields.io/badges>

## Presenting code

Sphinx and MyST-parser also adds a number of additional admonition types [for presenting code](https://myst-parser.readthedocs.io/en/latest/syntax/code_and_apis.html), such as `code-block` which can be useful.


::::{myst-example}
:::{code-block} python
:emphasize-lines: 3,5

def some_function():
   interesting = False
   print('This line is highlighted.')
   print('This one is not...')
   print('...but this one is.')
:::

::::

All Markdown syntax are also valid MyST markup. Therefore wrapping using three backticks to
syntax-highlight code can also work.

::::{myst-example}

```cpp
#include <iostream>

int main() {
  std::cout << "Hello world";
  return 0;
}
```

::::

For including code or code-snippets from other files,
[the `literalinclude` directive](https://myst-parser.readthedocs.io/en/latest/syntax/code_and_apis.html#including-code-from-files)
can also be adopted.


## Providing system or language-specific course instructions

Using `tabs` and `group-tab` directives we can allow the learner to focus on a single group of instructions.
Here is an example below[^coderef], starting with the syntax for 


::::::{myst-example}

### Testing frameworks

::::{tabs}
:::{group-tab} Python

The suggested solutions below use pytest.
:::

:::{group-tab} C++

The suggested solutions below use Catch2.
:::

:::{group-tab} R

The suggested solutions below use testthat.
:::

:::{group-tab} Julia

The suggested solutions below use Test.
:::

:::{group-tab} Fortran

The suggested solutions below use pFUnit.
:::
::::

:::::::

[^coderef]: Adapted from the [Coderefinery testing lesson](https://coderefinery.github.io/testing/), licensed CC-BY 4.0.

:::::::{admonition} Repeated use `tabs` and `group-tab` directives with the same key are synced
:class: important


::::::{exercise} Exercise: Design a test for a function that receives a number and returns a number
:::::{tabs}
::::{group-tab} Python

  :::{literalinclude} code/python/factorial.py
  :language: python
  :::

::::

::::{group-tab} C++

  :::{literalinclude} code/cpp/factorial.cpp
  :language: C++
  :::
  
::::

::::{group-tab} R

  :::{literalinclude} code/R/factorial.R
  :language: R
  :::
  
::::

::::{group-tab} Julia

  :::{literalinclude} code/julia/factorial.jl
  :language: julia
  :::

::::

::::{group-tab} Fortran

  :::{literalinclude} code/fortran/factorial.f90
  :language: fortran
  :::

::::
:::::
        
:::::{discussion}
The factorial grows very rapidly. What happens if you
pass a large number as argument to the function?
:::::



::::::{solution}

This is a **pure function** so is easy to test: inputs go to
outputs.  For example, start with the below, then think of some
what extreme cases/boundary cases there might be.  This example shows
all of the tests as one function, but you might want to make each test
function more fine-grained and test only one concept.

:::::{tabs}
::::{group-tab} Python

  :::{literalinclude} code/python/factorial_sol.py
  :language: python
  :::

::::

::::{group-tab} C++

  :::{literalinclude} code/cpp/factorial_sol.cpp
  :language: C++
  :::
  
::::

::::{group-tab} R

  :::{literalinclude} code/R/factorial_sol.R
  :language: R
  :::
  
::::

::::{group-tab} Julia

  :::{literalinclude} code/julia/factorial_sol.jl
  :language: julia
  :::

::::

::::{group-tab} Fortran

  :::{literalinclude} code/fortran/test_factorial.pf
  :::

::::
:::::
::::::
        
::::::

:::::::

## Embedding PDF slides

The `pdfembed` directive can be used to embed slides as follows:


::::{myst-example}

:::{pdfembed} ../../_static/slides/efficient-array-computing.pdf
:::

::::

**NOTE**: the slides need to be placed under the `content/_static` directory