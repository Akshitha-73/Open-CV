import numpy as np 
import cv2
import matplotlib.pyplot as plt 

color_image = cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\img\\lena_color_512.tif',1) # 0 b&w

print(color_image.shape)

#cv2.circle(color_image,(250,230) , 150 , (0,0,255),-2)
cv2.circle(color_image,(250,230) , 150 , (0,0,255),2)
plt.imshow(color_image[:,:,::-1])
plt.show()
