import subprocess
import os

def run(options):
    file = options.get("file", None)

    if not file:
        print("Please provide a file in options.")
        return
    
    if not os.path.exists(file):
        print("File not found.")
        return
    
    try:
        print("Running the Script...")
        subprocess.run(["python", file], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error while running the Script : {e}")