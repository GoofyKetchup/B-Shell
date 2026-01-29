import DevData.commands
import re
from pathlib import Path

print("DevsTools by B-Shell creator.\n")

path = Path(__file__).resolve().parent

COMMANDS = {
    "boilerplate": DevData.commands.boilerplate,
    "depend": DevData.commands.depend,
}

def dev():
    while True:
        try:
            Request = input(f"{path}:DevsTools>")

            parts = re.split(r'[ .]', Request)

            if not parts:
                continue

            command = parts[0]
            args = parts[1:]

            if command in COMMANDS:
                COMMANDS[command](args)
            else:
                print("Command not founded...")

            if Request == "":
                continue
        except Exception as e:
            print("Error catched: ", e)

def request():
    print("Would you like to use this tool in graphical window?(Y/n) ")
    mode = input()
    if mode == "Y":
        import ui
    if mode == "n":
        dev()

if __name__ == '__main__':
    request()