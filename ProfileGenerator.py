import bpy
import bmesh
import random

def create_plane():
    bpy.ops.mesh.primitive_plane_add()
    bpy.ops.object.mode_set(mode = 'EDIT') # Ensure in edit mode for proceeding commands to work
    bpy.ops.mesh.subdivide(number_cuts=16)
    current_plane = bpy.context.active_object
    return current_plane

def create_bmesh_data(current_plane):
    bpy.ops.object.mode_set(mode = 'EDIT') # Ensure in edit mode for proceeding commands to work
    bmesh_data = bmesh.from_edit_mesh(current_plane.data)
    return bmesh_data

def create_colors(detail_level, bmesh_data, current_plane):
    for i in range(detail_level):
        """ Creating random colors within the green region of the rgb color wheel"""
        material = bpy.data.materials.new(f"Material#{i}")
        green = 1.0
        alpha = 1.0
        material.diffuse_color = (random.uniform(0.1, 0.5), green, random.uniform(0.1,0.5), alpha)
        current_plane.data.materials.append(material)

    for face in bmesh_data.faces:
        current_plane.active_material_index = random.randint(0,detail_level - 1)
        
        face.select = True # selecting the current face that we are iterating through 
        bpy.ops.object.material_slot_assign()
        face.select = False

current_plane = create_plane()
bmesh_data = create_bmesh_data(current_plane)
detail_level = 4
create_colors(detail_level, bmesh_data, current_plane)
bpy.ops.object.mode_set(mode = 'OBJECT')