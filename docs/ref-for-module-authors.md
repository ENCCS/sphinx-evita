# Reference for module authors



## Directives



There are some directives or admonitions defined in 
[MyST markdown](https://mystmd.org/guide/admonitions) and
[sphinx-lesson](https://coderefinery.github.io/sphinx-lesson/directives/)
to highlight blocks within the course materials. Some of these are:

- `discussion`, `demo`, `exercises`, `solution`, `homework`, ...
- `note`, `hint`, `important`, `attention`, `caution`,`warning`, `danger`, ...

These directives are extensions on top of the vanilla Markdown syntax.



For example, when a markdown cell in a Jupyter notebook contains the following markup:

::::::{instructor-note} MyST markdown syntax

```
:::{discussion}

- How large is the data you are working with?
- Are you experiencing performance bottlenecks when you try to analyse it?

:::
```

:::::::

renders into HTML while appears as below:



:::{discussion}

- How large is the data you are working with?
- Are you experiencing performance bottlenecks when you try to analyse it?

:::



## All other directives



:::{objectives}

- learning objective 1
- learning objective 2

:::



:::{questions}

- What does the tool X do?
- How can we use tool X in an HPC cluster?

:::



:::{attention}

Do not remove the following line.

:::



:::{caution}

Do not remove the following line.

:::



:::{warning}

Do not remove the following line.

:::



:::{danger}

Here is a danger!

:::



:::{error}

Here is an error!

:::



:::{hint}

In this exercise, you can use A instead of B.
:::



:::{tip}

In this exercise, you can use A instead of B.

:::



:::{important}

You should use the latest version of Python.
:::



:::{exercise}

Description of exercise
- Do this
- then do this
- finally observe what happens when you do this.

:::



:::{exercise} Exercise with a "Click to show" button
:class: dropdown

Description of exercise
- Do this
- then do this
- finally observe what happens when you do this…do this…

:::



:::{solution}

Here is the solution for above exercises.

:::



:::{homework}

Here are the homework assignments for this episode.

:::



:::{note}
Here we emphasize an important point from the section.
:::



:::{demo}

Code for demonstration

:::



:::{type-along}

Code for a type-along live-coding session

```python
import this
```

:::



:::{keypoints}

- summary 1
- summary 2

:::



## Define addition keywords

To do:

- references, ...
- suggestion, recommendation, ...

For now we reuse `admonition`.



:::{admonition} References
:class: note

publications and webpages for references

:::



:::{admonition} Recommendation
:class: hint

It is recommended to use the CUDA version > 10.0.

:::



## Badges



Here is one badge after we publish this module at Zenodo.



[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14844443.svg)](https://doi.org/10.5281/zenodo.14844443)



We can design other badges with different colors. See: <https://shields.io/badges>



## Providing system or language-specific course instructions

Using `tabs` and `group-tab` directives we can allow the learner to focus on a single group of instructions. Here is an example below[^coderef]


::::::{instructor-note} MyST markdown syntax
:class: dropdown

```
:::::{admonition} Testing frameworks
Language-specific instructions

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
:::::
```
:::::::

which renders as follows:

:::::{admonition} Testing frameworks
Language-specific instructions

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
:::::

[^coderef]: Adapted from the [Coderefinery testing lesson](https://coderefinery.github.io/testing/), licensed CC-BY 4.0.



Start by discussing how you would design tests for the
following five functions, and then try to write the tests.
Also discuss why some are easier to test than others.


::::::{exercise} Design-1: Design a test for a function that receives a number and returns a number
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
::::::




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
  :language: fortran
  :::

::::
:::::
        
::::::



## Embed PDF slides

The `pdfembed` directive can be used to embed slides as follows (NOTE: the slides need to be placed under the `content/_static` directory):

```markdown

:::{pdfembed} ../../_static/slides/efficient-array-computing.pdf
:::

```

which gives



:::{pdfembed} ../../_static/slides/efficient-array-computing.pdf
:::
