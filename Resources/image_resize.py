import cv2
'''
import Detect_Color

path = f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Real\Vid_No3_2023-06-30-15-03'

images = Detect_Color.get_images(path)
images = Detect_Color.sort_image(images)

for img in images:
    src = cv2.imread(img)
    #cv2.imshow('origin', src)

    height, width = src.shape[:2]

    dst = cv2.resize(src, (int(width*0.5), int(height*0.5)), interpolation=cv2.INTER_AREA)
    # cv2.imshow('result', dst)
    # key = cv2.waitKey(0)
    
    cv2.imwrite(img, dst)
'''

def resize(image_path):
    src = cv2.imread(image_path)
    #cv2.imshow('origin', src)

    height, width = src.shape[:2]

    dst = cv2.resize(src, (int(width*0.5), int(height*0.5)), interpolation=cv2.INTER_AREA)
    # cv2.imshow('result', dst)
    # key = cv2.waitKey(0)
    cv2.imwrite(image_path, dst)
