import os

file = "E:\\PnT_Online_21\\17th Class\\new_file3.txt"

if os.path.exists(file):
    print("Cant create, File already exists.")
else:
    f = open(file, "x")
    print("File Created Successfully")
    f.close()
