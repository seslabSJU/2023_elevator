import yaml
import re

try:
    from config import Config_Log
    config_LOG = Config_Log

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
    log_path = config_LOG.log_file_path
    target_pattern = config_LOG.extract_pattern

    extracted_data = []

    with open(log_path, 'r') as file:
        line_number = 1
        for line in file:
            print("Reading Line Number {}".format(line_number))
            line_number += 1

            matches = re.findall(target_pattern, line)
            if len(matches) != 0:
                extracted_data.append(matches)

    return extracted_data