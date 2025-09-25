import cv2


vi=r'C:\Users\akshi\Downloads\opencv_yt\58760-489663268_small.mp4'

vid=cv2.VideoCapture(vi)

c=0
while True:
    ret, pixel =vid.read()

    if ret==True:
        
        cv2.putText(pixel,f'frame: {c}',(125,125),2,cv2.FONT_HERSHEY_PLAIN,([0,255,255]),1)
        cv2.imshow('frame',pixel)
        cv2.imwrite(r'C:\Users\akshi\Downloads\opencv_yt\images\utput\cy'+str(c)+'.png',pixel)
        c+=1
        
        print('ok')
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

    
vid.release()
cv2.destroyAllWindows


