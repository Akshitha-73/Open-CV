import numpy as np
import cv2

def fun(x):
    print(x)

cv2.namedWindow("PF")

cv2.createTrackbar("lower_b","PF",0,179,fun)
cv2.createTrackbar("lower_g","PF",0,255,fun)
cv2.createTrackbar("lower_r","PF",0,255,fun)

cv2.createTrackbar("upper_b","PF",179,179,fun)
cv2.createTrackbar("upper_g","PF",255,255,fun)
cv2.createTrackbar("upper_r","PF",255,255,fun)


while(1):
    mes_image = cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\img\messi.jpg',1)
    mes_hsv = cv2.cvtColor(mes_image,cv2.COLOR_BGR2HSV)

    lb = cv2.getTrackbarPos("lower_b","PF")
    lg = cv2.getTrackbarPos("lower_g","PF")
    lr = cv2.getTrackbarPos("lower_r","PF")

    ub = cv2.getTrackbarPos("upper_b","PF")
    ug = cv2.getTrackbarPos("upper_g","PF")
    ur = cv2.getTrackbarPos("upper_r","PF")

    low_values = np.array([lb,lg,lr])
    high_values = np.array([ub,ug,ur])

    mask_image = cv2.inRange(mes_hsv,low_values,high_values)

    final_image = cv2.bitwise_and(mes_image,mes_image,mask = mask_image)


    cv2.imshow("mask", mask_image)
    cv2.imshow("PF", mes_image)
    cv2.imshow("PF", final_image)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()


