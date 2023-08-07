import os
import time
import torch
import cv2
import numpy as np
import requests
import xml.etree.ElementTree as ET
import glob
from tqdm import tqdm
from multiprocessing import Pool
from ultralytics import YOLO
from torchvision import transforms
from PIL import Image
from io import BytesIO

os.chdir('..')
ML_Location = os.getcwd()
Dataset_Location = os.path.join(ML_Location, 'Dataset')
Annotation_Location = os.path.join(Dataset_Location, 'annotaions')
Label_Location = os.path.join(Dataset_Location, 'labels')

def xml_to_yolo_bbox(bbox, w, h):
    # [0], [1], [2], [3] = xmin, ymin, xmax, ymax
    x_center = ((bbox[2]+bbox[0])/2) /w
    y_center = ((bbox[3]+bbox[1])/2) /h
    width = (bbox[2]-bbox[0]) /w
    height = (bbox[3]-bbox[1]) /h

    return [x_center,y_center,width,height]

def VOC_to_YOLO(Annotation_Location, Label_Location):
    class_array = []

    files = glob.glob(os.path.join(Annotation_Location, '*.xml'))

    for file_ in tqdm(files):
        basename = os.path.basename(file_)
        filename = os.path.splitext(basename)[0]

        result = []

        tree = ET.parse(file_)
        root = tree.getroot()
        width = int(root.find("size").find("width").text)
        height = int(root.find("size").find("height").text)

        for obj in root.findall('object'):
            label = obj.find("name").text

            if label not in class_array:
                class_array.append(label)
            index = class_array.index(label)
            pil_bbox = [int(x.text) for x in obj.find("bndbox")]
            yolo_bbox = xml_to_yolo_bbox(pil_bbox, width, height)

            bbox_string = " ".join([str(x) for x in yolo_bbox])

            result.append(f"{index} {bbox_string}")
        if result:
            with open(os.path.join(Label_Location, f"{filename}.txt"), "w", encoding="utf-8") as f:
                f.write("\n".join(result))

            print("Write Complete")
        else:
            print("Error Occured")
            return 1
    return 0

# print(Dataset_Location)
# print(Annotation_Location)
# print(Label_Location)
VOC_to_YOLO(Annotation_Location, Label_Location)