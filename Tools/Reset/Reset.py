def reset():

    print("Reseting Shell to factory source code")

    with open("C:/Users/YOUR_USER/Desktop/Project/B-Shell/Tools/Reset/ResetData/Main.py", "r") as file:
        R3 = file.read()
        print("30% finished")

    with open("C:/Users/YOUR_USER/Desktop/Project/B-Shell/Main.py", "w") as file:
        file.write(R3)
        print("45% finished")

    with open("C:/Users/YOUR_USER/Desktop/Project/B-Shell/Tools/Reset/ResetData/Commands.py", "r") as file:
        R3 = file.read()
        print("75% finished")

    with open("C:/Users/YOUR_USER/Desktop/Project/B-Shell/Commands.py", "w") as file:
        file.write(R3)
        print("90% finished")

    print("Finishing reset...")
    print("Shell succefully reset!")

    input("Press Enter to exit...")
