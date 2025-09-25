import numpy as np
import matplotlib.pyplot as plt
import cv2

def values(event,x,y,p,g):
    if event == cv2.EVENT_LBUTTONDOWN:
        b = mes_img[x,y,0]
        g = mes_img[x,y,1]
        r = mes_img[x,y,2]
        t = str(b)+":"+str(g)+":"+str(r)
        cv2.putText(black_image,t,(x,y),2,cv2.FONT_HERSHEY_PLAIN,(0,0,255),2)
        cv2.imshow('b_image', black_image)


black_image = np.zeros((640,640,3))
mes_img = cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\img\messi.jpg',1) # 0 b&w
cv2.imshow('image',mes_img)
cv2.setMouseCallback('image' ,values)
cv2.waitKey()
cv2.destroyAllWindows()