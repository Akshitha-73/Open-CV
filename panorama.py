import cv2
import matplotlib.pyplot as plt

path=[
    r'C:\Users\akshi\Downloads\opencv_yt\images\pano_1.png',
    r'C:\Users\akshi\Downloads\opencv_yt\images\pano_2.png',
    r'C:\Users\akshi\Downloads\opencv_yt\images\pano_3.png',
    r'C:\Users\akshi\Downloads\opencv_yt\images\pano_4.png',
    r'C:\Users\akshi\Downloads\opencv_yt\images\pano_5.png',
    r'C:\Users\akshi\Downloads\opencv_yt\images\pano_6.png'
]
imgs = []
for p in path:
    img = cv2.imread(p)
    if img is None:
        print(f"Failed to load")
    else:
        imgs.append(img)

target_height = imgs[0].shape[0]
resized_imgs = [cv2.resize(img, (int(img.shape[1] * target_height / img.shape[0]), target_height))
                for img in imgs]

stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)
status, result = stitcher.stitch(resized_imgs)

if status == cv2.Stitcher_OK:
    cv2.imshow("Panorama", result)
    cv2.waitKey(0)
else:
    print('failed')

cv2.imwrite('final_pano.png',result)