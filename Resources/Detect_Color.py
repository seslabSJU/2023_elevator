import os.path
import random

import cv2
import yaml
import numpy as np

import config
import ViewLabel
import Sort_image
import classid_list

config_Detection = config.Config_Detection()
config_Color = config.Config_Color()

def detect_color_from_images(folder_path):
    img_path = Sort_image.get_images(folder_path)

    for p in img_path:
        img = cv2.imread(p)
        detect_color(img)

def detect_color(image_file_path, label_text_path, class_list):
    img = cv2.imread(image_file_path)
    lowest_color_to_detect = np.array(config_Color.Color_CV2['cv2_inrange_lowest'], dtype="uint8")
    highest_color_to_detect = np.array(config_Color.Color_CV2['cv2_inrange_highest'], dtype="uint8")

    detected_img = cv2.inRange(img, lowest_color_to_detect, highest_color_to_detect)
    contours, hierarchy = cv2.findContours(detected_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    if not contours:
        empty_contours(class_list)

    else:
        contour_list, hierarchy_list = check_contour_points(contours, hierarchy[0])

        draw_heirarchy_Contours(img, contours, hierarchy)

        class_list = detect_which_class_is_dot_in(img, label_text_path, class_list, contour_list, hierarchy_list)

        #print(class_list)

    green_button_list = classid_list.get_green_button_indexes(class_list)
    #ViewLabel.display_label_info(img, label_text_path)

    return green_button_list

def check_contour_points(contour_list, hierarchy_list):
    new_hierarchy_list = []
    final_contour = []
    final_hierarchy = []

    for i, hierarchy in enumerate(hierarchy_list):
        hierarchy = np.append(hierarchy, i)
        new_hierarchy_list.append(hierarchy)

    np_new_hierarchy_list = np.array(new_hierarchy_list)

    for i, contour in enumerate(contour_list):
        area = cv2.contourArea(contour)
        if area > config_Detection.Detection_Range['MinCircleArea']:
            final_contour.append(contour)
            final_hierarchy.append(np_new_hierarchy_list[i])

    return final_contour, final_hierarchy

def draw_heirarchy_Contours(image, contour_list, hierarchy_list):
    color = random_bgr_color()
    flag_inside = False
    flag_outside = False

    for i, contour in enumerate(contour_list):
        if hierarchy_list[0][i][3] == -1:
            if flag_inside:
                color = random_bgr_color()
            flag_outside = True
            flag_inside = False
        else:
            if flag_inside:
                color = random_bgr_color()
            else:
                flag_inside = True
                color = random_bgr_color()
        cv2.drawContours(image, [contour], -1, color, 3)

def detect_which_class_is_dot_in(image, label_text_path, class_list, contour_list, hierarchy_list):
    label_data = ViewLabel.get_label_data(label_text_path)
    label_data_list = []
    temp_class_list = classid_list.init_class_id_list(class_list)

    for label in label_data:
        l = []
        class_id, x, y, width, height = label

        image_height, image_width, _ = image.shape
        left = int((x-width/2) * image_width)
        top = int((y-height/2) * image_height)
        right = int((x+width/2) * image_width)
        bottom = int((y+height/2) * image_height)

        if class_id != 21:
            l.extend([class_id, left, top, right, bottom])
            label_data_list.append(l)
        #print("left " + str(left) + ", top " + str(top), ", right " + str(right), ", bottom ", str(bottom))

    classfication_rate = 0.15

    for label in label_data_list:
        for i, (contour, hierarchy) in enumerate(zip(contour_list, hierarchy_list)):
            dot_x = contour[0][0][0]
            dot_y = contour[0][0][1]
            class_id, left, top, right, bottom = label

            if classid_list.is_class_already_detected(class_id, temp_class_list):
                break

            elif (dot_x >= left and dot_x <= right) and (dot_y >= top and dot_y <= bottom):
                temp_class_list = classid_list.class_detected(class_id, temp_class_list)
                    # if len(id_list) == 0 or (len(id_list) >= 1 and class_id != id_list[-1]):
                    #     id_list.append(class_id)

    # for dot in dot_data_list:
    #     for label in dot:
    #         dot_x = dot[0][0]
    #         dot_y = dot[0][1]
    #         class_id, left, top, right, bottom = label
    #         if (dot_x>= left and dot_x<=right) and (dot_y >= top and dot_y <= bottom):
    #             #print(class_id)
    #             if len(id_list) == 0 or (len(id_list) >= 1 and class_id != id_list[-1]):
    #                 id_list.append(class_id)
    return temp_class_list

def random_bgr_color():
    return(random.randint(0, 255), random.randint(0, 255), 255)

def empty_contours(class_list):
    classid_list.init_class_id_list(class_list)