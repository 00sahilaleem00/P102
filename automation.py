# a task that takes me a lot of time is deleting my downloads folder
# i will automate the program so that it automatically deletes all the files in the folder
# to do this, I will borrow from the code from some of the previous projects (p99)

import os
import shutil

path = "C:/Users/Sahil Aleem/Downloads"

for currentPath, directories, files in os.walk(path):
    for i in directories:
        folderPath = os.path.join(currentPath, i)
        if(folderPath != "C:/Users/Sahil Aleem/Downloads\\C68..."):
            shutil.rmtree(folderPath)
    for j in files:
        filePath = os.path.join(currentPath, j)
        os.remove(filePath)
