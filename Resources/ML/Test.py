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


def temp(value):
    print("{}\n".format(str(value)*value))


start_time = time.time()

print(torch.__version__)

model_N = YOLO("yolov8n.pt")
model_S = YOLO("yolov8s.pt")
model_L = YOLO("yolov8l.pt")
model_X = YOLO("yolov8x.pt")

# print(type(model_N.names), len(model_N.names), model_N.names)
# # print(type(model_S.names), len(model_S.names), model_S.names)
# # print(type(model_L.names), len(model_L.names), model_L.names)
# # print(type(model_X.names), len(model_X.names), model_X.names)

# results = model_N.predict(source='E:\ML\CV2\Vid_To_IMG\Elevator_Sample\*.jpg', save=True)
end_time = time.time()

execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")