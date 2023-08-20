import os
import re
import math
import glob
import pytesseract
import cv2
import matplotlib.pyplot as plt

# path2 = f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Real\Vid_No3_2023-06-30-15-03\\frame_20550.jpg'
# crop_folder_path = f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Sample\Crop_Images'
# def get_files_from_folder(folder_path, extension_name):
#     absolute_paths = []
#
#     if not os.path.exists(folder_path):
#         print(f"Error: Folder path '{folder_path}' does not exist.")
#         return absolute_paths
#
#     pattern = os.path.join(folder_path, f"*.{extension_name}")
#     mathched_files = glob.glob(pattern)
#
#     for file in mathched_files:
#         absolute_path = os.path.abspath(file)
#         absolute_paths.append(absolute_path)
#
#     return sorted(mathched_files)
#
# def cv2_matchTemplate(image_path, template_image_path):
#     img = cv2.imread(image_path)
#     gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#     crop_img = cv2.imread(template_image_path, cv2.IMREAD_GRAYSCALE)
#     w, h = crop_img.shape[::-1]
#
#     result = cv2.matchTemplate(gray_img, crop_img, cv2.TM_CCORR_NORMED)
#     minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
#
#     start_x, start_y = maxLoc
#     end_x, end_y = start_x+w, start_y+h
#
#     img = cv2.rectangle(img, (start_x,start_y), (end_x,end_y), (0,0,255), 1)
#     cv2.imshow('sample', img)
#     key = cv2.waitKey(0)
#
#
#
# list = get_files_from_folder(crop_folder_path,extension_jpg)
#
# for temp_path in list:
#     print(temp_path)
#     cv2_matchTemplate(path, temp_path)

def get_images(path):
    formats = ['.jpg']
    path_list = []

    for root, dir, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_path = file_path.replace('\\','/')
            path_list.append(file_path)

    return path_list

def extract_frame_number(path):
    match = re.search(r'(\d+)\.jpg', path)
    if match:
        return int(match.group(1))
    return -1

def sort_image(images):
    sorted_img = sorted(images, key=extract_frame_number)
    return sorted_img

def OCR_Test(img):
    min_t = 200
    max_t = 255

    #img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(gray, min_t, max_t)
    thresh = cv2.adaptiveThreshold(canny, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 3)
    inverted_thresh = ~thresh

    contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)
    final_contours = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 20.0:
            (x,y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)

            cv2.circle(img, center, radius, (0, 255, 0), 3)
            #print(radius)
            arcLength = cv2.arcLength(contour, True)
            circle_area = radius * radius * math.pi

            print("Circle Area : {}, Contour Area : {}".format(circle_area, area))
            final_contours.append(contour)

    for i in range(len(final_contours)):
        img = cv2.drawContours(img, final_contours, i, (255, 0, 0), 4)

    cv2.imshow('S', img)
    cv2.imshow('C', canny)
    key = cv2.waitKey(0)

path = f'/Elevator Git/Effective-Elevator-Energy-Calculation-for-SejongAI-Center/Images_Sample/sample.jpg'
path2 = f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Sample\Elevator_Sample'
path3 = f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Real\Vid_No2_2023-06-30-15-12'
extension_jpg = 'jpg'

list = get_images(path3)
list = sort_image(list)

for i in list:
    img = cv2.imread(i)
    OCR_Test(img)