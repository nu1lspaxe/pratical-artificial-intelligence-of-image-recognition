import cv2 # 載入opencv套件

# 建立視訊或相機物件
cap = cv2.VideoCapture(0) # 參數0：使用系統預設相機。指定相機為1,2,3...

if cap.isOpened() is False: # 若沒讀到相機，跳出程式
    print("找不到相機")
    exit()

while (1):  # 用無窮迴圈讀取影片中每個畫格(幀)   
    ret, frame = cap.read() # 讀取影片中的畫格
    if ret == True: # 若有讀取到影片中的畫格
        cv2.imshow("Video", frame) #顯示該畫格
        # 停每25毫秒讀取鍵盤的按鍵
        key = cv2.waitKey(25) & 0xFF
        if key == 27: #當按鍵為ESC(ASCII碼為27)時跳出迴圈
            break   
    else: # 當沒讀到影片中的Frame時，跳出迴圈
        break

cap.release() # 釋放記憶體
cv2.destroyAllWindows()
