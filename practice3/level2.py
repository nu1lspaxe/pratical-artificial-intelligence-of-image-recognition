'''作業三：OpenCV瞌睡偵測 Level 2 提示'''
import cv2 # 匯入 openCV 套件
import numpy as np # 匯入 Numpy 套件

# 載入哈爾小波級聯正臉偵測訓練集(用CascadeClassifier())
face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_alt.xml")

# 建立視訊物件並讀取影片檔
cap = cv2.VideoCapture("sleepy.mp4")

## 讀取視訊參數 ##
#視訊畫面高(用.get)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#視訊畫面寬(用.get)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#視訊幀率(用.get)
fps = cap.get(cv2.CAP_PROP_FPS)
#視訊總幀數(用.get)
total_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

#畫面編號(預設0)
index = 0

# 用無窮迴圈讀取影片中每個畫格(幀)
while True:
    # 讀取影片中的畫格(用.read())
    ret, img = cap.read()
    # 若有讀取到影片中的畫格
    if ret == True:
        # 畫面數量加 1
        index += 1

        ###### 偵測膚色 #######
        # ROI是高寬25%:75%範圍
        # roi = cv2.resize(img, (0,0), fx=0.75, fy=0.75)
        top, bottom = round(img.shape[0]*0.25), round(img.shape[0]*0.75)
        left, right = round(img.shape[1]*0.25), round(img.shape[1]*0.75)
        roi = img[top:bottom, left:right, :]
        # 將ROI從 BGR 轉換至 HSV 色空間(用 cvtColor())
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        # 定義 HSV (hue, saturation, value) 空間的膚色上下界範圍(下界約 (0,50,50), 上界約 (80,180,220))
        lower_skin = np.array([0,50,50])
        upper_skin = np.array([80,180,220])     # 註：HSV的範圍上限 [180, 256, 256]
        # 取HSV色空間下，ROI範圍內的膚色遮罩(用inRange())
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        # 算出膚色面積率，也就膚色遮罩非零數值佔遮罩面積的比率(用np.count_nonzero()，可用mask[:]忽略維度，用round(,精度)四捨五入)
        skin_area_ratio = round(np.count_nonzero(mask[:]) / (mask.shape[0] * mask.shape[1]), 3)
        # 如果膚色面積率高於0.07，代表「有膚色」，否則代表「無膚色」
        if skin_area_ratio > 0.07:
            skin = True
        else:
            skin = False
        # 將膚色遮罩轉換為彩色格式(用cvtColor)
        mask_color = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        # 在遮罩上加面積率數值(用putText())
        cv2.putText(mask_color, f"area= {skin_area_ratio}", (20, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 165, 255), 2)
        # 建立跟輸入影像一樣大，一樣格式的背景影像(用np.zeros())
        bg = np.zeros(img.shape, img.dtype)
        # 將背景影像設成灰色
        bg[:] = 80
        # 把膚色遮罩貼入背景影像
        bg[int(bg.shape[0]*0.25):int(bg.shape[0]*0.75), int(bg.shape[1]*0.25):int(bg.shape[1]*0.75), :] = mask_color

        
        ###### 偵測人臉 ######
        # 影像轉成灰階格式(用cvtColor())
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 偵測正臉(用.detectMultiScale())
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        # 如果正臉數量(可用len(faces))為零，代表「無正臉」
        if len(faces) == 0:
            face = False
        # 否則「有正臉」
        else:
            face = True
            #增加矩形框的高度
            for (x, y, w, h) in faces:
            #繪製人臉矩形框(用rectangle())
                cv2.rectangle(img, (x,y), (x+w,int(y+h*1.2)), (255,0,0), 2)
            #在人臉矩形框上方放學號文字(用putText())，用雙層偏移繪出陰影
                cv2.putText(img, "BXXXXXXXX", (x-27, y-7), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
                cv2.putText(img, "BXXXXXXXX", (x-30, y-10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
        
        #### 判斷是否打瞌睡 #####
        # 如果「有膚色」但「無正臉」，在視窗中顯示"Wake Up!"字樣(最好能閃爍) -> (用雙層偏移繪出陰影)
        if skin == True and face == False :
            cv2.putText(img, "Wake Up!", (23, 123), cv2.FONT_HERSHEY_DUPLEX, 1.7, (0, 0, 0), 2)
            if index % 2 == 0:
                cv2.putText(img, "Wake Up!", (20, 120), cv2.FONT_HERSHEY_DUPLEX, 1.7, (0, 255, 255), 2)
            else:
                cv2.putText(img, "Wake Up!", (20, 120), cv2.FONT_HERSHEY_DUPLEX, 1.7, (255, 0, 0), 2)
        # 如果「無膚色」且「無正臉」，在視窗中顯示"Nobody"字樣(用雙層偏移繪出陰影)
        elif skin == False and face == False:
            cv2.putText(img, "Nobody", (23, 123), cv2.FONT_HERSHEY_DUPLEX, 1.7, (0, 0, 0), 2)
            cv2.putText(img, "Nobody", (20, 120), cv2.FONT_HERSHEY_DUPLEX, 1.7, (0, 0, 255), 2)

        #水平合併膚色遮罩與人臉偵測影像(用np.hstack)，並顯示該畫格(用imshow())
        cv2.imshow("Video", np.hstack((bg, img)))
        # 停每800/fps毫秒讀取鍵盤的按鍵(用waitKey())
        key = cv2.waitKey(round(800/fps)) & 0xFF
        #當按鍵為ESC(ASCII碼為27)時跳出迴圈
        if key == 27:
            break
        
    # 當沒讀到影片中的畫格時，跳出迴圈
    else:
        break

# 關閉視訊物件
cap.release()
# 關閉視窗
cv2.destroyAllWindows()