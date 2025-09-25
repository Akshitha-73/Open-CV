import numpy as np
import matplotlib.pyplot as plt
import cv2

mes_img = cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\img\\\\messi.jpg',1) # 0 b&w
hsv_image = cv2.cvtColor(mes_img,cv2.COLOR_BGR2HSV) # changing bgr to hsv

cv2.imshow('BGR image',mes_img)
cv2.imshow('HSV Image',hsv_image)
cv2.waitKey()
cv2.destroyAllWindows()


