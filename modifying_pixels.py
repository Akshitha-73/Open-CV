import cv2
import matplotlib.pyplot as plt
img=cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\images\LYjY7.png',0)

plt.imshow(img, cmap="gray")
plt.show()
print(img)
print(img[0])

img_c=img.copy()
img_c[:50, :] = 0  # turn first 50 rows black
plt.imshow(img_c, cmap="gray")
plt.show()


