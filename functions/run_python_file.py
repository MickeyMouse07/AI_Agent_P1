import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    target = os.path.abspath(os.path.join(working_directory, file_path))
    wd = os.path.abspath(working_directory)

    if not target.startswith(wd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'   
    if not os.path.exists(target):
        return f'Error: File "{file_path}" not found.'
    if not target.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    command = ["python", target]

    if args:
        command.extend(args)

    try:
        result = subprocess.run(
            command,
            capture_output=True,   # Capture both stdout and stderr
            text=True,             # Decode output as text
            cwd=wd,                # Set working directory
            timeout=30             # Prevent infinite loops
            )
        
        output = ""
        if result.stdout:
            output += f"STDOUT:\n{result.stdout.strip()}\n"
        if result.stderr:
            output += f"STDERR:\n{result.stderr.strip()}\n"
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"
        if not result.stdout and not result.stderr:
            output = "No output produced."

        return output
    

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)

    
    
        
        
        
        
        
    
    
    
    
        
    
        
    
        
    
        

    






