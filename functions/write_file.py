import os

def write_file(working_directory, file_path, content):
     target = os.path.abspath(os.path.join(working_directory, file_path))
     wd = os.path.abspath(working_directory)

     if not target.startswith(wd):
          return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'    
     if not os.path.exists(target):
          try:
                os.makedirs(os.path.dirname(target), exist_ok=True)
          except Exception as e:
               return f"Error: creating directory: {e}"
          
     if os.path.exists(target) and os.path.isdir(target):
          return f'Error: "{file_path}" is a directory, not a file'
     

     try:     
    
          with open(target, "w") as f:
               f.write(content)

               return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
          
     except Exception as e:
          return f"Error: writing to file: {e}"
    

        
