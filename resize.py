import cv2

import cv2

img_path=r'C:\Users\akshi\Downloads\opencv_yt\images\birds.jpeg'

img=cv2.imread(img_path)
print(img.shape)
img_new=cv2.resize(img,(150,150))

cv2.imshow('new_img',img_new)
print(img_new.shape)

#cv2.imwrite(r'C:\Users\akshi\Downloads\opencv_yt\images\1_write.png',img)

cv2.imshow('img',img)
cv2.waitKey()