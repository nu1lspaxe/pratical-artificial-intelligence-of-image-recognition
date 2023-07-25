'''cv39: 邊緣處理'''
import cv2 

a = 50
img1 = cv2.imread('data/s.jpg')
img1 = cv2.resize(img1,None,fx=0.5,fy=0.5)

cv2.imshow('img',img1)

constant= cv2.copyMakeBorder(img1,a,a,a,a,cv2.BORDER_CONSTANT,value=(0,255,255))
cv2.imshow('constant',constant)

replicate = cv2.copyMakeBorder(img1,a,a,a,a,cv2.BORDER_REPLICATE)
cv2.imshow('replicate',replicate)

reflect = cv2.copyMakeBorder(img1,a,a,a,a,cv2.BORDER_REFLECT)
cv2.imshow('reflect',reflect)

wrap = cv2.copyMakeBorder(img1,a,a,a,a,cv2.BORDER_WRAP)
cv2.imshow('wrap',wrap)

if cv2.waitKey(0) & 0xff == 27: #按ESC離開
    cv2.destroyAllWindows()