'''cv24: 繪製 gamma 階調調整曲線'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

def gamma_curve(gamma): ## 產生 gamma 曲線對照表
    gamma_LUT=np.arange(256).astype("float32")
    #gamma_LUT=np.arange(256) #請比較用 int 的差別
    for i in range(0,256):  #根據 gamma 值 產生調整後的 8bit 灰階值
        gamma_LUT[i]=255*(i/255)**gamma
    return gamma_LUT

## 繪製 gamma 值不同的曲線(不同粗細的黑線)
for x in np.arange(-0.4, 0.5, 0.2): 
    gamma = 1/(10**x) #換算成 gamma 值
    plt.plot(gamma_curve(gamma), 'k-', linewidth= 2.5 -2*x, \
            label='gamma = '+str(round(gamma, 1)))
    
fontSize = 'x-large'
## size options: xx-small, x-small, small, medium, large, x-large, xx-large, larger, or smaller
plt.title('Gamma curves', fontsize= fontSize) #標題內容,格式
plt.xlabel('input', fontsize= fontSize) #橫軸標題內容,格式
plt.ylabel('output', fontsize= fontSize) #,縱軸標題內容,格式
legend = plt.legend(loc='lower right', shadow=True, fontsize= fontSize) #圖例格式
plt.show() #顯示圖表

## 繪製 gamma 值不同的曲線(同粗細的彩色線)
for x in np.arange(-0.4, 0.5, 0.2): 
    gamma = 1/(10**x) #換算成 gamma 值
    plt.plot(gamma_curve(gamma), linewidth= 2, \
            label='gamma = '+str(round(gamma, 1)))
    
plt.title('Gamma curves', fontsize= fontSize) #標題內容,格式
plt.xlabel('input', fontsize= fontSize) #橫軸標題內容,格式
plt.ylabel('output', fontsize= fontSize) #,縱軸標題內容,格式
legend = plt.legend(loc='lower right', shadow=True, fontsize= fontSize) #圖例格式
plt.show()  #顯示圖表


