import cv2
import matplotlib.pyplot as plt
from IPython.display import YouTubeVideo, display, HTML
import webbrowser

source = r'C:\Users\akshi\Downloads\opencv_yt\58760-489663268_small.mp4'  # source = 0 for webcam
cap = cv2.VideoCapture(source)
if not cap.isOpened():
    print('error opening video stream or file')

ret, frame = cap.read()
if ret:
    pass
    plt.imshow(frame[:,:,::-1])
    plt.show()
else:
    print('no frame captured')

video_id = "IGsrOGhyzlI"
url = f"https://www.youtube.com/watch?v={video_id}"
webbrowser.open(url)



