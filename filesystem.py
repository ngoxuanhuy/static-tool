from os import listdir, path, walk
import json

files_list = {}

def find_root_path(cwd):
    dir_list = listdir(cwd)
   
    for element in dir_list:
        current_path = path.join(cwd, element) 

        if (current_path.endswith("squashfs-root")):
            return True, current_path
        if (path.isdir(current_path)):
            flag, msg = find_root_path(current_path)
            if (flag):
                return flag, msg
    return False, "Can't find the root filesystem"

def find_with_extension(root_path, extension):
    print("Find all files ending with `{}` extension....".format(extension))
    files_list[extension] = []
    for root, dirs, files in walk(root_path):
        for name in files:
            if name.endswith(extension):
                files_list[extension].append({
                    'file_name': name,
                    'path': path.join(root, name)
                })
    print("Number of files ending with `{}` extension: {}".format(extension, len(files_list[extension])))
    print("-----------------------------------------------")
    with open("file_extension.json", "w+") as output_file:
        json.dump(files_list, output_file)
    return files_list