from pathlib import Path
import os
import sys
import shutil

default_path = Path(__file__).resolve().parent

#Ya I don't know if you already use register in high level script, but it's fun

R1 = 0 # Register for operation
R2 = default_path # Register for pointer
R3 = "" # Register for stockage
R4 = None # Register for argument

print("B-Shell v0.2")
print("GoofyKetchup. 2025 MIT, Worst Open-Source Shell.")
print("")
print("""Install new version on my github "github.com/GoofyKetchup" for new commands""")
print("")
print("")

def create(args):
    filename = args[0]
    extension = args[1]
    with open(f"{filename}.{extension}", "w"):
        pass
    print("File created.")

def create_ubs(filename, extension):
    with open(f"{filename}.{extension}", "w"):
        pass

def load(args):
    global R3
    filename = args[0]
    extension = args[1]
    if extension == "txt" or "py":
        with open(f"{filename}.{extension}", "r") as file:
            R3 = file.read()
            print(f"File loaded. \n{R3}")

def load_ubs(path, filename, extension):
    global R3
    with open(f"{path}", "r") as file:
        R3 = file.read()
        return R3

def write(args):
    global R3
    wordon = args[0]
    filename = args[1]
    extension = args[2]
    new_text = args[3:]
    if extension == "txt" or "py":
        with open(f"{filename}.{extension}", "w") as file:
            file.write(" ".join(new_text))
            R3 = " ".join(new_text)
            print(f"File saved. \n{R3}")

def delete(args):
    filename = args[0]
    extension = args[1]
    Confirm = input("Are you sure you want to delete the file? (y/n): ")
    if Confirm == "y":
        os.remove(f"{filename}.{extension}")
        print("File deleted.")
    if Confirm == "n":
        print("Delete cancelled.")


def echo(args):
    global R3
    R3 = " ".join(args)
    print(R3)

def Help(args):
    global R3
    R3 = ("B-shell command:\n"
          "\n"
          "Create: Create a files(only work with .txt or .py!)\n"
          "Load: Load the text of a file and print it\n"
          "Write: Write on a text or python file\n"
          "Delete: Delete the file\n"
          "Execute: Execute a file\n"
          "Rename: Rename a file\n"
          "Cd: Change the actual path\n"
          "Pwd: Show the actual Path\n"
          "Cf: Create a folder\n"
          "Echo: Echo the chosen text\n"
          "Help: Show help\n"
          "Add: Add up 2 number chosen(Only use , not .)\n"
          "Sub: Subtract 2 number(Only use, not .)\n"
          "Mul: Multiple 2 number(Only use, not .)\n"
          "Div: Divide 2 number(Only use, not .)\n"
          "(Use -f to calcul float number)\n"
          "Move: Move a file to a path\n"
          "Ls: show every file/folder in current path\n"
          "Clear: Clear the Shell history\n"
          "Reload: Reload a new instance of the shell\n"
          "\n"
          "Hope this helped you.\n")
    print(R3)

def rename(args):
    try :
        filename = args[0]
        extension = args[1]
        wordto = args[2]
        newfilename = args[3]
        newextension = args[4]
        os.rename(f"{filename}.{extension}", f"{newfilename}.{newextension}")
        print(f"File renamed to {newfilename}.{newextension} .")

    except Exception as e:
        foldername = args[0]
        var = args[1]
        newfoldername = args[2]
        os.rename(foldername, newfoldername)
        print(f"Folder renamed to {newfoldername} .")


def execute(args):
    filename = args[0]
    extension = args[1]
    os.startfile(f"{filename}.{extension}")
    print(f"File executed successfully.")

def cd(args):
    global R2
    newpath = " ".join(args)
    if os.path.isdir(newpath):
        os.chdir(newpath)
        R2 = os.getcwd()
    if not os.path.isabs(newpath):
        newpath = os.path.join(R2, newpath)
    if not os.path.isdir(args) and not os.path.isdir(newpath):
        print("Path not found...")

def cf(args):
    dirname = args[0]
    chemin = os.path.join(os.getcwd(), dirname)
    os.makedirs(chemin, exist_ok=True)
    print("Folder created...")

def pwd(args):
    print(os.getcwd())

def add(args):
    global R1
    if args[0] == "-f":
        Result = float(args[1]) + float(args[2])
        R1 = str(Result)
        print(str(R1))
    else:
        Result = int(args[0]) + int(args[1])
        R1 = str(Result)
        print(str(R1))

def sub(args):
    global R1
    if args[0] == "-f":
        Result = float(args[1]) - float(args[2])
        R1 = str(Result)
        print(str(R1))
    else:
        Result = int(args[0]) - int(args[1])
        R1 = str(Result)
        print(str(R1))

def mul(args):
    global R1
    if args[0] == "-f":
        Result = float(args[1]) * float(args[2])
        R1 = str(Result)
        print(str(R1))
    else:
        Result = int(args[0]) * int(args[1])
        R1 = str(Result)
        print(str(R1))

def div(args):
    global R1
    if args[0] == "-f":
        Result = float(args[1]) / float(args[2])
        R1 = str(Result)
        print(str(R1))
    else:
        Result = int(args[0]) / int(args[1])
        R1 = str(Result)
        print(str(R1))

def mf(args):
    global R2
    filename = args[0]
    extension = args[1]
    wordto = args[2]
    endpath = args[3]
    full_file = f"{filename}.{extension}"
    full_file_path = os.path.abspath(full_file)
    endpath_abs = os.path.abspath(endpath)
    shutil.move(full_file_path, endpath_abs)
    print("File moved successfully.")

def ls(args):
    global R2
    entries = os.listdir(R2)

    files = [f for f in entries if os.path.isfile(os.path.join(R2, f))]
    dirs = [d for d in entries if os.path.isdir(os.path.join(R2, d))]

    print("Folder:")
    for d in dirs:
        print(f"    {d}/")
    print("Files:")
    for f in files:
        print(f"    {f}")

def clear(args):
    print("\n" * 100)

def reload(args):
    print("Reloading shell...")
    clear(args)
    os.execv(sys.executable, [sys.executable] + sys.argv)

def reset(args):
    os.startfile("C:/Users/YOUR_USER/Desktop/B-Shell/Tools/Reset/Reset.py")
