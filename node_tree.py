import bpy


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
        import urllib.parse
        import webbrowser

        orig_tree = context.space_data.edit_tree
        deg = context.view_layer.depsgraph
        eval_tree = deg.id_eval_get(orig_tree)
        dot_str = eval_tree.debug_lazy_function_graph()

        dot_str_encoded = urllib.parse.quote(dot_str)
        url = (
            f"https://dreampuf.github.io/GraphvizOnline/?presentation#{dot_str_encoded}"
        )
        webbrowser.open(url)
        return {"FINISHED"}


classes = (ShowLazyFunctionGraphOperator,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
