import os
from os import walk

files_by_ext = {}

username = os.getlogin()

for root, dirs, files in walk('.'):
    for file in files:
        ext = file.split('.')[-1]
        if ext not in files_by_ext:
            files_by_ext[ext] = []
        files_by_ext[ext].append(file)

with open(f"C:\\Users\\{username}\\Desktop\\result.txt", "w") as output:
    for ext, files in sorted(files_by_ext.items()):
        output.write(f"{ext}\n")
        for file in sorted(files):
            output.write(f"---{file}\n")

