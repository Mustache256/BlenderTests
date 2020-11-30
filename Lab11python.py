import bpy
import os
import sys

print("Hello World")
for env in os.environ:
    print(env)
for arg in sys.argv:
    print(arg)
    
print(sys.argv[4])

#Clean up initial scene
bpy.ops.object.select_all(action='DESELECT')

for obj in bpy.data.objects:
    if obj.type == 'MESH':
        obj.select_set(True)
        
bpy.ops.object.delete()

#Import Obj
path='curuthers/curuthers.obj'
bpy.ops.import_scene.obj(filepath=path)
obj = bpy.context.selected_objects[0]

#Join parts of the model
bpy.context.view_layer.objects.active = obj
obj.name = "Joined"
obj.data.name = "Joined"
bpy.ops.object.join()

#Export the model
bpy.ops.export_scene.obj(
    filepath=export/myfile.obj',
    use_selection=True,
    path_mode='COPY'
)