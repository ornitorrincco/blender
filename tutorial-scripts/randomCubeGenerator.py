import bpy
from random import randint

for i in range(50):
    bpy.ops.mesh.primitive_cube_add(
	location = [randint(-10,10) for axis in 'xyz'])