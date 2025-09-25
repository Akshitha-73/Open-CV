import numpy as np 
import cv2
import matplotlib.pyplot as plt 

color_image = cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\img\\lena_color_512.tif',1) # 0 b&w

print(color_image.shape)

cv2.rectangle(color_image,(50,80) , (430,380) , (180,0,0) ,1)

plt.imshow(color_image[:,:,::-1])

plt.show()
