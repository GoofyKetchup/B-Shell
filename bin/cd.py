import os

def run(options):
    path = options.get("path", None)
    if not path:
        print("Please enter the path after -path")
        return
    try:
        os.chdir(path)
    except Exception as e:
        print(f"Error : {e}")