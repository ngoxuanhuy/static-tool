from extract import scan_recursively
from filesystem import find_root_path, find_with_extension
from patterns import find_accounts, find_keys
import display
import sys
import os


def main():

    # Display banner
    display.banner()

    # Start scanning firmware
    firmware_name = sys.argv[len(sys.argv)-1]
    print("Start scanning and extracting the firmware: " + display.Color.BLUE + firmware_name + display.Color.END)
    modules = scan_recursively(firmware_name)

    extracted_directory = "_" + firmware_name + ".extracted"
    flag, root_path = find_root_path(extracted_directory)

    print("Full path of the root filesystem: " + display.Color.BLUE + root_path + display.Color.END)
    print("----------------------------------")

    # List all files with specific extensions
    find_with_extension(os.path.join(os.getcwd(),root_path), firmware_name)
    print("----------------------------------")

    # Find all possible accounts from /etc/passwd
    find_accounts(os.path.join(os.getcwd(), root_path), firmware_name)
    find_keys(os.path.join(os.getcwd(), root_path), firmware_name)
    print("Done")

if __name__ == "__main__":
    main()