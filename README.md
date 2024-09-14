# Core Debug Tools for Blender

Features:

- Visualize depsgraph relations.
- Visualize lazy-function graphs for geometry nodes.

This extension bundles a viewer for dot graph files which is based on [d3-graphviz](https://github.com/magjac/d3-graphviz). The only dependency is a browser that supports WebAssembly.

## Build Instructions

The Python code does not require any build steps.

However, the extension also contains an HTML viewer which needs to be build in the `viewer` directory.

- `cd viewer`
- `npm install`
- `npm run build`
