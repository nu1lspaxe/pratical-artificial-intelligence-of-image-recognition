import cv2

# 載入人臉偵測訓練集、建立偵測物件
face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_alt.xml")

# 建立攝影機物件
cap = cv2.VideoCapture("sleepy.mp4")
#視訊幀率
fps = cap.get(cv2.CAP_PROP_FPS) 

# 建立face_counter參數，計算連續幀數
face_counter = 0

# 用無窮迴圈讀取影片中每個畫格(幀)
while True:
    # 讀取影像
    ret, img = cap.read()

    # 當有讀取到影像則執行
    if ret == True:

        # 用cvtColor轉換GRAY後，啟動偵測物件
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # 讀取人臉範圍
        for (x, y, w, h) in faces:
            # 繪製人臉矩形框
            cv2.rectangle(img, (x,y), (x+w,int(y+h*1.2)), (255,0,0), 2)
            # 加上學號且用雙層偏移顯示陰影
            cv2.putText(img, "BXXXXXXXX", (x-27, y-7), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
            cv2.putText(img, "BXXXXXXXX", (x-30, y-10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
        
        # 是否辨識到正臉，若辨識不到(len(faces)==0)則在畫面印出Wake Up!
        # 指派face_counter數量，計算連續九幀畫面
        if len(faces) == 0:
            if face_counter == 10:
                face_counter -= 1
        else:
            face_counter = 10

        # 連續九幀顯示 Wake Up 字樣
        if face_counter > 0 and face_counter < 10:
            # 使用雙層偏移顯示陰影
            cv2.putText(img, "Wake Up!", (23, 123), cv2.FONT_HERSHEY_DUPLEX, 1.7, (0, 0, 0), 2)
            cv2.putText(img, "Wake Up!", (20, 120), cv2.FONT_HERSHEY_DUPLEX, 1.7, (0, 255, 255), 2)
            print(face_counter)     # 印出剩餘幀數
            face_counter -= 1

        # 顯示影像
        cv2.imshow("Video", img)

        # 停每800/fps毫秒讀取鍵盤的按鍵，若按Esc(ASCII=27)則退出
        key = cv2.waitKey(round(800/fps)) & 0xFF
        if key == 27:
            break
    else:
        break

# 關閉視訊物件
cap.release()
# 關閉視窗
cv2.destroyAllWindows()
