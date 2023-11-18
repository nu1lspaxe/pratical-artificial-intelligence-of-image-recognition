import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('data/digits.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# 切分成5000個子影像(高50x寬100份)，每份20x20像素。
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
# 轉換成 numpy array，尺寸是(50,100,20,20)
x = np.array(cells)
# 左半邊是訓練集，右半邊是測試集
train = x[:,:50].reshape(-1,400).astype(np.float32) # train.shape = (2500,400)
test = x[:,50:100].reshape(-1,400).astype(np.float32) # test.shape = (2500,400)

# 建立跟train和test同數量的數值標記
digit = np.arange(10)
train_labels = np.repeat(digit ,250)[:,np.newaxis] #train_labels序列中，每個digit數值重複250次
test_labels = train_labels.copy() #將train_labels複製到test_labels
# 建立KNN訓練模式
knn = cv.ml.KNearest_create()
knn.train(train, cv.ml.ROW_SAMPLE, train_labels) #ROW_SAMPLE: 每一筆資料都是 row 方向的
ret,result,neighbours,dist = knn.findNearest(test,k=3) #使用訓練好的 KNN，k=5
# 準確度評估
matches = result==test_labels #辨識成功的影像在 matches 標記為1，其它標記為0
correct = np.count_nonzero(matches) #計算 matches 中的非零數值數量
accuracy = correct*100.0/result.size 
print('accuracy= ', accuracy, '%') #計算準確度

p = np.random.randint(2500, size=12) #隨機產生12個[0 2499]間的整數數值

fig = plt.figure() 
for i in range(12):
    fig.add_subplot(3,4,i+1)
    im= np.reshape(test[p[i],:],(20,20)) #將第p[i]個影像資料還原成20x20尺寸
    plt.imshow(im, cmap= 'gray')
    plt.axis("off")
    test_i= int(test_labels[p[i]]) #第p[i]個影像的數值
    result_i= int(result[p[i]]) #第p[i]個影像的KNN估計數值
    if test_i== result_i: #如果答對，顯示黑色
        plt.title('No.'+str(p[i])+': '+str(result_i), fontsize= 16)
    else: #如果答錯，顯示紅色
        plt.title('No.'+str(p[i])+': '+str(result_i)+' (X)', fontsize= 16, color='r')

#全螢幕顯示
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized() 
plt.show() #顯示圖形陣列
