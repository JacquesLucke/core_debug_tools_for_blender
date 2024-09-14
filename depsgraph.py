import bpy
from . import dot_viewer


class ShowDepsgraphOperator(bpy.types.Operator):
    bl_idname = "debug.show_depsgraph"
    bl_label = "Show Depsgraph"

    def execute(self, context):
        deg = context.view_layer.depsgraph
        dot_viewer.show(deg.debug_relations_graphviz())
        return {"FINISHED"}


classes = (ShowDepsgraphOperator,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
