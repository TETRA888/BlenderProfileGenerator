import bpy
import bmesh
import random

bpy.ops.mesh.primitive_plane_add()
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.subdivide(number_cuts=16)

current_plane = bpy.context.active_object

bmesh = bmesh.from_edit_mesh(current_plane.data)

detail_level = 4

for i in range(detail_level):
    """ Creating random colors within the green region of the rgb color wheel"""
    material = bpy.data.materials.new(f"Material#{i}")
    green = 1.0
    alpha = 1.0
    material.diffuse_color = (random.uniform(0.1, 0.5), green, random.uniform(0.1,0.5), alpha)
    current_plane.data.materials.append(material)

for face in bmesh.faces:
    current_plane.active_material_index = random.randint(0,detail_level - 1)
    
    face.select = True # selecting the current face that we are iterating through 
    bpy.ops.object.material_slot_assign()
    face.select = False
    
bpy.ops.object.editmode_toggle()