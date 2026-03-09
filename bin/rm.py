import os
import shutil

def run(options):
    file = options.get("file", None)
    if not file:
        print("Please specify a file/directory to remove.")
        return
    
    if not os.path.exists(file):
        print("Pleace enter a existing file/directory.")
        return
    
    try:
        if os.path.isdir(file):
            shutil.rmtree(file)
            print("Directory removed successfully.")
        else:
            os.remove(file)
            print("File removed successfully.")
    except Exception as e:
        print(f"Error: {e}")