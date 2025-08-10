import os

def get_files_info(working_directory, directory="."):

    try:
        path = os.path.join(os.path.abspath(working_directory), directory)

        if os.path.commonpath([os.path.abspath(working_directory), os.path.abspath(path)]) != os.path.abspath(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(path):
            return f'Error: "{directory}" is not a directory'
        
        fileContent = sorted(os.listdir(path))
        result = []

        for i in fileContent:
            result.append(f"- {i}: file_size={os.path.getsize(os.path.join(path, i))} bytes, is_dir={os.path.isdir(os.path.join(path, i))}")
        end_result = "\n".join(result)
        return end_result

    except Exception as e:
        return f"Error: {e}"
    
        

    

    



    

