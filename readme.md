# project_template

A C++ project template. 

## Initial setup

- edit `CMakeLists.txt`: change <proj_name>
- edit `doc/DoxyFile`: Set `PROJECT_NAME`

## Documentation

to generate a documentation using files from `src/` and `doc/source/` run following code from the projects root dir:
```bash
doxygen doc/DoxyFile
```
Documentation will be written to `doc/out/`. Open it with `start doc/out/html/index.html` .
