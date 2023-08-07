import os
import sys
import time
import torch
import numpy as np
import requests
import subprocess
import cv2
import tensorrt
import glob
import yaml
from ultralytics import YOLO
from torchvision import transforms
from PIL import Image
from io import BytesIO

os.chdir('..')
os.chdir('yolov8') #Now At yolov8 directory
def execute_train():

    model = YOLO('yolov8x.pt')

    results = model.train(
        data = f'datasets/SAI Elevator.v1i.yolov8.yaml',
        imgsz=640,
        epochs=50,
        batch=8,
        name='CC',
    )

    print(model.names, len(model.names)
)
def execute_test():

    model = YOLO(f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\yolov8\runs\detect\CC2\weights\\best.pt')

    results = model.predict(
w
    )

    # for result in results:
    #     result_plotted = result[0].plot()
    #     cv2.imshow("result",result_plotted)

    print(model.names, len(model.names))

def execute_get_annotation():
    model = YOLO(f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\yolov8\\runs\detect\CC2\weights\\best.pt')
    image_dir = f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Sample\Elevator_Sample'

    annotaion_dir = 'annotations'
    os.makedirs(annotaion_dir, exist_ok=True)

    image_files = glob.glob(os.path.join(image_dir, '*.jpg'))

    for image_file in image_files:
        image_name = os.path.basename(image_file)
        image = cv2.imread(image_file)

        results = model.predict(image, imgsz=640, conf=0.5, save=False)
        for result in results:
            for box in result.boxes:
                # print(box)
                list = box.xywhn.tolist()
                x, y, w, h = list[0][0], list[0][1], list[0][2], list[0][3]
                label_text = f'{int(box.cls.item())} {x} {y} {w} {h}\n'

                annotation_file = f'{image_name}.txt'
                annotation_path = os.path.join(annotaion_dir, annotation_file)
                with open(annotation_path, 'a') as f:
                    f.write(label_text)

        # results2 = model.track(image, show=True)
        # for result in results2:
        #     print(result)
        # for result in results.pandas().xyxy[0]:
        #     class_id = result[5]
        #     xmin, ymin, xmax, ymax = result[:4]
        #
        #     x = (xmin + xmax) / 2
        #     y = (ymin + ymax) / 2
        #     width = xmax - xmin
        #     height = ymax - ymin
        #     label_text = f'{class_id} {x} {y} {width} {height}'
        #
        #     annotation_file = f'{image_name}.txt'
        #     annotation_path = os.path.join(annotaion_dir, annotation_file)
        #     with open(annotation_path, 'w') as f:
        #         f.write(label_text)

if __name__ == '__main__':
    #execute = execute_train()
    #execute = execute_test()
    execute = execute_get_annotation()
