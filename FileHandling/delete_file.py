import os

if os.path.exists("E:\\PnT_Online_21\\17th Class\\new_file.txt"):
    os.remove("E:\\PnT_Online_21\\17th Class\\new_file.txt")
else:
    print("The file does not exist")
