import random
import math
import cv2
import numpy as np
import os
import View_Label
import Sort_image

try:
    from config import Config_Detection, Config_Color, Config_Elevator_SW

except Exception as e:
    pass

# def detect_color_from_images(folder_path):
#     img_path = Sort_image.get_images(folder_path)
#
#     for p in img_path:
#         img = cv2.imread(p)
#         detect_color(img)

def detect_color(image_name, label_text_path, class_list):
    os.chdir(Config_Detection.Detection_path['image_folder_path'])
    
    img = cv2.imread(image_name)
    lowest_color_to_detect = np.array(Config_Color.Color_CV2['cv2_inrange_lowest'], dtype="uint8")
    highest_color_to_detect = np.array(Config_Color.Color_CV2['cv2_inrange_highest'], dtype="uint8")

    detected_img = cv2.inRange(img, lowest_color_to_detect, highest_color_to_detect)
    contours, hierarchy = cv2.findContours(detected_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    detected_button_list = []

    if contours:
        contour_list, hierarchy_list = check_contour_points(contours, hierarchy[0])
        draw_heirarchy_Contours(img, contours, hierarchy)
        detected_button_list = detect_which_class_is_dot_in(img, label_text_path, class_list, contour_list, hierarchy_list)

    result = []
    for green_button_elem in detected_button_list:
        value = Config_Elevator_SW.Location_List[green_button_elem]
        if value != 999:
            result.append(value)

    #View_Label.display_label_info(img, label_text_path)
    return result

def check_contour_points(contour_list, hierarchy_list):
    new_hierarchy_list = []
    final_contour = []
    final_hierarchy = []
    total_points = 0

    for i, hierarchy in enumerate(hierarchy_list):
        hierarchy = np.append(hierarchy, i)
        new_hierarchy_list.append(hierarchy)

    np_new_hierarchy_list = np.array(new_hierarchy_list)

    for i, contour in enumerate(contour_list):
        area = cv2.contourArea(contour)
        if area > Config_Detection.Detection_Range['MinCircleArea']:
            final_contour.append(contour)
            final_hierarchy.append(np_new_hierarchy_list[i])
            
            total_points += len(contour)
            #print("Total Dot Count is : {}".format(total_points))

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
    label_data = View_Label.get_label_data(label_text_path)
    label_data_list = []
    green_button_list = []

    for label in label_data:
        l = []
        class_id, x, y, width, height = label

        image_height, image_width, _ = image.shape
        left = int((x-width/2) * image_width)
        top = int((y-height/2) * image_height)
        right = int((x+width/2) * image_width)
        bottom = int((y+height/2) * image_height)

        #print("id : {}, left : {}, top : {}, right : {}, bottom : {}\n".format(class_id, left, top, right, bottom))

        if class_id != 21:
            l.extend([class_id, left, top, right, bottom])
            label_data_list.append(l)
        #print("left " + str(left) + ", top " + str(top), ", right " + str(right), ", bottom ", str(bottom))

    classfication_rate = 0.07

    detect_rate_list = make_detect_rate()
    for i, (contour, hierarchy) in enumerate(zip(contour_list, hierarchy_list)):
        detect_rate_list[1][0] += len(contour)

    for index, each_contour_heir in enumerate(contour_list):
        # print(each_contour_heir)  # Three dimensional array
        for each_dot in each_contour_heir:
            for x, y in each_dot:
                dot_x = x
                dot_y = y

                for label in label_data_list:
                    class_id, left, top, right, bottom = label
                    #print("id is {}, l {}, t {}, r {}, b {}".format(class_id, left, top, right, bottom))

                    if (dot_x >= left and dot_x <= right) and (dot_y >= top and dot_y <= bottom):
                        detect_rate_list[0][class_id] += 1
    #print("Detect rate Lists are {}".format(detect_rate_list))

    for index, elem in enumerate(detect_rate_list[0]):
        #print(detect_rate_list[1][0] * classfication_rate)
        #print(elem)
        #if detect_rate_list[0][-1] != 0 and elem >= math.ceil(detect_rate_list[1][0] * classfication_rate):
        if detect_rate_list[0][-1] != 0 and elem >= 20:
            green_button_list.append(index)
    #print(green_button_list)

    return green_button_list

def make_detect_rate():
    list = []
    detect_list = [0] * 20
    total_dot = [0]

    list.append(detect_list)
    list.append(total_dot)

    return list

def random_bgr_color():
    return(random.randint(0, 255), random.randint(0, 255), 255)

if __name__ == '__main__':
    make_detect_rate()
