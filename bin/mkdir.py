import os

def run(options):
    dir = options.get("dir", None)
    if not dir:
        print("Please enter a directory name after -dir")
        return
    try:
        os.mkdir(dir)
        print(f"{dir} Directory got created with Success!")
    except Exception as e:
        print(f"Error : {e}")