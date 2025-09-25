import cv2
import numpy as np

path=r'C:\Users\akshi\Downloads\opencv_yt\images\apollo_11_launch.jpg'
img = cv2.imread(path)
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

angle = 55 
scale = 1.0

M = cv2.getRotationMatrix2D(center, angle, scale)
rotated = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
