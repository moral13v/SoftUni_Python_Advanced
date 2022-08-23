from os import listdir, path


def traverse_dir(current_path, files_ext):
    for element in listdir(current_path):
        if path.isdir(path.join(current_path, element)):
            traverse_dir(path.join(current_path, element), files_ext)
        else:
            ext = element.split('.')[-1]
            if ext not in files_ext:
                files_ext[ext] = []
            files_ext[ext].append(element)


files_ext = {}
traverse_dir(".", files_ext)

for ext, files in sorted(files_ext.items()):
    print(f"{ext}")
    for file in sorted(files):
        print(f"---{file}")
