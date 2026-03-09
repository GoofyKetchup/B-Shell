import os

def run(options):
    try:
        print(os.getcwd())
    except Exception as e:
        print(f"Error : {e}")