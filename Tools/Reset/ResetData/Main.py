import re
import Commands

COMMANDS = {
    "create": Commands.create,
    "load": Commands.load,
    "write": Commands.write,
    "rename": Commands.rename,
    "delete": Commands.delete,
    "execute": Commands.execute,
    "cd": Commands.cd,
    "pwd": Commands.pwd,
    "cf": Commands.cf,
    "echo": Commands.echo,
    "help": Commands.Help,
    "add": Commands.add,
    "sub": Commands.sub,
    "mul": Commands.mul,
    "div": Commands.div,
    "move": Commands.mf,
    "ls": Commands.ls,
    "clear": Commands.clear,
    "reload": Commands.reload,
}

def bshell_loop():
    while True:
        try:
            Request = input(f"{Commands.R2}>>>")

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

        except KeyboardInterrupt:
            print("Keyboard interrupted...")
            break

        except Exception as e:
            print("Error catched: ", e, ".")

if __name__ == "__main__":
    bshell_loop()