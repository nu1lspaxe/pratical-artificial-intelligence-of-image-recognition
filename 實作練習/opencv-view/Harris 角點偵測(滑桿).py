import cv2
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX #字體

def processing(pos):
    k = cv2.getTrackbarPos("Harris","images")*0.002 #k理想值= 0.04
    img = src.copy() #複製影像
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #轉換成灰階影像

    gray = np.float32(gray) #將灰階影像轉換成浮點數格式
    dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=k) #海利斯角點偵測
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7)) #7x7圓形結構元素
    dst = cv2.dilate(dst, kernel) #角點膨脹

    img[dst>0.01*dst.max()]=[0,0,255] #將較明顯的角點(達到角點指標最高值1%以上)顯示為紅色
    cv2.putText(img, "Harris corners k= %.3f"% k, (22, 34), font, 1, 0, 2)
    cv2.putText(img, "Harris corners k= %.3f"% k, (20, 30), font, 1, (0,255,255), 2)
    output = np.hstack((src, img))
    cv2.imshow("images", output)

filename = 'data/building.jpg'
src = cv2.imread(filename) #讀取影像
src = cv2.resize(src, (0,0), fx=0.75, fy=0.75) #影像縮小一倍

cv2.namedWindow("images") #建立視窗
cv2.createTrackbar("Harris","images", 20, 100, processing) #建立滑桿
processing(0)

if cv2.waitKey(0) & 0xff == 27: #按ESC離開
    cv2.destroyAllWindows()
