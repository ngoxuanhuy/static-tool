from extract import scan_recursively
from filesystem import find_root_path, find_with_extension
import sys
from os import getcwd, path

EXTENSIONS_LIST = [".sh", ".crt", ".pem", ".so", ".conf", ".script", ".bin"]
CODE_EXTENSIONS_LIST = [".c", ".cpp", ".js", ".php", ".py"]

def main():
    print("Name of program: ", sys.argv[0])
    print()
    firmware = sys.argv[len(sys.argv)-1]
    print("=====")
    print("Scan file: ", firmware)

    modules = scan_recursively(firmware)

    extracted_directory = "_" + firmware + ".extracted"
    flag, root_path = find_root_path(extracted_directory)

    print("Full path of the root filesystem: ", root_path)

    for extensions in EXTENSIONS_LIST:
        find_with_extension(path.join(getcwd(),root_path), extensions)

    for extensions in CODE_EXTENSIONS_LIST:
        find_with_extension(path.join(getcwd(),root_path), extensions)


if __name__ == "__main__":
    main()