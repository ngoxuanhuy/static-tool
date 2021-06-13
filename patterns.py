import re
import json
import display
import os
from results import save_to_json

json_data = {}

def find_accounts(root_path, firmware):
    json_data["accounts"] = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            full_path = os.path.join(root, file)
            if (full_path.endswith("/etc/passwd")):
                # Read the file content, extract accounts and save results to a json file
                f = open(full_path, "r")
                for line in f:
                    fields = line.split(":")
                    json_data["accounts"].append({
                        "username": fields[0],
                        "password": fields[1],
                        "UID": fields[2],
                        "groupID": fields[3],
                        "GECOS": fields[4],
                        "home_dir": fields[5],
                        "shell": fields[6]
                    })
    print("+ Found " + display.Color.YELLOW + str(len(json_data["accounts"])) + display.Color.END + " possible system's accounts: ")
    for account in json_data["accounts"]:
        print("  " + display.Color.YELLOW + account["username"] + display.Color.END)
    print()     

    # Save results to a json file under a new directory 'output'
    file_extraction = save_to_json(firmware, json_data, "_extraction")             


def find_keys(root_path, firmware):
    json_data["keys"] = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            full_path = os.path.join(root, file)
            if (full_path.endswith(".key")):
                # Read the file content, extract accounts and save results to a json file
                f = open(full_path, "r")
                json_data["keys"].append({
                    "file_name": file,
                    "location": full_path,
                    "content": f.read()
                })
    print("+ Found " + display.Color.YELLOW + str(len(json_data["keys"])) + display.Color.END + " possible keys: ")
    for key in json_data["keys"]:
        print("  " + display.Color.YELLOW + key["location"] + display.Color.END)
    print()     

    # Save results to a json file under a new directory 'output'
    file_extraction = save_to_json(firmware, json_data, "_extraction")

    print("Output is saved into file: " + display.Color.YELLOW + file_extraction + display.Color.END) 