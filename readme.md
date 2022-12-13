# standard project template for my c++ projects
 Requirements:
 - doxygen
 - dot
 - gcc
 - python3

## doc
### markdown
.md-files in this folder will be included in the doxygen documentation.
If a title or Header of an included .md is mentioned in another file a reference will
be generated (may need further testing).

### diagrams
DOT-Engine files (.gv) in this dir will be rendered as pngs and can be included in .md -files by
including them as [filename].png

## res
external files which may be included in code.

## src
header and source files

## lib
3rd-party librarys.

## test
Test cases.
