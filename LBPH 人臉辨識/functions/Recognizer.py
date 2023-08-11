import cv2
import os

class Recognizer:

    def __init__(self, cascadePath: str, deepmind: str) -> None:

        """
        參數:
            cascadePath(str): 影像偵測建置資源檔，此處建議使用'haarcascade_frontalface_alt2.xml'(存於data資料夾下)
            deepmind(str): 人臉辨識訓練數據，預設名稱為'deepmind.yml'(存於facedata資料夾下)
        """
        self.cascadePath = cascadePath
        self.deepmind = deepmind


    def cut(self, picName: str) -> bool:

        """
        功能: 照片截圖，用於人臉辨識

        參數:
            picName(str): 用於辨識的照片檔名

        回傳: 布林值(bool)，代表是否截圖成功
        """

        try:
            # 建立影像辨識物件
            face_cascade = cv2.CascadeClassifier(self.cascadePath)
            img = cv2.imread(picName)
            os.remove(picName)

        except Exception as e:
            print(e)
            return False
        
        else:
            faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
                                                  minNeighbors=3, minSize=(20,20))
            
            # 偵測找到多少人臉 -> 若是>1則回傳截圖失敗(False)，必須=1
            if len(faces) > 1:
                print("照片多於一張人像，必須為個人照")
                return False

            x, y, w, h = faces
            imageCrop = img[y:y+h,x:x+w]
            imageResize = cv2.resize(imageCrop, (160, 160))

            cv2.imwrite('facedata\\loginPic.jpg', imageResize)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        return True
    

    def recognize(self, picName: str) -> bool:
        
        """
        功能: 人臉辨識

        參數:
            picName(str): 用於辨識的檔案，預設檔名為'loginPic.jpg'(存於facedata資料夾下)
            
        回傳: 布林值(bool)，代表是否通過辨識
        """

        try:
            model = cv2.face.LBPHFaceRecognizer_create()
            model.read(self.deepmind)

            # f = open('facedata\\users.txt', 'r')
            # users = f.readline().split(',')

            gray = cv2.imread(picName)
            score = model.predict(gray)
        
        except Exception as e:
            print(e)
            return False
        
        # print(f'用戶名是 {users[score[0]]}')
        print(f'匹配值是 {score[1]:.2f}')
        return score[1] < 50
