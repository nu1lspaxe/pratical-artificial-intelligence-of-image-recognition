from matplotlib import pyplot as plt #匯入 matplotlib.pyplot
#import matplotlib.pyplot as plt #同上一行
import numpy as np

plt.close('all') #關閉所有視窗
x= np.arange(0, 10, 0.1) #橫軸資料
y= x**2 #縱軸資料
plt.plot(x, y, linewidth=4) #繪圖函式,線寬設定
plt.text(1,max(y)*0.7,'y=x**2', fontsize=16)
plt.title('plot(x,y)', fontsize=16) #標題
plt.xlabel('x') #橫軸標題
plt.ylabel('y') #縱軸標題
plt.savefig('data/myfig.png') #儲存figure截圖(含標題)
plt.show() #顯示
