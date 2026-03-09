import shlex

def parse(input_string):
    parts = shlex.split(input_string)
    
    command = parts[0]
    options = {}

    i = 1
    while i < len(parts):
        if parts[i].startswith("-"):
            key = parts[i][1:]

            if i + 1 < len(parts) and not parts[i + 1].startswith("-"):
                value = parts[i + 1]
                i += 1
            else:
                value = True

            options[key] = value
        else:
                print(f"Correct Syntax: command -option value -option value -option value")
                return None

        i += 1

    return {
        "command": command,
        "options": options,
    }