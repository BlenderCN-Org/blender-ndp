import bpy
from . enums import PrimType, CustomProperty, prim_props

# def factoryPropertiesModel(obj):
#     prim_type = obj[prim_props][CustomProperty.prim_type.name]
#     return prim_type_to_init_mapping[prim_type]()

def _init_prim_types():
        enum_items = []
        for prim_type in PrimType:
            enum_items.append(
                (
                    prim_type.name.upper(),
                    prim_type.name,
                    "Non-destructive {}".format(prim_type.name),
                    prim_type.value
                ))
        return enum_items
prim_types = _init_prim_types()

def _init_size_policy(container, context):
    options = [('DEFAULT', "Default", "Default (blender) size behavior.", "", 0)]
    if container._is_radius_based():
        options.append(('AXIS_SCALE', "Per-Axis Size", "XYZ scale.", "", 1))
    if container._is_torus():
        options.append((
            'EXTERIOR_INTERIOR',
            "Exterior/Interior",
            "Use the exterior/interior radii for torus dimensions.",
            "",
            2))
    return options
    
def _set_dirty(self, context):
    self.is_dirty = True

class PropertiesContainer(bpy.types.PropertyGroup):
    #ndp marker:
    is_ndp : bpy.props.BoolProperty(default=False)
    #prim type:
    prim_type : bpy.props.EnumProperty(
        items = prim_types,
        name = "Type")
    #divisions are also used as segments and rings for sphere, vertices for circle, etc
    divisions_x : bpy.props.IntProperty(default=0, min=0, soft_max=100, update=_set_dirty)
    divisions_y : bpy.props.IntProperty(default=0, min=0, soft_max=100, update=_set_dirty)
    divisions_z : bpy.props.IntProperty(default=0, min=0, soft_max=100, update=_set_dirty)
    #axis_based_size
    size_x : bpy.props.FloatProperty(default=1, update=_set_dirty)
    size_y : bpy.props.FloatProperty(default=1, update=_set_dirty)
    size_z : bpy.props.FloatProperty(default=1, update=_set_dirty)
    #(radius), (cone's first radius), (torus's first param):
    radius_a : bpy.props.FloatProperty(default=1, update=_set_dirty)
    #(cone's second radius), (torus's second param):
    radius_b : bpy.props.FloatProperty(default=1, update=_set_dirty)
    #fill type for caps on circle, cylinder, cone
    fill_type : bpy.props.EnumProperty(
        items = [
            ('NGON', "Ngon", "Use ngon."),
            ('TRIANGLE_FAN', "Triangle Fan", "Use Triangle Fans"),
            ('NOTHING', "Nothing", "Don't fill at all."),
            ],
        name = "Caps Fill Type",
        update=_set_dirty)
    # # pivot(relative):
    # pivot_x : bpy.props.FloatProperty(default=.5, min=0, max=1)
    # pivot_y : bpy.props.FloatProperty(default=.5, min=0, max=1)
    # pivot_z : bpy.props.FloatProperty(default=.5, min=0, max=1)
    
    calculate_uvs : bpy.props.BoolProperty(
        name="Calculate UVs",
        default=True,
        update=_set_dirty)

    size_policy : bpy.props.EnumProperty(
        items = _init_size_policy,
        name = "Size Policy",
        update=_set_dirty)

    is_dirty = True
    
    def _is_radius_based(self):
        result = (self.prim_type == PrimType.Circle.name.upper())
        result |= (self.prim_type == PrimType.UvSphere.name.upper())
        result |= (self.prim_type == PrimType.IcoSphere.name.upper())
        result |= (self.prim_type == PrimType.Cylinder.name.upper())
        result |= (self.prim_type == PrimType.Cone.name.upper())
        # result |= (self.prim_type == PrimType.Torus.name.upper())
        return result

    def _is_torus(self):
        # result = (self.prim_type == PrimType.Torus.name.upper())
        # return result
        return False

#cache class for the scene, where the last used NDP initial values are cached
class InitialPropertiesCacheContainer(bpy.types.PropertyGroup):
    plane : bpy.props.PointerProperty(type = PropertiesContainer)
    box : bpy.props.PointerProperty(type = PropertiesContainer)
    circle : bpy.props.PointerProperty(type = PropertiesContainer)
    uvsphere : bpy.props.PointerProperty(type = PropertiesContainer)
    icosphere : bpy.props.PointerProperty(type = PropertiesContainer)
    cylinder : bpy.props.PointerProperty(type = PropertiesContainer)
    cone : bpy.props.PointerProperty(type = PropertiesContainer)

def get_properties_cache(context):
    scene = context.scene
    cache = scene.ndp_cache_initial
    try:
        if cache.plane.prim_type != 'PLANE':
            raise Exception("NDP cache was not found.")
        
        return cache
    except:
        print("Initializing NDP Cache...")
    
    for prim_type in PrimType:
        if (prim_type == PrimType.Unknown):
            continue
        setattr(getattr(cache, prim_type.name.lower()), "prim_type", prim_type.name.upper())
    
    setattr(cache.circle, "divisions_x", 32)
    
    setattr(cache.cylinder, "divisions_x", 32)
    
    setattr(cache.cone, "divisions_x", 32)

    return cache