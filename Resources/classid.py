import os
import yaml
import re

try:
    from config import Config_DefaultPath, Config_Log

except Exception as e:
    pass

def get_class_id_list(yaml_path):
    with open(yaml_path, 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
        class_list = yaml_data['names']

    return class_list

def print_class_id(class_id_list, yaml_path):
    class_list = get_class_id_list(yaml_path)

    for class_id in class_id_list:
        if class_id < len(class_list):
            label_text = f"Button {class_list[class_id]} is Green!"
            print(label_text)
        else:
            label_text = f"Class ID: {class_id}"

def get_classid_list_from_log():
    txt_name = "Log_Condition.txt"
    target_pattern = Config_Log.extract_pattern

    extracted_data = []

    os.chdir(Config_DefaultPath.config_default_path)

    with open(txt_name, 'r') as file:
        line_number = 1
        for line in file:
            print("Reading Line Number {}".format(line_number))
            line_number += 1

            matches = re.findall(target_pattern, line)
            if len(matches) != 0:
                extracted_data.append(matches)

    return extracted_data
