#Generate a polygonal mesh with form of sin
import bpy
import numpy as np
from math import sin

m = bpy.data.meshes.new('sin')
n = 100
#add 100 vertices
m.vertices.add(n)
#add 99 edges for our vertices
m.edges.add(n - 1)
yVals = np.linspace(0, 10, 100)
for i,y in zip(range(n), yVals):
	m.vertices[i].co = (0, y, sin(y))
	
if i < n - 1:
	m.edges[i].vertices = (i, i + 1)
#create the object of the mesh
o = bpy.data.objects.new('sin', m)	
#add this object to the scene
bpy.context.scene.objects.link(o)
bpy.context.scene.objects.active = o
