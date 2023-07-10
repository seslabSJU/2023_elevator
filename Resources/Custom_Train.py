import os
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

    model = YOLO(f'E:\ML\Elevator Git\Effective_Elavator_Algorithm_For_SejongAICenter\yolov8\\runs\detect\CC2\weights\\best.pt')

    results = model.predict(
        source = f'E:\ML\Elevator Git\Effective_Elavator_Algorithm_For_SejongAICenter\Images_Sample\Elevator_Sample',
        imgsz=640,
        conf=0.5,
        save=True
    )

    # for result in results:
    #     result_plotted = result[0].plot()
    #     cv2.imshow("result",result_plotted)

    print(model.names, len(model.names))



if __name__ == '__main__':
    #execute = execute_train()
    execute = execute_test()
