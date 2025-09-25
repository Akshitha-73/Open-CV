import cv2
import matplotlib.pyplot as plt

img=cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\images\apollo_11_launch.jpg',0)
img_horz=cv2.flip(img,1)
img_vert=cv2.flip(img,0)
img_both=cv2.flip(img,-1)


plt.figure(figsize=(18, 5))
plt.subplot(141);plt.imshow(img_horz);plt.title("Horizontal Flip")
plt.subplot(142);plt.imshow(img_vert);plt.title("Vertical Flip")
plt.subplot(143);plt.imshow(img_both);plt.title("Both Flipped")
plt.subplot(144);plt.imshow(img);plt.title("Original")
plt.show()
