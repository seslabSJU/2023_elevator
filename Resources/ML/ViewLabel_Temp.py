import re
import sys

import cv2
import os
import yaml
import time

import Detect_Color
def get_label_data(label_text_path):
    label_data = []

    with open(label_text_path, 'r') as f:
        labels = f.readlines()

    for label_info in labels:
        label_info = label_info.strip().split(' ')

        class_id = int(label_info[0])
        x = float(label_info[1])
        y = float(label_info[2])
        width = float(label_info[3])
        height = float(label_info[4])

        label_data.append((class_id, x, y, width, height))

    return label_data
def display_label_info(image, label_text_path, yaml_path):
    #image = cv2.imread(image_path)
    label_data = get_label_data(label_text_path)

    text_height = 30  # Height of each label text
    text_margin = 20  # Margin between label texts and image border
    text_offset = text_margin

    for label in label_data:
        class_id, x, y, width, height = label

        image_height, image_width, _ = image.shape
        left = int((x-width/2) * image_width)
        top = int((y-height/2) * image_height)
        right = int((x+width/2) * image_width)
        bottom = int((y+height/2) * image_height)

        #print("left " + str(left) + ", top " + str(top), ", right " + str(right), ", bottom ", str(bottom))
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        label_text = f"Class ID: {class_id}"

        with open(yaml_path, 'r') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
            class_lables = yaml_data['names']

        if class_id < len(class_lables):
            label_text = f"Class ID: {class_id} - {class_lables[class_id]}"
        else:
            label_text = f"Class ID: {class_id}"

        font_scale = 0.75
        font_color_white = (255, 255, 255)
        font_color_black = (0, 0, 0)

        if class_lables[class_id] == "Green":
            cv2.putText(image, label_text, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color_black, 2)
        else:
            cv2.putText(image, label_text, (text_margin, text_offset), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color_black, 2)
            text_offset += text_height

    cv2.imshow('sample', image)
    key = cv2.waitKey(0)

def number_extract(filename):
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    else:
        return -1
def read_all_img_from_folder(folder_path, label_folder_path):
    files = os.listdir(folder_path)
    img_files = [f for f in files if f.lower().endswith('.jpg')]

    img_files = sorted(img_files, key=number_extract)

    for img_file in img_files:
        filename, extension = os.path.basename(img_file).split('.')
        image_path = os.path.join(folder_path, img_file)
        label_file_path = os.path.join(label_folder_path, filename+".txt")
        print(image_path)
        print(label_file_path)
        if not os.path.exists(label_file_path):
            update_label(image_path, label_file_path, yaml_path)


def read_label_from_txt(image_path, label_txt_path):
    image = cv2.imread(image_path)

    with open(label_txt_path, 'r') as f:
        labels = f.readlines()

    label_data = []

    for label_info in labels:
        label_info = label_info.strip().split(' ')

        class_id = int(label_info[0])
        x = float(label_info[1])
        y = float(label_info[2])
        width = float(label_info[3])
        height = float(label_info[4])

        label_data.append((class_id, x, y, width, height))

    return label_data
def update_label_txt_with_new_data(new_label_path, label_data):
    with open(new_label_path, 'w') as f:
        for label in label_data:
            class_id, x, y, width, height = label
            f.write(f"{class_id} {x} {y} {width} {height}\n")

def delete_label_txt_with_class_id(new_label_path, class_id):
    try:
        with open(new_label_path, 'r') as f:
            lines = f.readlines()
        with open(new_label_path, 'w') as f:
            for line in lines:
                arg = line.split()

                if(arg[0] == class_id):
                    continue
                f.write(line)

    except:
        print("No Label txt")

def move_label_txt(argv, label_data):
    # x, y, width, height = [1], [2], [3], [4]
    if argv[0] == "u":
        if len(argv) == 2:
            axis_unit = float(argv[1])
            for i in range(len(label_data)):
                label_data[i] = (
                    label_data[i][0], label_data[i][1], label_data[i][2] - axis_unit, label_data[i][3],
                    label_data[i][4])

        elif len(argv) == 3 and argv[1].isdigit():
            axis_unit = float(argv[2])
            for i in range(len(label_data)):
                if (label_data[i][0] == int(argv[1])):
                    label_data[i] = (
                        label_data[i][0], label_data[i][1], label_data[i][2] - axis_unit, label_data[i][3],
                        label_data[i][4])
    elif argv[0] == "d":
        if len(argv) == 2:
            axis_unit = float(argv[1])
            for i in range(len(label_data)):
                label_data[i] = (
                    label_data[i][0], label_data[i][1], label_data[i][2] + axis_unit, label_data[i][3],
                    label_data[i][4])

        elif len(argv) == 3 and argv[1].isdigit():
            axis_unit = float(argv[2])
            for i in range(len(label_data)):
                if (label_data[i][0] == int(argv[1])):
                    label_data[i] = (
                        label_data[i][0], label_data[i][1], label_data[i][2] + axis_unit, label_data[i][3],
                        label_data[i][4])
    elif argv[0] == "l":
        if len(argv) == 2:
            axis_unit = float(argv[1])
            for i in range(len(label_data)):
                label_data[i] = (
                    label_data[i][0], label_data[i][1] - axis_unit, label_data[i][2], label_data[i][3],
                    label_data[i][4])

        elif len(argv) == 3 and argv[1].isdigit():
            axis_unit = float(argv[2])
            for i in range(len(label_data)):
                if (label_data[i][0] == int(argv[1])):
                    label_data[i] = (
                        label_data[i][0], label_data[i][1] - axis_unit, label_data[i][2], label_data[i][3],
                        label_data[i][4])
    elif argv[0] == "r":
        if len(argv) == 2:
            axis_unit = float(argv[1])
            for i in range(len(label_data)):
                label_data[i] = (
                    label_data[i][0], label_data[i][1] + axis_unit, label_data[i][2], label_data[i][3],
                    label_data[i][4])

        elif len(argv) == 3 and argv[1].isdigit():
            axis_unit = float(argv[2])
            for i in range(len(label_data)):
                if (label_data[i][0] == int(argv[1])):
                    label_data[i] = (
                        label_data[i][0], label_data[i][1] + axis_unit, label_data[i][2], label_data[i][3],
                        label_data[i][4])

    return label_data

def resize_label(argv, label_data):
    for i in range(len(label_data)):
        if (label_data[i][0] == int(argv[1])):
            label_data[i] = (
                label_data[i][0], label_data[i][1], label_data[i][2], argv[2],
                argv[3])
    return label_data

def lookup_label(argv, label_data):
    print("Lookup Data is :\n")
    for i in range(len(label_data)):
        if (label_data[i][0] == int(argv[1])):
            print(label_data[i])

def make_label(argv, label_path):
    print(label_path)

    class_id = argv[1]
    x, y, width, height = argv[2], argv[3], argv[4], argv[5]
    with open(label_path, 'a') as f:
        f.write(f"{class_id} {x} {y} {width} {height}\n")
        f.close()

def make_label_like_class_id(argv, label_data, label_path):
    print(label_path)

    margin = 0.05

    for i in range(len(label_data)):
        if (label_data[i][0] == int(argv[2])):
            x, y, width, height = label_data[i][1], label_data[i][2], label_data[i][3], label_data[i][4]
    x += margin
    y += margin
    width += margin
    height += margin

    print(x, y, width, height)

    with open(label_path, 'a') as f:
        f.write(f"{argv[1]} {x} {y} {width} {height}\n")
        f.close()
def update_label(image_path, label_txt_path, yaml_path):
    label_data = read_label_from_txt(image_path, base_label_file_path)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    label_dir, label_file = os.path.split(label_txt_path)
    label_name, label_ext = os.path.splitext(label_file)
    new_label_name = f"{label_name}_{timestamp}{label_ext}"
    new_label_path = os.path.join(label_dir, new_label_name)

    update_label_txt_with_new_data(label_txt_path, label_data)
    update_label_txt_with_new_data(new_label_path, label_data)
    display_label_info(image_path, label_txt_path, yaml_path)
    label_updated = False

    while True:
        inp = input("Left = l, Right = r, Up = u, Down = d : ")

        argv = inp.split()
        # print(argv[0])
        # print(len(argv))

        if argv[0] == 'Q':
            print("Quit")
            sys.exit(0)
        elif argv[0] == "u":  # Up arrow key
            label_data = move_label_txt(argv, label_data)
            update_label_txt_with_new_data(new_label_path, label_data)
            display_label_info(image_path, new_label_path, yaml_path)
            label_updated = True
            cv2.destroyAllWindows()
        elif argv[0] == "d":  # Down arrow key
            label_data = move_label_txt(argv, label_data)
            update_label_txt_with_new_data(new_label_path, label_data)
            display_label_info(image_path, new_label_path, yaml_path)
            label_updated = True
            cv2.destroyAllWindows()
        elif argv[0] == 'l':  # Left arrow key
            label_data = move_label_txt(argv, label_data)
            update_label_txt_with_new_data(new_label_path, label_data)
            display_label_info(image_path, new_label_path, yaml_path)
            label_updated = True
            cv2.destroyAllWindows()
        elif argv[0] == 'r':
            label_data = move_label_txt(argv, label_data)
            update_label_txt_with_new_data(new_label_path, label_data)
            display_label_info(image_path, new_label_path, yaml_path)
            label_updated = True
            cv2.destroyAllWindows()
        elif argv[0] == "del":
            if len(argv) == 2:
                delete_label_txt_with_class_id(new_label_path, argv[1])
                display_label_info(image_path, new_label_path, yaml_path)
                label_updated = True
                cv2.destroyAllWindows()
        elif argv[0] == "LK":
            if len(argv) == 2:
                lookup_label(argv, label_data)
        elif argv[0] == "RS":
            if len(argv) == 4:
                label_data = resize_label(argv, label_data)
                update_label_txt_with_new_data(new_label_path, label_data)
                display_label_info(image_path, new_label_path, yaml_path)
                label_updated = True
                cv2.destroyAllWindows()
        elif argv[0] == "MK":
            if len(argv) == 6:
                make_label(argv, new_label_path)
                display_label_info(image_path, new_label_path, yaml_path)
        elif argv[0] == "MKL":
            if len(argv) == 3:
                make_label_like_class_id(argv, label_data, new_label_path) #Has Data
                display_label_info(image_path, new_label_path, yaml_path)
        elif argv[0] == "SAVE":
            update_label_txt_with_new_data(label_txt_path, label_data)
        elif argv[0] == "NEXT":
            break

        label_data = read_label_from_txt(image_path, new_label_path)
        # for line in label_data:
        #     print(line)
    cv2.destroyAllWindows()

    if label_updated:
        update_label_txt_with_new_data(label_txt_path, label_data)
        print(f"Updated labels saved as {new_label_name}")

def view_label(img_path, label_path, yaml_path):
    update_label(img_path, label_path, yaml_path)


if __name__== '__main__':
    image_path = r"E:/ML/Elevator Git/Effective-Elevator-Energy-Calculation-for-SejongAI-Center/Images_Sample/Elevator_Sample/"
    yaml_path = r"E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Sample\data.yaml"
    label_folder_path =  "E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Sample\Sample_Annotes\\"
    base_label_file_path = r"E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Sample\Sample_Annotes\Base.txt"

    sample_img_path = r"E:/ML/Elevator Git/Effective-Elevator-Energy-Calculation-for-SejongAI-Center/Images_Sample/Elevator_Sample/frame_1080.jpg"
    sample_label_path = "E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\yolov8\\annotations\\frame_1080.jpg.txt"

    axis_unit = 0.05

    update_label(image_path, label_text_path, yaml_path)
    read_all_img_from_folder(image_path, label_folder_path)
    view_label(sample_img_path, sample_label_path, yaml_path)