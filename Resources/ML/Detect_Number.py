import cv2
import math

import sys
import cv2
import numpy as np

path = f'/Elevator Git/Effective-Elevator-Energy-Calculation-for-SejongAI-Center/Images_Sample/Elevator_Sample/frame_510.jpg'
img = cv2.imread(path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
samples = np.empty((0, 100), np.float32)
responses = []
keys = [i for i in range(48, 58)]

for cnt in contours:
    if cv2.contourArea(cnt) > 100:
        [x, y, w, h] = cv2.boundingRect(cnt)

        if h > 49:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2) #Red Color
            roi = thresh[y:y + h, x:x + w]
            roismall = cv2.resize(roi, (10, 10))

            cv2.imshow('norm', img)
            key = cv2.waitKey(0)

            if key == 27:  # (escape to quit)
                sys.exit()

            elif key in keys:
                responses.append(int(chr(key)))
                print(sample)
                sample = roismall.reshape((1, 100))
                samples = np.append(samples, sample, 0)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2) #Blue Color

responses = np.array(responses, np.float32)
responses = responses.reshape((responses.size, 1))

samples = np.float32(samples)
responses = np.float32(responses)

cv2.imwrite("../cv2/train_result.jpg", img)
np.savetxt('../cv2/generalsamples.data', samples)
np.savetxt('../cv2/generalresponses.data', responses)

# cv2.imshow('img', img)
# cv2.imshow('gray',gray)
# cv2.imshow('blur',blur)
#cv2.imshow('thresh',thresh)

cv2.destroyAllWindows()