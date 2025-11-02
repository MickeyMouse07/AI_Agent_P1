import os

def write_file(working_directory, file_path, content):
     target = os.path.abspath(os.path.join(working_directory, file_path))
     wd = os.path.abspath(working_directory)

     try:
          if not target.startswith(wd):
               return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
          if not os.path.exists(wd):
               os.makedirs(wd)
          

        

          with open(target, "w") as f:
               f.write(content)

               return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
          

     except Exception as e:
          return f"Error: {e}"
    

        
