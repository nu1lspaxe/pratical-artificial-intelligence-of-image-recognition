import numpy as np
import cv2

possible_resolutions= np.array([
    [176,144],[352,288],#aspect ratio = 11:9
    [320,240],[400,300],[640,480],[800,600],[960,720],[1024,768],[1280,960],[1440,1080],[1600,1200],#aspect ratio = 4:3
    [400,255],[640,360],[800,450],[960,540],[1024,576],[1280,720],[1440,810],[1600,900],[1920,1080],[3840,2160],#aspect ratio = 16:9
    ])

apiPreference = int(input('API: (1) Any, (2) DirectShow = ? '))
if apiPreference==1:
    cap = cv2.VideoCapture(1)
elif apiPreference==2:
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
else:
    print('error')
resolutions = {}


for i in range(len(possible_resolutions)):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, possible_resolutions[i,0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, possible_resolutions[i,1])
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   
    resolutions[str(width)+"x"+str(height)]='OK'
    print(i)

print(resolutions)