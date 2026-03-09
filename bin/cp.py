import shutil
import os

def run(options):
    src = options.get("src", None)
    dst = options.get("dst", None)
    if not src or not dst:
        print("Please enter correct source and destination.")
        return

    if not os.path.exists(src):
        print("Source not Exist!")
        return
    
    try:
        shutil.copy(src, dst)

        print(f"{src} Was succefully Copied to {dst}")
    except Exception as e:
        print(f"Error : {e}")