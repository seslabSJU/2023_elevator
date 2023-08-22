import os
import yaml
import re
import config

log_path = config.Config_Log.log_file_path
def get_class_id_list(yaml_path):
    with open(yaml_path, 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
        class_list = yaml_data['names']

    return class_list

def append_class_id_list_with_flag(class_list):
    list = []

    for key, value in enumerate(class_list):
        list.append(value)
        #list.append([value, False])

    return list

def print_class_id(class_id_list, yaml_path):
    class_list = get_class_id_list(yaml_path)

    # Print Class id on image`
    for class_id in class_id_list:
        if class_id < len(class_list):
            label_text = f"Button {class_list[class_id]} is Green!"
            print(label_text)
        else:
            label_text = f"Class ID: {class_id}"
def class_detected(class_id, class_list):
    class_list[class_id][1] = True
    return class_list
def is_class_already_detected(class_id, class_list):
    return class_list[class_id][1]

def get_green_button_indexes(class_list):
    green_button_list = []

    for i, class_id in enumerate(class_list):
        if class_id:
            green_button_list.append(c)

    #print(green_button_list)
    return green_button_list

def check_this_class_is_really_green(class_id, class_list):
    pass

def log_green_button(config, previous_green_button_list, now_green_button_list):
    basename = os.path.basename(config.Detection_path['image_file_path'])
    frame_str = basename.replace("frame_", "").replace(".jpg", "")
    frame_number = int(frame_str)

    if not previous_green_button_list == now_green_button_list:
        log = "Condition Changed at {}\nPrevious Condition was : {}\nLatest Condition is : {}\n\n".format(basename, previous_green_button_list, now_green_button_list)

        with open(log_path, "a") as f:
            f.write(log)
        return frame_number

    else:
        return None

def log_interval(interval):
    log = "Interval Between Previous Conditional Change is : {}s\n\n".format(interval)
    with open(log_path, "a") as f:
        f.write(log)

def get_classid_list_from_log():
    log_path = config.Config_Log.log_file_path
    target_pattern = config.Config_Log.extract_pattern

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