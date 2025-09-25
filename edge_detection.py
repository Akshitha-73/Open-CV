import os

import cv2
import numpy as np


img = cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\images\footbal.jpg')
#canny---used for edge detection and reducing noise in the iage
img_edge = cv2.Canny(img, 200, 50)
# low threshold is too high in the Canny edge detection---few only detected
#dilate--grow and thicken object in image
img_edge_d = cv2.dilate(img_edge, np.ones((3, 3), dtype=np.int8))
#erode--thin objects in an image
img_edge_e = cv2.erode(img_edge_d, np.ones((3, 3), dtype=np.int8))

cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)
cv2.waitKey(0)
cv2.destroyAllWindows()