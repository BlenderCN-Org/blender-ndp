import bpy

def draw_prop_row(data, layout:bpy.types.UILayout,
    label:str, prop_names:[], align=True):
    row = layout.row(align=align)
    row.label(text=label)
    for prop_name in prop_names:
        row.prop(data, prop_name, text="")