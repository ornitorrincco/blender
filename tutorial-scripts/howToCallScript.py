import bpy

script = bpy.data.texts["script_name.py"]
exec(script.as_string())