# SPDX-FileCopyrightText: See AUTHORS file
#
# SPDX-License-Identifier: GPL-2.0-or-later

import bpy


def show_dot_graph(dot_str):
    import webbrowser
    import urllib.parse

    dot_str_encoded = urllib.parse.quote(dot_str)
    url = f"https://dreampuf.github.io/GraphvizOnline/?presentation#{dot_str_encoded}"
    webbrowser.open(url)


class ShowLazyFunctionGraphOperator(bpy.types.Operator):
    bl_idname = "debug.show_lazy_function_graph"
    bl_label = "Show Lazy-Function Graph"

    @classmethod
    def poll(cls, context):
        if context.area.type != "NODE_EDITOR":
            return False
        if context.space_data.edit_tree is None:
            return False
        return True

    def execute(self, context):
        orig_tree = context.space_data.edit_tree
        deg = context.view_layer.depsgraph
        eval_tree = deg.id_eval_get(orig_tree)
        dot_str = eval_tree.debug_lazy_function_graph()

        if dot_str:
            show_dot_graph(dot_str)
        return {"FINISHED"}


class ShowZoneBodyLazyFunctionGraphOperator(bpy.types.Operator):
    bl_idname = "debug.show_zone_body_lazy_function_graph"
    bl_label = "Show Zone Body Lazy-Function Graph"

    @classmethod
    def poll(cls, context):
        if context.area.type != "NODE_EDITOR":
            return False
        if context.space_data.edit_tree is None:
            return False
        if context.active_node is None:
            return False
        return True

    def execute(self, context):
        orig_tree = context.space_data.edit_tree
        orig_node = context.active_node

        deg = context.view_layer.depsgraph

        eval_tree = deg.id_eval_get(orig_tree)
        eval_node = eval_tree.nodes[orig_node.name]

        dot_str = eval_node.debug_zone_body_lazy_function_graph()
        if dot_str:
            show_dot_graph(dot_str)
        return {"FINISHED"}


classes = (
    ShowLazyFunctionGraphOperator,
    ShowZoneBodyLazyFunctionGraphOperator,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
