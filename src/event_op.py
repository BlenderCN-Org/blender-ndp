import bpy

def register_events():
    bpy.app.handlers.load_factory_startup_post.append(_load_handler)
    bpy.app.handlers.load_post.append(_load_handler)

    regEventsRegistered = 1
    if not bpy.app.timers.is_registered(_register_events):
        bpy.app.timers.register(_register_events, first_interval=.5)

def unregister_events():
    bpy.app.handlers.load_factory_startup_post.remove(_load_handler)
    bpy.app.handlers.load_post.remove(_load_handler)
    try:
        if bpy.app.timers.is_registered(_register_events):
            bpy.app.timers.unregister(_register_events)
    except BaseException as exception:
        print(str(exception))

def _register_events():
    if not EventContextReady.isRunning:
        while True:
            try:
                override = None
                window = bpy.context.window
                if window is None:
                    for w in bpy.context.window_manager.windows.values():
                        if w is not None:
                            window = w
                            
                    if window is None:
                        print("weird, but there is no window at all")
                        return 1

                    override = bpy.context.copy()
                    override['window'] = window
                    override['screen'] = window.screen

                if override:
                    bpy.ops.nondestructive_prims.raise_if_context_restricted(override)
                else:
                    bpy.ops.nondestructive_prims.raise_if_context_restricted('INVOKE_DEFAULT')
                break
            except BaseException as exception:
                exceptionMessage = str(exception)
                print("RESTRICTED!\n{}".format(exceptionMessage))
                return 1
        
        print("NDP EVENTS REGISTERED!")
        if override:
            bpy.ops.nondestructive_prims.event_editmode(override)
        else:
            bpy.ops.nondestructive_prims.event_editmode('INVOKE_DEFAULT')

from bpy.app.handlers import persistent
@persistent
def _load_handler(dummy):
    if not bpy.app.timers.is_registered(_register_events):
        bpy.app.timers.register(_register_events)


class EventContextReady(bpy.types.Operator):
    bl_idname = "nondestructive_prims.raise_if_context_restricted"
    bl_label = "Exception if Context Restricted"
    bl_description = "Raises exception if context is restricted"
    bl_options = {"INTERNAL"}

    @classmethod
    def poll(self, context):
        return True

    isRunning = False

    def __init__(self):
        EventContextReady.isRunning = True
        print("Start ContextReady")

    def __del__(self):
        EventContextReady.isRunning = False
        print("End ContextReady")

    def invoke(self, context, event):
        return self.execute(context)
        # return self.execute(context)

    def modal(self, context, event):
        return {'PASS_THROUGH'}

    def execute(self, context):
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


class EventEditMode(bpy.types.Operator):
    bl_idname="nondestructive_prims.event_editmode"
    bl_label="Event Edit Mode"
    bl_description="Sends out an event about entering edit mode"
    bl_options={"INTERNAL"}

    currentMode = ""

    @classmethod
    def poll(self, context):
        return True

    def __init__(self):
        print("Start EventEditMode")

    def __del__(self):
        print("End EventEditMode")

    def invoke(self, context, event):
        return self.execute(context)

    def modal(self, context, event):
        if EventEditMode.currentMode == context.mode:
            return {'PASS_THROUGH'}
        
        EventEditMode.currentMode = context.mode
        if not (EventEditMode.currentMode == 'EDIT_MESH'):
            return {'PASS_THROUGH'}
        activeObject = context.object
        if not activeObject:
            return {'PASS_THROUGH'}
        
        ndp_props = activeObject.non_destructive
        if not activeObject.non_destructive.is_ndp:
            #print("default prim")
            return {'PASS_THROUGH'}

        #print("EDITING NON-D PRIM!")
        op_edit = getattr(
            bpy.ops.nondestructive_prims,
            "edit_{}".format(ndp_props.prim_type.lower()))
        op_edit('INVOKE_AREA')
        context.scene.update()

        return {'RUNNING_MODAL'}

    def execute(self, context):
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

CLASSES = [
    EventContextReady,
    EventEditMode
]