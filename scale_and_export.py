import bpy
import os
import sys

# Handles cases where directories have spaces in them
directory = " ".join(sys.argv[sys.argv.index('--') + 1:])

# Finds the first valid FBX or OBJ file in the specified directory
model_file = None
for file in sorted(os.listdir(directory)):
    file_path = os.path.join(directory, file)
    if file.lower().endswith('.fbx'):
        model_file = file_path
        break
    elif file.lower().endswith('.obj'):
        # Make sure it's not the RCINFO file by checking the size
        if os.path.getsize(file_path) > 1024:  # Adjust size as necessary
            model_file = file_path
            break

if not model_file:
    print("No valid FBX or OBJ file found in the directory.")
    sys.exit()

# Clears existing objects
bpy.ops.wm.read_factory_settings(use_empty=True)

# Imports the model file
if model_file.lower().endswith('.fbx'):
    bpy.ops.import_scene.fbx(filepath=model_file)
elif model_file.lower().endswith('.obj'):
    # Import OBJ with Y forward and Z up axis
    bpy.ops.wm.obj_import(filepath=model_file, forward_axis='Y', up_axis='Z')

# selects the model and (optionally) scales it down
for obj in bpy.context.scene.objects:
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    # bpy.ops.transform.resize(value=(0.1, 0.1, 0.1))                               # scale down the model to 0.1 scale 
    # De-select the object afterward if needed
    # obj.select_set(False)

# Makes sure the correct context is set for exporting
bpy.context.view_layer.update()

# Exports to USDZ by naming the file with a .usdz extension, ensuring only selected objects are exported
usdz_file_path = model_file.rsplit('.', 1)[0] + ".usdz"
bpy.ops.wm.usd_export(filepath=usdz_file_path, selected_objects_only=True)

print(f"Exported to USDZ: {usdz_file_path}")
