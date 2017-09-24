#Generate a sin curve with cubes in a plane
import bpy
from math import sin
for i in range(50):
	x,y,z = 0,i,sin(i)
	bpy.ops.mesh.primitive_cube_add(
		location = [x,y,z])