import cv2
import os
import glob
import numpy as np

class BuildDB:

    def __init__(self) -> None:

        # 初始化名稱列表、圖像陣列、標籤陣列、標籤索引值
        self.nameList = []
        self.facesDB = []
        self.labels = []
        self.index = 0


    def lebel(self, dirName: str) -> bool:
        
        """
        功能: 建立影像檔案標籤

        參數:
            dirName(str): 影像資料夾名稱

        回傳: 布林值(bool)，代表是否建立成功
        """

        try:
            if not os.path.exists("facedata\\" + dirName):
                print("查無該影像資料夾")
                return False
            if dirName in self.nameList:
                print("已標籤過影像檔案")
                return False
            
            faces = glob.glob("facedata\\" + dirName + "\\*.jpg")
            for face in faces:
                img = cv2.imread(face, cv2.IMREAD_GRAYSCALE)
                self.facesDB.append(img)
                self.labels.append(self.index)
            self.nameList.append(dirName)
            self.index += 1
        
        except Exception as e:
            print(e)
            return False
        
        else:
            f = open('facedata\\users.txt', 'w')
            f.write(','.join(self.nameList))
            f.close()
        
        return True
    

    def build(self) -> bool:

        """
        功能: 使用建立好標籤的資料，建置資料庫
        """

        try:
            print("建立人臉辨識資料庫...")
            model = cv2.face.LBPHFaceRecognizer_create()
            model.train(self.facesDB, np.array(self.labels))
            model.save('facedata\\deepmind.yml')
            print("人臉辨識資料庫建置完成")

        except Exception as e:
            print(e)
            return False

        return True