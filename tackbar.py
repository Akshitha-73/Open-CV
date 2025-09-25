import numpy as np
import cv2

mes_image = cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\img\messi.jpg',1)
mes_hsv = cv2.cvtColor(mes_image,cv2.COLOR_BGR2HSV)
low_val = np.array([110, 50, 50])
high_val = np.array([130, 255, 2500])

mask_image = cv2.inRange(mes_hsv,low_val,high_val)

final_image = cv2.bitwise_and(mes_image,mes_image,mask=mask_image)

cv2.imshow('BGR image',mes_image)
cv2.imshow('HSV Image',mes_hsv)
cv2.imshow('mask_image',mask_image)
cv2.imshow('final_red_color',final_image)

cv2.waitKey()
cv2.destroyAllWindows()



