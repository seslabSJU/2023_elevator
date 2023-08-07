import os
import time
import torch
from ultralytics import YOLO
from torchvision import transforms
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import cv2
import tensorrt

os.chdir('..')
os.chdir('tensorRT')

print(torch.__version__)
print(tensorrt.__version__)

model_n = YOLO("yolov8n.pt") #Get YOLOv8 Pre-Trained Dataset
model_n.export(format='engine', device=0, half=True) #Change YOLO dataset into TensroRT Engine File Format

model_s = YOLO("yolov8s.pt") #Get YOLOv8 Pre-Trained Dataset
model_s.export(format='engine', device=0, half=True) #Change YOLO dataset into TensroRT Engine File Format

model_l = YOLO("yolov8l.pt") #Get YOLOv8 Pre-Trained Dataset
model_l.export(format='engine', device=0, half=True) #Change YOLO dataset into TensroRT Engine File Format

model_x = YOLO("yolov8x.pt") #Get YOLOv8 Pre-Trained Dataset
model_x.export(format='engine', device=0, half=True) #Change YOLO dataset into TensroRT Engine File Format

# model_L = YOLO("yolov8l.pt") #Get YOLOv8 Pre-Trained Dataset
# model_L.export(format='engine', device=0, half=True) #Change YOLO dataset into TensroRT Engine File Format