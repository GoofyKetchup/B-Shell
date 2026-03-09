import os

def run(options):
    path = options.get("path", os.getcwd())
    try:
        files = os.listdir(path)
        if not files:
            print("This Directory is Empty.")
            return
        else:
            for f in files:
                print(f)
    except Exception as e:
        print(f"Error : {e}")