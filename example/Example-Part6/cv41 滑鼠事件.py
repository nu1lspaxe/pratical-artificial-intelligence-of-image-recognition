'''cv41: 滑鼠事件'''
import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print( events ) # 列出所有滑鼠事件參數

# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP: # 如果滑鼠左鍵彈起
        cv2.circle(img, (x,y), 10, (0,255,255), -1) # 在游標位置繪製黃色圓形

print('click left button')
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle) # 建立滑鼠反應函式
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
