from os import listdir, path, walk, getcwd, mkdir
from results import save_to_json
import display
import json


files_list = {}

EXTENSIONS_LIST = [".sh", ".crt", ".pem", ".so", ".conf", ".script", ".bin", ".c", ".cpp", ".js", ".php", ".py"]

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

def find_with_extension(root_path, firmware):
    for extension in EXTENSIONS_LIST:
        # print("Find all files ending with `{}` extension....".format(extension))
        files_list[extension] = []
        for root, dirs, files in walk(root_path):
            for name in files:
                if name.endswith(extension):
                    files_list[extension].append({
                        'file_name': name,
                        'path': path.join(root, name)
                    })
        print("+ Number of files ending with " + display.Color.YELLOW + extension + display.Color.END + " extension: " + display.Color.YELLOW + str(len(files_list[extension])) + display.Color.END)
        
        # Save results to a json file under a new directory 'output'
        files_extension = save_to_json(firmware, files_list, "_extension")

    print("Output is saved into file: " + display.Color.YELLOW + files_extension + display.Color.END) 
    return files_list