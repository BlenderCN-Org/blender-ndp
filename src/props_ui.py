import bpy
from . enums import CustomProperty, PrimType

#This panel shows up in object properties. Just in case.
class PrimObjectPanel(bpy.types.Panel):
    bl_label = "Non-Destructive Prim"
    bl_idname = "OBJECT_PT_tester"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'object'

    @classmethod
    def poll(cls, context):
        try:
            return context.object.data.ndp_props.is_ndp
        except:
            return False

    def draw(self, context):
        obj = context.object
        layout : bpy.types.UILayout = self.layout
        # if not obj:
        #     layout.label("SELECT OBJECT!")

        ndp_props = obj.data.ndp_props
        # is_ndp = getattr(ndp_props, CustomProperty.is_ndp.name)
        # if not is_ndp:
        #     layout.label(text="Not non-destructive prim!")
        #     return

        prim_type = getattr(ndp_props, CustomProperty.prim_type.name)
        if prim_type == PrimType.Plane.name.upper():
            self.draw_plane(context)
        if prim_type == PrimType.Box.name.upper():
            self.draw_box(context)
        if prim_type == PrimType.Circle.name.upper():
            self.draw_circle(context)
        if prim_type == PrimType.UvSphere.name.upper():
            self.draw_uvsphere(context)
        if prim_type == PrimType.IcoSphere.name.upper():
            self.draw_icosphere(context)
        if prim_type == PrimType.Cylinder.name.upper():
            self.draw_cylinder(context)
        if prim_type == PrimType.Cone.name.upper():
            self.draw_cone(context)
        # if prim_type == PrimType.Torus.name.upper():
        #     self.draw_torus(context)
    
    def draw_plane(self, context):
        props = context.object.data.ndp_props
        layout : bpy.types.UILayout = self.layout
    
    def draw_box(self, context):
        props = context.object.data.ndp_props
        layout : bpy.types.UILayout = self.layout
        row = layout.row()
        row.label(text="divisions")
        row.prop(props, CustomProperty.divisions_x.name, text="X")
        row.prop(props, CustomProperty.divisions_y.name, text="Y")
        row.prop(props, CustomProperty.divisions_z.name, text="Z")
        
        row = layout.row()
        row.label(text="size")
        row.prop(props, CustomProperty.size_x.name, text="X")
        row.prop(props, CustomProperty.size_y.name, text="Y")
        row.prop(props, CustomProperty.size_z.name, text="Z")
    
    def draw_circle(self, context):
        props = context.object.data.ndp_props
        layout : bpy.types.UILayout = self.layout
    
    def draw_uvsphere(self, context):
        props = context.object.data.ndp_props
        layout : bpy.types.UILayout = self.layout
    
    def draw_icosphere(self, context):
        props = context.object.data.ndp_props
        layout : bpy.types.UILayout = self.layout
    
    def draw_cylinder(self, context):
        props = context.object.data.ndp_props
        layout : bpy.types.UILayout = self.layout
    
    def draw_cone(self, context):
        props = context.object.data.ndp_props
        layout : bpy.types.UILayout = self.layout
    
    def draw_torus(self, context):
        props = context.object.data.ndp_props
        layout : bpy.types.UILayout = self.layout