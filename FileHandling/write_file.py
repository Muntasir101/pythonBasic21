import os

file_name = "demofile2.txt"

if os.path.exists(file_name):
    file = open(file_name, "w")
    file.write("Hello Python 2")
    file.close()
else:
    print("Cant write !! The file does not exist.")