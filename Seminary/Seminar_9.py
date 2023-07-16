# # Постройте графики для приведенных наборов данных. Найдите коэффициенты для линии
# # регрессии и коэффициенты детерминации. Что вы замечаете? Нанесите на график модель
# # линейной регрессии.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X1= np.array([30, 30, 40, 40])
Y1= np.array([37, 47, 50, 60])

x2= np.array([30,30,40, 40, 20, 20, 50, 50])
y2= np.array([37, 47, 50, 60, 25, 35, 62, 72])

X3 = np.array([30,30,40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
Y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84]) 

models = [[X1, Y1],[x2,y2],[X3,Y3]]

fig, axis = plt.subplots(3,1)
for i in range(len(models)):
    cor = np.corrcoef(models[i])[0][1]
    axis[i].scatter(models[i][0], models[i][1])
    axis[i].set_title(f'r={round(cor,3)}')

plt.tight_layout()   
# plt.show()

# reshape
for i in range(len(models)):
    models[i][0] = models[i][0].reshape(-1,1)

# regression
for i in  range(len(models)):
    model= LinearRegression()
    model.fit(models[i][0], models[i][1])
    r_sq = model.score(models[i][0], models[i][1])
    print(f'model {i + 1}')
    print(f'R2: {round(r_sq, 3)}')
    print(f'const: {round(model.intercept_, 3)}')
    print(f'beta: {model.coef_}')
    print('-' * 30)

#plot
fig, axis = plt.subplots(3,1)
for i in range(len(models)):
    x = models[i][0]
    y = models[i][1]
    model = LinearRegression()
    model.fit(x, y)
    r_sq = model.score(x, y)
    const = model.intercept_
    beta = model.coef_[0]

    axis[i].scatter(x, y)
    axis[i].set_title(f'R2 = {round(r_sq, 3)}')

    axis[i].plot(x, beta * x + const, 'g')

plt.tight_layout()
plt.show()    

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])

model = LinearRegression()
x = x.reshape(-1, 1)
model.fit(x, y)
r_sq = model.score(x, y)

const = model.intercept_
beta = model.coef_[0]
print(const, beta)

plt.scatter(x, y)
plt.plot(x, beta * x + const, 'g')
plt.title(f'R2 = {round(r_sq, 3)}')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# проверка остатков

y_hat = beta * x + const
y_hat = y_hat.reshape(1, -1)
resid = y - y_hat
print(resid)

plt.figure(figsize=(3,3))
plt.scatter(x,resid)
plt.xlabel('x')
plt.ylabel('residuals')
plt.show()

print(stats.shapiro(resid))

# гомоскедантичность

plt.figure(figsize=(3,3))
plt.scatter(y_hat,resid)
plt.xlabel('y_hat')
plt.ylabel('residuals')
plt.show()

# значимость модели

n = x.shape[0]
m = 1

k1 = m
k2 = n - m - 1

print(k1, k2)

alpha = 0.05

t = stats.f.ppf(1 - alpha, k1, k2)
print(t)

R2 = r_sq
F = (R2 / k1) / ((1 - R2) / k2)
print(F)

import statsmodels.api as sm

x = sm.add_constant(x) # функция добавления константы
model = sm.OLS(y, x) # метод наименьших квадратов
results = model.fit() # обучаем модель
print(results.summary()) # выводим всю суммарную информацию