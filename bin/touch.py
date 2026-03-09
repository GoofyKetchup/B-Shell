def run(options):
    file = options.get("file", None)
    if not file:
        print("Please enter a file full name after -file.")
        return
    try:
        with open(file, "a") as f:
            pass
        print(f"File {file} succefully got created!")
    except Exception as e:
        print(f"Error : {e}")