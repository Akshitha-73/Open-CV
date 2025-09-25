import cv2
import numpy as np
import matplotlib.pyplot as plt

img_files = [
    r"C:\Users\akshi\Downloads\opencv_yt\images\hdr_1.1.png",
    r"C:\Users\akshi\Downloads\opencv_yt\images\hdr_1.2.png",
    r"C:\Users\akshi\Downloads\opencv_yt\images\hdr_1.3.png",
    r'C:\Users\akshi\Downloads\opencv_yt\images\hdr_1.4.png'
]
def readimg_times():
    imgs=[img_files[0],img_files[1],img_files[2],img_files[3]]
    times = np.array([1 / 30.0, 0.25, 2.5, 15.0], dtype=np.float32)
    imgg=[]
    for i in img_files:
        im=cv2.imread(i)
        #im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        imgg.append(im)

    return imgg, times

imgg,times=readimg_times()

#creates an object that converts images to median threshold bitmaps
align_mtb = cv2.createAlignMTB()
align_mtb.process(imgg, imgg)  

merge_debevec = cv2.createMergeDebevec()
hdr = merge_debevec.process(imgg,times=times)
cv2.imwrite("hdr_image.png", hdr)

# Tonemap using Drago's method to obtain 24-bit color image
tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
ldrDrago = tonemapDrago.process(hdr)
ldrDrago = 3 * ldrDrago
cv2.imwrite("ldr-Drago.jpg", 255*ldrDrago)
plt.figure(figsize=(20, 10));plt.imshow(np.clip(ldrDrago, 0, 1)[:,:,::-1]);plt.axis("off");
plt.show()

print("Tonemaping using Reinhard's method ... ")
tonemapReinhard = cv2.createTonemapReinhard(1.5, 0, 0, 0)
ldrReinhard = tonemapReinhard.process(hdr)
cv2.imwrite("ldr-Reinhard.jpg", ldrReinhard * 255)
plt.figure(figsize=(20, 10));plt.imshow(np.clip(ldrReinhard, 0, 1)[:,:,::-1]);plt.axis("off")
plt.show()

print("Tonemaping using Mantiuk's method ... ")
tonemapMantiuk = cv2.createTonemapMantiuk(2.2, 0.85, 1.2)
ldrMantiuk = tonemapMantiuk.process(hdr)
ldrMantiuk = 3 * ldrMantiuk
cv2.imwrite("ldr-Mantiuk.jpg", ldrMantiuk * 255)
plt.figure(figsize=(20, 10));plt.imshow(np.clip(ldrMantiuk, 0, 1)[:,:,::-1]);plt.axis("off")
plt.show()