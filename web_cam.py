import cv2

vid=cv2.VideoCapture(0)

c=0
while True:
    res,pix=vid.read()

    if res==True:
        
        cv2.putText(pix,f'frame: {c}',(125,125),2,cv2.FONT_HERSHEY_PLAIN,([0,255,255]),1)
        cv2.imshow('frame',pix)
        cv2.imwrite(r'C:\Users\akshi\Downloads\opencv_yt\images\utput\yuy'+str(c)+'.png',pix)
        c+=1
        
        print('ok')
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

    
vid.release()
cv2.destroyAllWindows