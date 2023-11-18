from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt #同上一行
import numpy as np

plt.close('all') #關閉所有視窗
x= np.arange(0, 1000, 20) #橫軸資料0到1000以20為間隔
y1= np.sin(x*(np.pi/180)) #縱軸資料,注意要將角度量轉成徑度量
y2= np.cos(x*(np.pi/180)) #縱軸資料
y3= np.tan(x*(np.pi/180)) #縱軸資料
plt.plot(x, y1,'-s', color='blue') #繪圖,線/標記,顏色
plt.plot(x, y2,'-o', color='r') #繪圖,線/標記,顏色
plt.plot(x, y3,':+', color=[0, 0.5, 0]) #繪圖,線/標記,顏色
'''
線形態(Line Styles): '-'實線, '--'斷線, '-.'點線, ':'虛線
標記(Markers): '.'點, 'o'圓, 'v'倒三角, '^'正三角, 's'方, 'd'菱形, '+'十字, 'x' 叉
顏色(color): 'r'紅, 'g'綠, 'b'藍, 'c'青, 'm'洋紅, 'y'黃, 'k'黑, 'w'白
'''
plt.title('sin/cos/tan', fontsize= 24) #標題,字級
plt.xlabel('x (degree)', fontsize= 18) #橫軸標題,字級
plt.ylabel('y', fontsize= 18) #縱軸標題,字級
plt.xticks(np.arange(0,1000,90)) #橫軸數值以90為間隔
plt.xlim(0, 900)  #橫軸範圍
plt.ylim(-3, 2)  #縱軸範圍

plt.legend(['sin','cos','tan'], loc='lower right') #圖例,位置
plt.text(90, -2.5, 'y= sin(x)\ny= cos(x)\ny= tan(x)', fontsize=16, color='k') #上字
plt.show() #顯示
