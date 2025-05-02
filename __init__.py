bl_info = {
    "name": "Armature Export to Unreal Engine",
    "description": "Exports armature objects to FBX files that can be used in Unreal Engine. Rigify armatures will be exported with a simplified bone structure",
    "author": "Samjooma",
    "version": (1, 0, 0),
    "blender": (4, 4, 1),
    "category": "Rigging"
}

import bpy
from . import export_to_ue_operator

def register():
    export_to_ue_operator.register()

def unregister():
    export_to_ue_operator.unregister()

if __name__ == "__main__":
    register()