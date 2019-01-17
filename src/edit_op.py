import bpy
from . props_containers import PropertiesContainer, get_properties_cache
from . enums import CustomProperty, PrimType
import time

def __setupProperly(cls):
    cls.bl_idname = "ndp.edit_{}".format(cls.prim_name).lower().replace(' ', '')
    cls.bl_label = "Edit {} (Non-Destructive)".format(cls.prim_name)
    cls.bl_description = "Edits a non-destructive {} primitive".format(cls.prim_name).lower()
    if not cls.bl_icon:
        cls.bl_icon = "MESH_{}".format(cls.prim_name.replace(' ', '').upper())

    return cls

def _set_values(props_from, props_to):
    for cp in CustomProperty:
        cp_name = cp.name
        if not hasattr(props_from, cp_name):
            continue
        if not hasattr(props_to, cp_name):
            continue
        val = getattr(props_from, cp_name)
        setattr(props_to, cp_name, val)

class _BaseOpEditPrim(bpy.types.Operator):
    bl_icon = ""
    prim_name = ""
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        if (context.area is not None) and (context.area.type != 'VIEW_3D'):
            return False
        try:
            ndp_props = context.object.data.ndp_props
            if not ndp_props[CustomProperty.is_ndp.name]:
                return False
            return ndp_props.prim_type == cls.prim_name.upper()
        except:
            return False

    def execute(self, context):
        self._on_executing(context)
        obj = context.object
        mesh = obj.data
        _set_values(self.props, mesh.ndp_props)
        prim_name = self.props.prim_type
        cache = getattr(get_properties_cache(context), prim_name.lower())
        _set_values(self.props, cache)

        bpy.ops.ndp.update_geometry()
        return {'FINISHED'}
    
    def _on_executing(self, context):
        pass

    def _on_invoke(self, context, event):
        pass

    def invoke(self, context, event):
        obj = context.object
        mesh = obj.data
        _set_values(mesh.ndp_props, self.props)

        obj.show_wire = True
        obj.show_all_edges = True

        wm = context.window_manager
        if event.type == 'ESC':
            return {'CANCELLED'}

        wm : bpy.types.WindowManager = context.window_manager

        self._on_invoke(context, event)

        bpy.ops.ndp.update_geometry()

        w = wm.invoke_props_popup(self, event)

        return w
        
@__setupProperly
class OpEditPlane(_BaseOpEditPrim):
    prim_name = PrimType.Plane.name

@__setupProperly
class OpEditBox(_BaseOpEditPrim):
    prim_name = PrimType.Box.name

    props : bpy.props.PointerProperty(type=PropertiesContainer)

    def _on_invoke(self, context, event):
        setattr(self, CustomProperty.size_x.name,
            getattr(context.object.data.ndp_props, CustomProperty.size_x.name))

    def draw(self, context):
        obj = context.object
        layout : bpy.types.UILayout = self.layout
        props = self.props
        row = layout.row()
        row.label(text="Size(XYZ)")
        row.prop(props, CustomProperty.size_x.name, text="")
        row.prop(props, CustomProperty.size_y.name, text="")
        row.prop(props, CustomProperty.size_z.name, text="")

        row = layout.row()
        row.label(text="Divisions")
        row.prop(props, CustomProperty.divisions_x.name, text="X")
        row.prop(props, CustomProperty.divisions_y.name, text="Y")
        row.prop(props, CustomProperty.divisions_z.name, text="Z")

        row = layout.row()
        row.prop(props, CustomProperty.calculate_uvs.name, text="Generate UVs")

        layout.prop(props, CustomProperty.size_x.name, text="X")
        
@__setupProperly
class OpEditCircle(_BaseOpEditPrim):
    prim_name = PrimType.Circle.name
        
@__setupProperly
class OpEditUvSphere(_BaseOpEditPrim):
    prim_name = PrimType.UvSphere.name
        
@__setupProperly
class OpEditIcoSphere(_BaseOpEditPrim):
    prim_name = PrimType.IcoSphere.name
        
@__setupProperly
class OpEditCylinder(_BaseOpEditPrim):
    prim_name = PrimType.Cylinder.name
        
@__setupProperly
class OpEditCone(_BaseOpEditPrim):
    prim_name = PrimType.Cone.name


CLASSES = [
    OpEditPlane,
    OpEditBox,
    OpEditCircle,
    OpEditUvSphere,
    OpEditIcoSphere,
    OpEditCylinder,
    OpEditCone
]