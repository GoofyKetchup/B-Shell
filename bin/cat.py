def run(options):
    file = options.get("file", None)
    if not file:
        print("Please enter a File Path after -file")
        return
    try:
        with open(file, "r") as f:
            print(f.read())
    except Exception as e:
        print(f"Error : {e}")