
import numpy as np 
import cv2
import matplotlib.pyplot as plt 

f = cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\img\\lena_color_512.tif',1) # 0 b&w
print(f.shape)

cv2.imshow('Complete_Image',f)
cv2.imshow('B_channel',f[:,:,0])
cv2.imshow('G_channel',f[:,:,1])
cv2.imshow('R_channel',f[:,:,2])

cv2.waitKey()
cv2.destroyAllWindows()