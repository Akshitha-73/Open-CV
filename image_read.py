import cv2

img_path=r'C:\Users\akshi\Downloads\opencv_yt\images\birds.jpeg'
img=cv2.imread(img_path)

cv2.imwrite(r'C:\Users\akshi\Downloads\opencv_yt\images\1_write.png',img)

cv2.imshow('img',img)
cv2.waitKey()