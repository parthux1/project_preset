Getting started
===============

## Documentation

### generate docs
To generate the documentation compile source code docs using

```bash
doxygen
```

To generate the actual `html`-Documentation includeding your markdown files use

```{note} 
for the following step to work doxygen must be invocable on command line using `doxygen`
```

```bash
sphinx-build -b html -D breathe_projects.project=..\doxygen_out\xml .\docs\source\ ..\build
```

Documentation can now be opened via
```bash
.\docs\build\index.html
```

### append docs

#### Markdown

1. Add markdowns to `docs\source\markdown`
1. Append Section `Toctree` in `docs\source\index.rst`

#### bind/autogen Code Snippets

Code snippets can be included by `breathes` doxygenspecific commands [found here](https://breathe.readthedocs.io/en/latest/directives.html).

The following example documents all members of `ClassA` 
```
.. doxygenclass:: <class name>
    :members:
```

Other mentionable commands are `doxygenindex` for autogeneration of everything or specified file-groups, as well as `doxygenfile` and `doxygennamespace`. 

```{note}
argument `:allow-dot-graphs:` needs [graphviz](https://graphviz.org/download/) to be installed.
```

This syntax can be embedded in markdown like this:

`````markdown
```{eval-rst}
.. doxygenclass:: <class name>
    :members:
``` 
`````
More information on `mystparsers` directives can be found [here](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html).

## Additional information and sources

- [This Blog](https://devblogs.microsoft.com/cppblog/clear-functional-c-documentation-with-sphinx-breathe-doxygen-cmake/) describes the process of linking `doxygen` with `sphinx` using `breathe`

- Doxygens accepted doc-styles can be found [here](https://www.doxygen.nl/manual/docblocks.html)