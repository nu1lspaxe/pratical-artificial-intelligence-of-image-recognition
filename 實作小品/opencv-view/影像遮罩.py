import cv2 
import numpy as np

#read the input image
img = cv2.imread('data/ntust.jpg')
#show the original image
cv2.imshow('img',img)
#create mask
mask = np.zeros(img.shape[:2], dtype = "uint8")
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2) #center x,y
cv2.circle(mask, (cX, cY), 200, 255, -1)
#apply mask
masked = cv2.bitwise_and(img, img, mask = mask)
#Show masked image
cv2.imshow('masked',masked)

if cv2.waitKey(0) & 0xff == 27: #按ESC離開
    cv2.destroyAllWindows()