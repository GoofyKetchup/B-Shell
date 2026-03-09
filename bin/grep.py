def run(options):
    text = options.get("text", None)
    file = options.get("file", None) 

    if not text or not file:
        print("Please provide both text and file in options.")
        return
    
    try:
        with open(file, 'r') as f:
            for line in f:
                if text in line:
                    print(line.strip())
    except Exception as e:
        print(f"Error : {e}")