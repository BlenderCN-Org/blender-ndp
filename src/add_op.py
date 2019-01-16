import bpy
import bmesh
import math
import mathutils
from enum import Enum

from . enums import PrimType, CustomProperty, prim_props

def __setupProperly(cls):
    cls.bl_idname = "nondestructive_prims.{}".format(cls.primName).lower().replace(' ', '')
    cls.bl_label = "Add {} (Non-Destructive)".format(cls.primName)
    cls.bl_description = "Creates a non-destructive {} primitive".format(cls.primName).lower()
    # cls.mesh_update_func = update_func[cls.primName.upper()]
    if not cls.bl_icon:
        cls.bl_icon = "MESH_{}".format(cls.primName.replace(' ', '').upper())

    print(cls.bl_idname)
    return cls

from . props_containers import get_properties_cache

class _BaseOpCreatePrim(bpy.types.Operator):
    bl_icon = ""
    primName = "UNKNOWN"
    bl_options = {'REGISTER', 'UNDO'}

    # mesh_update_func = lambda self, context, obj: print(
    #         "Class '{}' was not setup-ed properly!".format(str(type(self))))

    @classmethod
    def poll(cls, context):
        return (context.area is not None) and (context.area.type == 'VIEW_3D')

    def invoke(self, context, event):
        return self.execute(context)
    
    def execute(self, context):
        scene = context.scene
        cursor_rotation : mathutils.Quaternion = scene.cursor_rotation
        rotation = cursor_rotation.to_euler('XYZ')
        bpy.ops.object.add(
            radius=1.0,
            type='MESH',
            view_align=False,
            enter_editmode=False,
            location=scene.cursor_location,
            rotation=rotation)
        obj = context.active_object
        ndp_props = obj.non_destructive
        #Set Props:
        cache = getattr(get_properties_cache(context), self.primName.lower())
        for cp in CustomProperty:
            cp_name = cp.name
            setattr(ndp_props, cp_name, getattr(cache, cp_name))

        setattr(ndp_props, CustomProperty.is_ndp.name, True)
        setattr(ndp_props, CustomProperty.prim_type.name, getattr(cache, CustomProperty.prim_type.name))
        # obj.non_destructive[CustomProperty.divisions_x.name] = 1
        # obj.non_destructive[CustomProperty.divisions_y.name] = 1
        # obj.non_destructive[CustomProperty.divisions_z.name] = 1
        # obj.non_destructive[CustomProperty.size_x.name] = 1.0
        # obj.non_destructive[CustomProperty.size_y.name] = 1.0
        # obj.non_destructive[CustomProperty.size_z.name] = 1.0

        context.scene.update()

        # self.mesh_update_func(context, obj)
        bpy.ops.nondestructive_prims.update_geometry()

        getattr(bpy.ops.nondestructive_prims, "edit_{}".format(self.primName.lower()))('INVOKE_DEFAULT')

        print("CREATED {}".format(self.primName))
        return {'FINISHED'}

    def on_set_props(self, obj):
        pass

@__setupProperly
class OpCreatePlane(_BaseOpCreatePrim):
    primName = PrimType.Plane.name

@__setupProperly
class OpCreateBox(_BaseOpCreatePrim):
    primName = PrimType.Box.name
    bl_icon = 'MESH_CUBE'

@__setupProperly
class OpCreateCircle(_BaseOpCreatePrim):
    primName = PrimType.Circle.name

@__setupProperly
class OpCreateUvSphere(_BaseOpCreatePrim):
    primName = PrimType.UvSphere.name

@__setupProperly
class OpCreateIcoSphere(_BaseOpCreatePrim):
    primName = PrimType.IcoSphere.name

@__setupProperly
class OpCreateCylinder(_BaseOpCreatePrim):
    primName = PrimType.Cylinder.name

@__setupProperly
class OpCreateCone(_BaseOpCreatePrim):
    primName = PrimType.Cone.name

# @__nameProperly
# class OpCreateTorus(_BaseOpCreatePrim):
#     primName = PrimType.Torus.name

CLASSES = [
    OpCreatePlane,
    OpCreateBox,
    OpCreateCircle,
    OpCreateUvSphere,
    OpCreateIcoSphere,
    OpCreateCylinder,
    OpCreateCone,
    # OpCreateTorus
]