# Core Debug Tools for Blender

Features:

- Visualize depsgraph relations
  - `F3 > Show Depsgraph`
- Visualize lazy-function graphs for geometry nodes.
  - `F3 > Show Lazy-Function Graph` (in node editor)
  - `F3 > Show Zone Body Lazy-Function Graph` (in node editor with zone output node selected)

This extension bundles a viewer for dot graph files which is based on [d3-graphviz](https://github.com/magjac/d3-graphviz). The only dependency is a browser that supports WebAssembly.

## Build Instructions

The Python code does not require any build steps.

However, the extension also contains an HTML viewer which needs to be build in the `viewer` directory.

- `cd viewer`
- `npm install`
- `npm run build`
