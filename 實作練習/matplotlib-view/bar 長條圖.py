import matplotlib.pyplot as plt #匯入 matplotlib.pyplot
import numpy as np

x = np.array([4, 5, 6, 3, 6, 5, 7, 3, 4, 5])
y = np.array([3, 4, 1, 3, 2, 3, 3, 1, 2, 3])
z = np.array([6, 9, 8, 7, 9, 8, 9, 6, 8, 7])

x_mean = np.mean(x)
y_mean = np.mean(y)
z_mean = np.mean(z)

x_deviation = np.std(x)
y_deviation = np.std(y)
z_deviation = np.std(z)

bars = [x_mean, y_mean, z_mean] #平均值資料
bar_categories = ['X', 'Y', 'Z'] #項目名稱
error_bars = [x_deviation, y_deviation, z_deviation] #誤差線資料

plt.bar(bar_categories, bars, yerr= error_bars) 
# bar 垂直長條圖(項目名稱,長條圖資料,yerr垂直誤差線資料)
plt.show() #顯示

##關閉垂直長條圖後，顯示水平長條圖
plt.figure() #建立新圖
plt.barh(bar_categories, bars, xerr= error_bars, color='m') 
# barh 水平長條圖(項目名稱,長條圖資料,xerr水平誤差線資料)
plt.show() #顯示
