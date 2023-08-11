import cv2
import os
import glob
import numpy as np

class Database:

    def __init__(self, sourcePath: str = 'data\\haarcascade_frontalface_default.xml') -> None:
        self.sourcePath = sourcePath    # 資源路徑檔
        self.cascade = cv2.CascadeClassifier(self.sourcePath)  # 建立識別檔案物件



    def takePics(self, total: int) -> None:

        """
        功能: 建立影像樣本資料夾
        參數:
            total(int): 拍攝樣本數量
        回傳: None
        """

        # 若資料夾不存在則建立
        if not os.path.exists("pics"):
            os.mkdir("pics")
        
        name = input("Enter name: ") # 輸入欲建立之資料之名稱
        # 確認是否建立過該人臉資料
        if os.path.exists("pics\\"+name):
            print("此人資料已存在")
        else:
            os.mkdir("pics\\"+name)     # 建立資料夾
            cap = cv2.VideoCapture(0)   # 開啟攝影機
            num = 1     # 執行次數
            
            while (cap.isOpened()):
                ret, img = cap.read()   # 讀取影像
                faces = self.cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(20,20))
                
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)  # 框住人臉
                cv2.imshow("Photo", img)    # 顯示影像
                key = cv2.waitKey(200)

                # 若是影像讀取成功 -> 按下"X"或"x"鍵以拍攝影像
                if ret == True:
                    if key == ord('x') or key == ord('X'):
                        imageCrop = img[y:y+h,x:x+w]    # type: ignore # 裁切
                        imageResize = cv2.resize(imageCrop, (160,160))  # 重製大小
                        faceName = "pics\\" + name + "\\" + name + "_" + str(num) + ".jpg"
                        cv2.imwrite(faceName, imageResize)  # 儲存影像

                        print(f"拍攝第 {num} 次人臉成功")
                        if num == total: break
                        num += 1

            cap.release()   # 關閉攝影機
            cv2.destroyAllWindows()

    

    def buildDB(self) -> None:

        """
        功能: 讀取人臉樣本並放入faces_db，建立標籤與人名串列
        回傳: None
        """

        try:
            nameList = []   # 員工姓名
            faces_db = []   # 儲存所有人臉
            labels = []     # 建立人臉標籤
            index = 0       # 員工編號索引
            
            dirs = os.listdir("pics")
            # 讀取pics資料夾中的每個影像資料夾
            for dir in dirs:
                if os.path.isdir("pics\\"+dir):
                    faces = glob.glob("pics\\"+dir+"\\*.jpg")   # 資料夾中所有影像檔案

                    # 讀取每個影像檔案
                    for face in faces:
                        img = cv2.imread(face, cv2.IMREAD_GRAYSCALE)    # 轉為灰度讀取
                        faces_db.append(img)
                        labels.append(index)

                    nameList.append(dir)
                    index += 1

            # 儲存人名串列，在辨識人臉時使用
            file = open("pics\\people.txt", "w")
            file.write(','.join(nameList))
            file.close()

            print("建立人臉辨識資料庫")
            model = cv2.face.LBPHFaceRecognizer_create()    # 建立LBPH人臉辨識物件
            model.train(faces_db, np.array(labels))     # 訓練LBPH人臉辨識
            model.save("pics\\deepmind.yml")        # 儲存LBPH訓練術具
            print("人臉辨識資料庫完成")

        except Exception as e:
            print(e)


    
    def login(self) -> None:

        """
        功能: 在人臉資料庫中找出最接近的員工標籤，匹配度低於50則算通過; 否則失敗
        回傳: None
        """

        # 建立LBPH人臉辨識物件，並讀取已訓練數據
        model = cv2.face.LBPHFaceRecognizer_create()   
        model.read('pics\\deepmind.yml') 

        # 獲取名稱標籤
        file = open('pics\\people.txt', 'r')
        names = file.readline().split(',')

        cap = cv2.VideoCapture(0)
        while (cap.isOpened()):
            ret, img = cap.read()
            faces = self.cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(20,20))

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)  # 框住人臉

            cv2.imshow("Photo", img)    # 顯示影像
            key = cv2.waitKey(200)

            # 若是影像讀取成功 -> 按下"X"或"x"鍵以拍攝影像
            if ret == True:
                if key == ord('x') or key == ord('X'):
                    imageCrop = img[y:y+h,x:x+w]    # type: ignore # 裁切
                    imageResize = cv2.resize(imageCrop, (160,160))  # 重製大小
                    cv2.imwrite("pics\\face.jpg", imageResize)  # 儲存影像
                    break
        
        cap.release()   # 關閉攝影機
        cv2.destroyAllWindows()

        face = cv2.imread('pics\\face.jpg', cv2.IMREAD_GRAYSCALE)   # 讀取人臉影像
        # 辨識人臉 -> 若是小於50則代表成功
        score = model.predict(face)
        if score[1] < 50:
            print(f"使用者 {names[score[0]]} 成功登入!")
            print(f"匹配值: {score[1]:.2f}")
        else:
            print("登入失敗qq")
            print(f"匹配值: {score[1]:.2f}")

        os.remove("pics\\face.jpg")     # 刪除影像
