import json
import os
import display

def save_to_json(firmware, results, type):
    new_dir = os.path.join(os.getcwd(), "output")
    if not os.path.exists(new_dir):
         os.mkdir(new_dir)

    file_name = ""
    if (type == "_extension"):
        file_name = os.path.join(new_dir, firmware.split(".")[0] + type + ".json")
        with open(str(file_name), "w+") as output_file:
            json.dump(results, output_file)
    elif (type == "_extraction"):
        file_name = os.path.join(new_dir, firmware.split(".")[0] + type + ".json")
        with open(str(file_name), "w+") as output_file:
            json.dump(results, output_file)
    return file_name
   
