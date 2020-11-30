import bpy
import os
import sys

for env in os.environ:
    print(env)
for arg in sys.argv:
    print(arg)
print("Hello World")

# POSX
#export MYVAR=Hello

#REM MS-DOS/Windows
#set MYVAR=Hello
x = 0
#for obj in bpy.data.objects:
    #print(obj.name + " " + obj.type)
    #obj.location = [x, 0, 0]
    #x = x + 5

def add_cube(position, rotation, scale):
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.context.selected_objects[0]
    cube.scale = scale
    cube.location = position
    return cube
    
pos = [0, 0, 0]

add_cube([5, 0, 0], [0, 45, 0], [10, 10, 0.1])
add_cube([10, 5, 0], [0, 45, 0], [2, 2, 2])
add_cube([10, 0, 5], [0, 45, 0], [2, 2, 2])
add_cube([10, 10, 0], [0, 45, 0], [2, 2, 2])

for x in range(10):
    pos[2] += 1
    pos[0] += 2
    add_cube(pos, [0, 45, 0], [1, 1, 0.5]) 