# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "NDP(Non-Destructive Primitives)",
    "author" : "ChieVFX",
    "description" : "",
    "blender" : (2, 80, 0),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy

# from . utils.ui import extend_menus

from . src.test import OpHelloWorld
from . src.add_ui import SubmenuAdd
from . src.props_containers import PropertiesContainer, InitialPropertiesCacheContainer

from . src.update_op import OpUpdateGeometry

from . src.enums import prim_props, CustomProperty, PrimType

from . src.props_ui import PrimObjectPanel


classes = [
    OpUpdateGeometry,
    OpHelloWorld,
    PropertiesContainer,
    InitialPropertiesCacheContainer,
    PrimObjectPanel,

    SubmenuAdd,
]

from .src.utils_op import CLASSES as src_utils_op_CLASSES
classes.extend(src_utils_op_CLASSES)

from .src.add_op import CLASSES as src_op_add_CLASSES
classes.extend(src_op_add_CLASSES)

from .src.edit_op import CLASSES as src_op_edit_CLASSES
classes.extend(src_op_edit_CLASSES)

from .src.event_op import CLASSES as src_event_CLASSES
classes.extend(src_event_CLASSES)
from .src.event_op import register_events, unregister_events


def register():
    # global keymaps, icons

    from bpy.utils import register_class
    # # from utils.registration import register_icons, register_keymaps, get_tools, get_pie_menus
    for c in classes:
        register_class(c)

    bpy.types.Scene.ndp_cache_initial = bpy.props.PointerProperty(
        type = InitialPropertiesCacheContainer)
    # scene = bpy.context.scene
    # print("HEY!")
    # scene.ndp_cache_initial

    bpy.types.Mesh.ndp_props = bpy.props.PointerProperty(
        type = PropertiesContainer,
        name = "Non Destructive Prim Props")

    
    register_events()


def unregister():
    from bpy.utils import unregister_class
    # # from utils.registration import unregister_icons, unregister_keymaps
    # global keymaps, icons
    
    for c in classes:
        unregister_class(c)
    
    unregister_events()


separator = lambda menu, context: menu.layout.separator()

from .src.ui_utils import menu_menu, menu_operator

def extend_menus(is_registering):
    _extend_menu_add(is_registering)

def _extend_menu_add(is_registering):
    prepend = bpy.types.VIEW3D_MT_add.prepend
    append = bpy.types.VIEW3D_MT_add.append

    menu_menu(SubmenuAdd, prepend)

extend_menus(True)