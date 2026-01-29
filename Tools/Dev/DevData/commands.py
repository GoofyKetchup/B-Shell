import shutil
import os
import subprocess

def boilerplate(args):
    type = args[0]
    wordto = args[1]
    path = args[2]
    if wordto != "to":
        print("Correct syntax : boilerplate <type> to <path>")
    if not args:
        print("Correct syntax : boilerplate <type> to <path>")
    if type == "html":
        shutil.copy2("C:/Users/bekhtim3/Desktop/Project/B-Shell/Tools/Dev/DevData/boilerplate/New HTML Project", path)
    if type == "python":
        shutil.copy2("C:/Users/bekhtim3/Desktop/Project/B-Shell/Tools/Dev/DevData/boilerplate/New Python Project", path)
    if type != "html" or "python":
        print("Type not found!")

def depend(args):
    action = args[0]
    if action == "install":
        type = args[1]
        path = args[2]
        if type == "python":
            subprocess.run(["pip", "install", "-r", path])

    if not args:
        print("Correct syntax : depend <action> <type> <filepath>")

def run(args):
    pass