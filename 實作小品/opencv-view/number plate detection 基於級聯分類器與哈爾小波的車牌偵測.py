import cv2
import numpy as np

#讀入兩幅影像
nPlateCascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_russian_plate_number.xml')
img = cv2.imread('data/plates1.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 5)
print(numberPlates)

minArea =100
color = (255,0,255)

n=0
for (x,y,w,h) in numberPlates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    area = w*h
    if area > minArea:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        cv2.putText(img,"Number Plate",(x,y-5),
        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
        imgRoi = img[y:y+h,x:x+w]
        n+=1
        str1='ROI '+str(n)
        cv2.namedWindow(str1)
        cv2.imshow(str1, imgRoi)

cv2.namedWindow('input') 
cv2.imshow('input',img)
cv2.waitKey()
cv2.destroyAllWindows()