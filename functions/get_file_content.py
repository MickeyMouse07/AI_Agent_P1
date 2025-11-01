import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    target = os.path.join(working_directory, file_path)

    try:
        if not os.path.abspath(target).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(os.path.abspath(target)):
            return f'Error: File not found or is not a regular file: "{file_path}"' 
        

        with open(os.path.abspath(target), "r", encoding="utf-8") as f:
            file_content_string = f.read(MAX_CHARS + 1)
            if len(file_content_string) > MAX_CHARS:
                file_content_string = file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return file_content_string
    
    except Exception as e:
        return f"Error: {e}"
    


        

        
    


    
        

    
        
    

    
        

        
            














