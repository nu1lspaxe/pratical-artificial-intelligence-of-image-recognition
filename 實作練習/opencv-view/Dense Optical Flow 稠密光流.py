import numpy as np
import cv2 as cv
cap = cv.VideoCapture(1) #開啟相機視訊物件
ret, frame1 = cap.read() # 讀取初始視訊影像
prvs = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY) #影像轉換至灰階格式
hsv = np.zeros_like(frame1) #建立初始 hsv 格式影像
hsv[..., 1] = 255 #將飽和度(saturation)設為最大值

while(1): #視訊迴圈
    ret, frame2 = cap.read()  # 讀取視訊影像
    if not ret:
        print('沒有讀到影像!')
        break
    next = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)   #影像轉換至灰階格式
    flow = cv.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    #將光流從(x,y)座標系轉換成極座標系: 強度 mag，角度 ang
    mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1]) 
    hsv[..., 0] = ang*180/np.pi/2 #將角度換算為[0 180]度範圍的色相
    hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)  #將強度換算為[0 255]範圍的明度
    bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR) #將 hsv 格式影像轉換回 BGR 格式
    cv.imshow('frame2', bgr) #顯示處理後的稠密光流影像，顏色代表物件運動方向，亮度代表運動速度
    k = cv.waitKey(30) & 0xff #要給電腦30微秒時間處理
    if k == 27: #按Esc離開
        break
    elif k == ord('s'): #按's'鍵儲存當下的影像與稠密光流
        cv.imwrite('data/DOF_frame.png', frame2)
        cv.imwrite('data/DOF_flow.png', bgr)
    prvs = next #更新上一幀
    
cv.destroyAllWindows()