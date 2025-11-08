import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        wd_abs = os.path.abspath(working_directory)
        target_abs = os.path.abspath(os.path.join(wd_abs, directory))

        if not target_abs.startswith(wd_abs + os.sep) and target_abs != wd_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_abs):
            return f'Error: "{directory}" is not a directory'

        entries = sorted(os.listdir(target_abs))
        lines = []
        for name in entries:
            full = os.path.join(target_abs, name)
            is_dir = os.path.isdir(full)
            size = os.path.getsize(full)
            lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
    
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

    



    

