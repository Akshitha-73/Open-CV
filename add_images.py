import numpy as np
import cv2
import matplotlib.pyplot as plt

lena_image = cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\img\\lena_color_512.tif',1) # 0 b&w
monkey_image = cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\img\\mandril_color.tif',1)


print(f"Lena Image shape : {lena_image.shape}")
print(f"monkey Image shape : {monkey_image.shape}")

combined_image = cv2.add(lena_image,monkey_image,-1) # -1 [take all rows and columns]

combined_image_with_weightage = cv2.addWeighted(lena_image,0.3,monkey_image,0.7,-1)

cv2.imshow('Lena_Lady_Image',lena_image)
cv2.imshow('Monkey_Image',monkey_image)
cv2.imshow('Added image',combined_image)
cv2.imshow('added image with weight',combined_image_with_weightage)
cv2.waitKey()
cv2.destroyAllWindows()


