import os

def run(options):
    if "create" in options:
        filename = options.get("create", None)
        size = options.get("size", None)

        if not filename or not size:
            print("Please enter a filename and size for the disk.")
            return
        
        try:
            size = int(size)
        except ValueError:
            print("Size must be an integer.")
            return
        
        try:
            with open(filename, "wb") as f:
                f.write(b"\0" * size * 1024 * 1024)
                print(f"Disk '{filename}' created with size {size} MB.")
        except Exception as e:
            print(f"Error creating disk: {e}")
            return
        
    if "floppy" in options:
        filename = "floppy.img"
        try:
            with open(filename, "wb") as f:
                f.write(b"\0" * 1440 * 1024)
                print(f"Floppy disk '{filename}' created with size 1.44 MB.")
        except Exception as e:
            print(f"Error : {e}")
            return