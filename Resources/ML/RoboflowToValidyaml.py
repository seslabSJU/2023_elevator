import os
from ultralytics import YOLO
from glob import glob

# E:\Anaconda\Lib\site-packages\ultralytics
# This is where Anaconda ultralytics(YOLOv8) is installed

# E:\Anaconda\Lib\site-packages\ultralytics\yolo\v8\detect
# This is where YOLOv8 CustomTrained python file exists

os.chdir('..')
os.chdir('Roboflow/SAI Elevator.v1i.yolov8')

train_img_list = glob('./train/images/*.jpg') + glob('./train/images/*.jpeg')
valid_img_list = glob('./valid/images/*.jpg') + glob('./valid/images/*.jpeg')

with open('./train.txt', 'w') as f:
    f.write('\n'.join(train_img_list) + '\n')

with open('./valid.txt', 'w') as f:
    f.write('\n'.join(valid_img_list) + '\n')