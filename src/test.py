import bpy

class OpHelloWorld(bpy.types.Operator):
    bl_icon = 'PLUGIN'
    bl_idname="ndp.hello_world"
    bl_label="HELLO_WORLD"

    extend_menu = None

    def execute(self, context):
        # bpy.ops.wm.call_menu('VIEW3D_MT_object')
        bpy.ops.wm.call_menu(name="VIEW3D_MT_transform_object")
        # bpy.ops.wm.call_menu_pie(name="VIEW3D_PT_collections")
        print("HELLO WORLD")
        return {'FINISHED'}