import numpy as np
import cv2
import matplotlib.pyplot as plt

mes_img = cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\img\messi.jpg',1) # 0 b&w

interested_area = mes_img[515:605 , 350:505]

mes_img[50:140 , 50:205] = interested_area
cv2.imshow('int_area',interested_area)
cv2.waitKey()
cv2.destroyAllWindows()

plt.imshow(mes_img[:,:,::-1])
plt.show()