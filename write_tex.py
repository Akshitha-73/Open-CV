import numpy as np 
import cv2
import matplotlib.pyplot as plt 

color_image = cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\img\\lena_color_512.tif',1) # 0 b&w
print(color_image.shape)

cv2.putText(color_image,"Computer Vision",(80,80),2,cv2.FONT_HERSHEY_PLAIN,(0,255,0),2)

plt.imshow(color_image[:,:,::-1])
plt.show()
