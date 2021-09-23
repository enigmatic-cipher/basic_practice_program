import os
path = "Note.py"
if os.path.isdir(path):
    print("It is a directory")
elif os.path.isfile(path):
    print("It is file")
else:
    print("Unknown file")
