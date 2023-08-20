import cv2
import numpy as np

samples = np.loadtxt('../cv2/generalsamples.data', np.float32)
responses = np.loadtxt('../cv2/generalresponses.data', np.float32)
responses = responses.reshape((responses.size, 1))

model = cv2.ml.KNearest_create()
model.train(samples, cv2.ml.ROW_SAMPLE, responses)

img = cv2.imread('../data/test.jpg')
out = np.zeros(img.shape, np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 50:
        [x, y, w, h] = cv2.boundingRect(cnt)
        if h > 28:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi = thresh[y:y + h, x:x + w]
            roismall = cv2.resize(roi, (10, 10))
            roismall = roismall.reshape((1, 100))
            roismall = np.float32(roismall)
            retval, results, neigh_resp, dists = model.findNearest(roismall, k=1)
            string = str(int((results[0][0])))
            cv2.putText(out, string, (x, y + h), 0, 1, (0, 255, 0))

cv2.imshow('im', img)
cv2.imshow('out', out)
cv2.waitKey(0)