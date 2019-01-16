import bpy
from .add_op import CLASSES

class SubmenuNonDestructive(bpy.types.Menu):
    bl_idname = "ADD_MT_non_destructive"
    bl_label = "Non-Destructive"
    bl_icon = 'OUTLINER_OB_MESH'

    def draw(self, context):
        layout = self.layout
        
        # menusString:str = 'add( angle_control( armature_add( armature_specials( assign_material( bone_options_disable( bone_options_enable( bone_options_toggle( brush( brush_paint_modes( camera_add( curve_add( edit_armature( edit_armature_delete( edit_armature_names( edit_armature_parent( edit_armature_roll( edit_curve( edit_curve_clean( edit_curve_ctrlpoints( edit_curve_delete( edit_curve_segments( edit_curve_showhide( edit_curve_specials( edit_font( edit_gpencil( edit_gpencil_delete( edit_gpencil_interpolate( edit_gpencil_transform( edit_lattice( edit_mesh( edit_mesh_clean( edit_mesh_delete( edit_mesh_edges( edit_mesh_edges_data( edit_mesh_extrude( edit_mesh_faces( edit_mesh_faces_data( edit_mesh_normals( edit_mesh_select_by_trait( edit_mesh_select_linked( edit_mesh_select_loops( edit_mesh_select_mode( edit_mesh_select_more_less( edit_mesh_select_similar( edit_mesh_shading( edit_mesh_showhide( edit_mesh_specials( edit_mesh_vertices( edit_mesh_weights( edit_meta( edit_meta_showhide( edit_proportional( edit_surface( edit_text_chars( editor_menus( gpencil_animation( gpencil_autoweights( gpencil_copy_layer( gpencil_edit_specials( gpencil_sculpt_specials( gpencil_simplify( hide_mask( hook( image_add( light_add( lightprobe_add( make_links( make_single_user( mesh_add( metaball_add( mirror( object( object_animation( object_apply( object_clear( object_collection( object_constraints( object_mode_pie( object_parent( object_quick_effects( object_relations( object_rigid_body( object_shading( object_showhide( object_specials( object_track( orientations_pie( paint_gpencil( paint_vertex( paint_weight( particle( particle_showhide( particle_specials( pivot_pie( pose( pose_apply( pose_constraints( pose_group( pose_ik( pose_library( pose_motion( pose_propagate( pose_showhide( pose_slide( pose_specials( pose_transform( proportional_editing_falloff_pie( sculpt( select_edit_armature( select_edit_curve( select_edit_lattice( select_edit_mesh( select_edit_metaball( select_edit_surface( select_edit_text( select_gpencil( select_object( select_object_more_less( select_paint_mask( select_paint_mask_vertex( select_particle( select_pose( select_pose_more_less( shading_ex_pie( shading_pie( snap( snap_pie( surface_add( tools_projectpaint_clone( tools_projectpaint_stencil( tools_projectpaint_uvlayer( transform( transform_armature( transform_base( uv_map( vertex_group( view( view_align( view_align_selected( view_borders( view_cameras( view_local( view_navigation( view_pie( view_viewpoint( weight_gpencil('
        # menus = menusString.split('(')
        # for menu in menus:
        #     m = "VIEW3D_MT_" + menu.replace(' ', '')
        #     layout.menu(m)
        # layout.menu('VIEW3D_PT_collections')

        for cls in CLASSES:
            layout.operator(cls.bl_idname, icon=cls.bl_icon)
