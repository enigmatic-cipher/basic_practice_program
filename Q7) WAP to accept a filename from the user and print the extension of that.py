filename = input("Enter the name of the file: ")
file_ext = filename.split(".")
print("The extension of the file is, " + repr(file_ext[-1]))