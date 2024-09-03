import os

file = "E:\\PnT_Online_21\\17th Class\\test2.txt"

if os.path.exists(file):
    file_text = open(file, "r")
    # print(file_text.read())
    # print(file_text.read(10))
    print(file_text.readline())
    file_text.close()
else:
    print("Cant Read file.No file found.")
