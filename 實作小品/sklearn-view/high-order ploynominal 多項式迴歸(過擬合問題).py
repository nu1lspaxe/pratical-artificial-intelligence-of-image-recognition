# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt

#讀取csv檔的資料，用','分欄，忽略第一列(row)
data = np.genfromtxt("data/Position_Salaries.csv",
                    delimiter=",", skip_header=1) 

x = data[:,1].reshape(-1, 1) #將第一欄「年資」當作x
y = data[:,2].reshape(-1, 1) #將第二欄「薪資」當作y

# Fitting Simple Linear Regression to the Training Set
# 線性迴歸
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# Visualising the Linear Regression results
plt.subplot(2,2,1)
plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg.predict(x), color = 'blue')
plt.title('Trurh or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')

print('score=%.4f' % lin_reg.score(x, y))

# Fitting Ploynomial Regression to the dataset order=2
from sklearn.preprocessing import PolynomialFeatures
poly_reg_2 = PolynomialFeatures(degree = 2)
x_poly_2 = poly_reg_2.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly_2, y)

# Visualising the Polynomal Regression results
plt.subplot(2,2,2)
plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg_2.predict(poly_reg_2.fit_transform(x)), color = 'blue')
plt.title('Truth or Bluff (2nd-order Polynomal Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')

print('score=%.4f' % lin_reg_2.score(x_poly_2, y))

# Fitting Ploynomial Regression to the dataset order=3
poly_reg_3 = PolynomialFeatures(degree = 3)
x_poly_3 = poly_reg_3.fit_transform(x)
lin_reg_3 = LinearRegression()
lin_reg_3.fit(x_poly_3, y)

# Visualising the Polynomal Regression results
plt.subplot(2,2,3)
plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg_3.predict(poly_reg_3.fit_transform(x)), color = 'blue')
plt.title('Truth or Bluff (3rd-order Polynomal Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')

print('score=%.4f' % lin_reg_3.score(x_poly_3, y))

# Fitting Ploynomial Regression to the dataset order=4
poly_reg_4 = PolynomialFeatures(degree = 4)
x_poly_4 = poly_reg_4.fit_transform(x)
lin_reg_4 = LinearRegression()
lin_reg_4.fit(x_poly_4, y)

# Visualising the Polynomal Regression results
plt.subplot(2,2,4)
plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg_2.predict(poly_reg_2.fit_transform(x)), color = 'blue')
plt.title('Truth or Bluff (4th-order Polynomal Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')

print('score=%.4f' % lin_reg_4.score(x_poly_4, y))

# Show results
plt.show()
