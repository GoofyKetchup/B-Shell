def run(options):
    text = options.get("text", "")
    if text:
        print(text)
    else:
        print("No text Provided")
        return