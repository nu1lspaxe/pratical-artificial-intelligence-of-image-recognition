'''cv69: MOG Background Reduction 背景減除'''
import cv2
#開啟影片檔案。
cap = cv2.VideoCapture('https://pythonprogramming.net/static/images/opencv/people-walking.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2()
# 以高斯混和模型為基礎的背景/前景分割算法，用於影片背景移除。

while True: # 無窮迴圈，值為真。  # 一直循環擷取，直到手動退出。
    ret, frame = cap.read()# 從攝影機擷取每一張影像。
    # ret → 返回一個布林值，正確為True，表示是否正確讀取影像。
    # frame → 再返回一個值，表示讀取到每一畫格圖像內容。
    fgmask = fgbg.apply(frame) #套用背景分割。
    
    # 顯示影像
    cv2.imshow('original',frame)
    cv2.imshow('fg',fgmask)

    # 鍵盤綁定函數，若在等待間隔30毫秒內按下某鍵，則停止擷取畫面。
    k = cv2.waitKey(30) & 0xff # 與0xFF進行位元運算，取輸入的低八位。
    if k == 27: # 27是ESC鍵的ASCII碼值。
        break # 跳離迴圈。
    

cap.release() # 釋放視訊相機。
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗。