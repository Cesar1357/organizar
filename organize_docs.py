from importlib.resources import path
import os
import shutil

from_dir = "C:/Users/TOSHIBA/Downloads"
to_dir = "C:/Users/TOSHIBA/Downloads/docs"
list_of_files = os.listdir(from_dir)
# print(list_of_files)

for fileName in list_of_files:
    name,extension = os.path.splitext(fileName)
    # print(name)
    # print(extension)
    if extension == "":
        continue
    if extension in [".zip"]:
        path1 = from_dir + "/" + fileName
        path2 = to_dir + "/" + "docs"
        path3  = to_dir + "/" + "docs" + "/" + fileName
        # print(path1)
        # print(path3)
        if os.path.exists(path2):
            print("Moviendo "+fileName+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moviendo "+fileName+"..." )
            shutil.move(path1,path3)