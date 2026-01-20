import os
import shutil

def reset():

    print("Reseting Shell to factory source code")

    RESET_DIR = os.path.dirname(os.path.abspath(__file__))

    ROOT_DIR = os.path.abspath(os.path.join(RESET_DIR, "..", ".."))

    clean_main = os.path.join(RESET_DIR, "Main.py")
    clean_commands = os.path.join(RESET_DIR, "Commands.py")

    target_main = os.path.join(RESET_DIR, "Main.py")
    target_commands = os.path.join(RESET_DIR, "Commands.py")

    print("15% finished...")

    shutil.copyfile(clean_main, target_main)
    print("55% finished...")
    shutil.copyfile(clean_commands, target_commands)
    print("67% finished...")

    print("Finishing reset...")
    print("Shell succefully reset!")
    input("Press Enter to exit...")
