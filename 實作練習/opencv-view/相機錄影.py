import cv2 # 載入opencv模組

# 建立視訊或相機物件
cap = cv2.VideoCapture(0)  # 參數0：使用系統預設相機。指定相機為1,2,3...

#讀取視訊參數
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv2.CAP_PROP_FPS)
print("影像高,寬: %d x %d" % (height, width))
print("影像幀率(FPS, Frame Per Second): %.2f" % fps)

##選定視訊編碼器
fourcc = cv2.VideoWriter_fourcc(*'X264') # 錄影格式
out = cv2.VideoWriter('data/output.mp4', fourcc, fps, (int(width), int(height))) # 設定錄影物件
##fourcc = cv2.VideoWriter_fourcc(*'XVID') # 錄影格式
##out = cv2.VideoWriter('data/output.avi', fourcc, 20.0, (640,480)) # 設定錄影物件
print('按 "Esc" 離開')

while(cap.isOpened()):
    ret, frame = cap.read() #讀取視訊影像
    if ret == True:
        out.write(frame) # 將畫面寫入錄影物件
        cv2.imshow('frame', frame)
        k = cv2.waitKey(10) & 0xFF
        if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
            break
    else:
        break

cap.release()  # 釋放相機視訊讀取記憶體
out.release()  # 釋放視訊寫入記憶體
cv2.destroyAllWindows()
