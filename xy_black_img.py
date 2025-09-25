import numpy as np
import cv2

def mouse(event,x,y,p,g):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        x1=str(x)
        y1=str(y)
        t=x1+" "+y1
        cv2.putText(black_img,t,(x,y),2,cv2.FONT_HERSHEY_PLAIN,[0,255,255],1)
        cv2.imshow('cor_img',black_img)

black_img=np.zeros((640,640,3))
img=cv2.imread(r'C:\Users\akshi\Downloads\opencv_yt\img\messi.jpg',1)
print(img.shape)

cv2.imshow('img',img)
cv2.setMouseCallback('img',mouse)
cv2.waitKey()
cv2.destroyAllWindows()