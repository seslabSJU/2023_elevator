import os
from ultralytics import YOLO

# E:\Anaconda\Lib\site-packages\ultralytics
# This is where Anaconda ultralytics(YOLOv8) is installed

# E:\Anaconda\Lib\site-packages\ultralytics\yolo\v8\detect
# This is where YOLOv8 CustomTrained python file exists

os.chdir('..')
os.chdir('yolov8')

model = YOLO("yolov8n.yaml")
model = YOLO("yolov8n.pt")

model = YOLO("yolov8s.yaml")
model = YOLO("yolov8s.pt")

model = YOLO("yolov8l.yaml")
model = YOLO("yolov8l.pt")

model = YOLO("yolov8x.yaml")
model = YOLO("yolov8x.pt")

