import cv2
path=r'C:\Users\akshi\Downloads\opencv_yt\images\apollo_11_launch.jpg'
img = cv2.imread(path)

rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotated_180 = cv2.rotate(img, cv2.ROTATE_180)
rotated_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Rotated", rotated_90)
cv2.imshow('180',rotated_180)
cv2.imshow('270',rotated_270)
cv2.waitKey(0)
