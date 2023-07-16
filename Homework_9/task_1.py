# Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): 
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. 
# Используя математические операции, посчитать коэффициенты линейной регрессии, 
# приняв за X заработную плату (то есть, zp - признак),
# а за y - значения скорингового балла (то есть, ks - целевая переменная).
# Произвести расчет как с использованием intercept, так и без.

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# сначала делаем с интерсепт 

model = LinearRegression()
zp = zp.reshape(-1, 1)
model.fit(zp, ks)
r_sq = model.score(zp, ks)

const = model.intercept_
beta = model.coef_[0]
print(const, beta)

# график с линейной регрессией 
plt.scatter(zp, ks)
plt.plot(zp, beta * zp + const, 'g')
plt.title(f'R2 = {round(r_sq, 3)}')
plt.xlabel('x')
plt.ylabel('y')
# plt.show()

# Матричный метод без интерсепт

x = zp.reshape((10,1))

y = ks.reshape((10,1))

B = np.dot(np.linalg.inv(np.dot(x.T,x)), x.T @ y)
print(B)

plt.scatter(zp, ks)
plt.plot(zp, beta * zp + const, 'g', label=r'$ks=444.18+2.62\cdot zp$')
plt.plot(zp, B * zp , 'r', label=r'$ks=5.89\cdot zp$')
plt.legend()
plt.title(f'R2 = {round(r_sq, 3)}')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

