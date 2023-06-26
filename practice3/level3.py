'''作業三：OpenCV瞌睡偵測 Level 3 提示'''
import cv2 # 匯入 openCV 套件
import numpy as np # 匯入 Numpy 套件

# 載入哈爾小波級聯正臉偵測訓練集(用CascadeClassifier())
face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_alt.xml")

# 建立視訊物件並讀取影片檔
cap = cv2.VideoCapture("sleepy.mp4")
# 讀取口罩圖片檔
mask_img = cv2.imread('mask.jpg')

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
#人臉特效選項(預設1，不做特效)
option = 1

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
        
        ###### 偵測正臉 ######
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
                h = int(h*1.2)

            # 如果人臉特效選項為2: 灰階(cvtColor)、文字"Grayscale"(用雙層偏移繪出陰影)
                if option == 2:
                    # 文字顯示
                    cv2.putText(img, "Grayscale", (x-27, y+h+33), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
                    cv2.putText(img, "Grayscale", (x-30, y+h+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
                    # 灰階處理，並放入人臉區域
                    gray = cv2.cvtColor(img[y:y+h, x:x+w, :], cv2.COLOR_BGR2GRAY)
                    img[y:y+h, x:x+w, :] = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            # 如果人臉特效選項為3: 二值化(threshold)、文字"Bilevel"(用雙層偏移繪出陰影)
                elif option == 3:
                    # 文字顯示
                    cv2.putText(img, "Bilevel", (x-7, y+h+33), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
                    cv2.putText(img, "Bilevel", (x-10, y+h+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
                    # 二值化處理並放入人臉區域
                    _, img[y:y+h, x:x+w, :] = cv2.threshold(img[y:y+h, x:x+w, :], 127, 255, cv2.THRESH_BINARY)         
            # 如果人臉特效選項為4: 馬賽克(resize)、文字"Mosaic"(用雙層偏移繪出陰影)
                elif option == 4:
                    # 文字顯示
                    cv2.putText(img, "Mosaic", (x-7, y+h+33), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
                    cv2.putText(img, "Mosaic", (x-10, y+h+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
                    # 馬賽克處理(縮小比率 -> 放大比率 -> 放入人臉區域)
                    ratio = 0.2     
                    small_img = cv2.resize(img[y:y+h, x:x+w, :], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_AREA)
                    resized_img = cv2.resize(small_img, None, fx=1/ratio, fy=1/ratio, interpolation=cv2.INTER_AREA)
                    img[y:y+resized_img.shape[0], x:x+resized_img.shape[1], :] = resized_img
            # 如果人臉特效選項為5: 負片(255-)、文字"Negative"(用雙層偏移繪出陰影)
                elif option == 5:
                    # 文字顯示
                    cv2.putText(img, "Negative", (x-17, y+h+33), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
                    cv2.putText(img, "Negative", (x-20, y+h+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
                    # 將人臉區域做負片處理
                    img[y:y+h, x:x+w, :] = 255 - img[y:y+h, x:x+w, :]
            # 如果人臉特效選項為6: Sobel縱向邊緣檢測、文字"Edges"(用雙層偏移繪出陰影)
                elif option == 6:
                    # 文字顯示
                    cv2.putText(img, "Edges", (x+3, y+h+33), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
                    cv2.putText(img, "Edges", (x, y+h+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
                    # 用Sobel函數做縱向邊緣檢測，並放入人臉區域
                    img[y:y+h, x:x+w, :] = cv2.Sobel(img[y:y+h, x:x+w, :].astype('float32')/255, cv2.CV_64F, 1, 0, ksize=7)
            # 如果人臉特效選項為7: 影像遮罩、文字"Mask"(用雙層偏移繪出陰影)
                elif option == 7:
                    # 文字顯示
                    cv2.putText(img, "Mask", (x+8, y+h+33), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
                    cv2.putText(img, "Mask", (x+5, y+h+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
                    # 「口罩」影像遮罩處理
                    mask_copy = mask_img.copy()     # 用複製圖像，避免頻繁調整失真
                    mask_copy = cv2.resize(mask_copy, (w, h))   # 將大小縮放到人臉區域大小
                    roi_fcae = img[y-5:y+h-5, x:x+w, :]     # 取出人臉感興趣區域(ROI)(roi_face)
                    mask_copy = np.where(mask_copy>2, mask_copy, 0)     # 用np.where()將mask_copy小於2的區域值改為0，其餘保留原本數據
                    roi_fcae = np.where(mask_copy==0, roi_fcae, 0)      # 用np.where()將mask_copy不等於0的區域值改為0，其餘保留原本數據
                    img[y-5:y+h-5, x:x+w, :] = cv2.add(mask_copy, roi_fcae)     # 用cv2.add()將mask_copy貼入roi_face後，放入人臉區域


            #繪製人臉矩形框(用rectangle())
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            #繪製人臉橢圓形框(用ellipse())
                cv2.ellipse(img, (int(x+w/2),int(y+h/2)), (int(w/2), int(h/2)), 0, 0, 360, (0, 255, 255), 2)
            #在人臉矩形框上方放學號文字(用putText())，並用雙層偏移繪出陰影
                cv2.putText(img, "BXXXXXXXX", (x-27, y-7), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
                cv2.putText(img, "BXXXXXXXX", (x-30, y-10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)

  
        #### 判斷是否打瞌睡 #####
        # 如果「有膚色」但「無正臉」，在視窗中顯示"Wake Up!"字樣(最好能閃爍) -> (用雙層偏移繪出陰影)
        if skin == True and face == False:
            cv2.putText(img, "Wake Up!", (23, 123), cv2.FONT_HERSHEY_DUPLEX, 1.7, (0, 0, 0), 2)
            if index % 2 == 0:
                cv2.putText(img, "Wake Up!", (20, 120), cv2.FONT_HERSHEY_DUPLEX, 1.7, (0, 255, 255), 2)
            else:
                cv2.putText(img, "Wake Up!", (20, 120), cv2.FONT_HERSHEY_DUPLEX, 1.7, (255, 0, 0), 2)
        # 如果「無膚色」且「無正臉」，在視窗中顯示"Nobody"字樣，並用雙層偏移繪出陰影
        elif skin == False and face == False:
            cv2.putText(img, "Nobody", (23, 123), cv2.FONT_HERSHEY_DUPLEX, 1.7, (0, 0, 0), 2)
            cv2.putText(img, "Nobody", (20, 120), cv2.FONT_HERSHEY_DUPLEX, 1.7, (0, 0, 255), 2)

        #水平合併膚色遮罩與人臉偵測影像(用np.hstack)，並顯示該畫格(用imshow())
        cv2.imshow("Video", np.hstack((bg, img)))
        # 停每800/fps毫秒讀取鍵盤的按鍵(用waitKey())
        key = cv2.waitKey(round(800/fps)) & 0xFF
        # 當按鍵為ESC(ASCII碼為27)時跳出迴圈
        if key == 27:
            break
        # 如果電腦鍵盤按下1(可用ord('1')轉成相應的ASCII碼)，將人臉區域處理選項設為 1(不做特效)
        elif key == ord('1'):
            option = 1
        # 如果電腦鍵盤按下2，將人臉區域處理選項設為2 (執行特效2)
        elif key == ord('2'):
            option = 2
        # 如果電腦鍵盤按下3，將人臉區域處理選項設為3 (執行特效3)
        elif key == ord('3'):
            option = 3
        # 如果電腦鍵盤按下4，將人臉區域處理選項設為4 (執行特效4)
        elif key == ord('4'):
            option = 4
        # 如果電腦鍵盤按下5，將人臉區域處理選項設為5 (執行特效5)
        elif key == ord('5'):
            option = 5
        # 如果電腦鍵盤按下6，將人臉區域處理選項設為6 (執行特效6)
        elif key == ord('6'):
            option = 6
        # 如果電腦鍵盤按下7，將人臉區域處理選項設為7 (執行特效7)
        elif key == ord('7'):
            option = 7


    # 當沒讀到影片中的畫格時，跳出迴圈
    else:
        break

# 關閉視訊物件
cap.release()
# 關閉視窗
cv2.destroyAllWindows()