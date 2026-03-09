import os
import importlib
from parser import parse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BIN_PATH = os.path.join(BASE_DIR, "bin")

startup_path = os.path.expanduser("~")
os.chdir(startup_path)

while True:
    try:
        cmd = input(os.getcwd() + ">")

        # Exit command
        if cmd == "exit":
            break

        # Send input to parser
        parsed = parse(cmd)

        if parsed is None:
            continue

        command_name = parsed["command"]
        options = parsed["options"]

        command_file = os.path.join(BIN_PATH, command_name + ".py")

        if os.path.exists(command_file):
            module_name = f"bin.{command_name}"
            try:
                module = importlib.import_module(module_name)
                module.run(options)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Command not found...")
    except KeyboardInterrupt:
        exit