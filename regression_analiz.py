import numpy as np
import pandas as pd
import scipy.stats as stats

s = np.array([27, 37, 42, 48, 57, 56, 77, 80])
p = np.array([1.2, 1.6, 1.8, 1.8, 2.5, 2.6, 3, 3.3])
n = 8
# 1 способ
b1 = (n*np.sum(s*p) - np.sum(s) * np.sum(p)) / (n* np.sum(s**2) - np.sum(s)**2)
# print(b1)

# 2 способ
b1 = (np.mean(s*p) - np.mean(s) * np.mean(p)) / (np.mean(s**2) - np.mean(s)**2)
# print(b1)

b0 = np.mean(p) - b1*np.mean(s)
# print(b0)

y_pred = 0.17147009 + 0.03874585 * s
# print(y_pred)

# функция потерь
mse = ((p - y_pred)**2).sum() / n
# print(mse)

# Матричный метод
x = s.reshape((8,1))
# print(x)
y = p.reshape((8,1))
# print(y)
X = np.hstack([np.ones((8,1)),x])
# print(X)
B = np.dot(np.linalg.inv(np.dot(X.T,X)), X.T @ y)
# print(B)

# Градиентный спуск

def mse_(B1, y = y, x = x, n = 8):
    return np.sum((B1*x - y)**2)/n

alpha = 1e-6

# mse = 1/n * np.su,((B1*x-y)**2)
# mse = (2/n) * np.sum((B1*X-y)*X)

B1 = 0.1

# n = 8

for i in range (10):
    B1 -= alpha * (2/n) * np.sum((B1 * x - y)*x)
    print('B1 = {}'.format(B1))

for i in range(3000):
    B1 -= alpha * (2/n) * np.sum((B1 * x - y)* x)
    if i % 500 == 0:
        print('Iteranion = {i}, B1 = {B1}, mse = {mse}'.format(i = i, B1 = B1, mse = mse_(B1)))

# а теперь посчитаем mse через записанную ранее функцию и убедимся, что они одинаковы

print(mse_(0.041668))

from sklearn.linear_model import LinearRegression

model = LinearRegression() #задаем модель линейной регрессии

#  делаем массив S двумерным атрибутом reshape(-1,1)

s = s.reshape(-1,1)
print(s)

regres = model.fit(s,p) # подбираем коэффициенты
print(regres.intercept_) # выводим интерсепрт
print(regres.coef_) # выводим коэффициент

# Функция predict()

y_pred = model.predict(s) # подставим площадь в модель и посчитаем предиктовые значения цены квартиры
# print(y_pred)

df = pd.DataFrame({'реальные':p, 'предсказанные': y_pred})
# print(df)

#  коэффициент детерминации R2

# print(np.corrcoef(s,p)) #[1,0]
# print(np.corrcoef(s,p)**2)

# или получим из математической модели
print(regres.score(s,p))

# Оценка значимости математической модели. Критерий Фишера
# Установим уровень значимости  α =0,05.

print(stats.f.ppf(1-0.05,1,6))

# критерий Фишера Fр = MSf/ MSo
# Msf (фактическая сумма квадратных отклонений на одну степень свободы)
# Msf = SSf / df1

# остаточная сумма квадратных отклонений на 1 степень свободы
# Mso = SSo / df2

# df1 - степень свободы числителя df1 = p - 1, p - число параметров(у нас площадь и цена, т.е. 2)
# df2 - степень свободы знаменателя df2 = n - p, n - число парных измерений (у нас n = 8)

# SSf - сумма квадратных отклонений фактическая
# SSo - сумма квадратных отклонений остаточная

df1 = 2 - 1
df2 = 8 - 2

SSf = sum((y_pred - np.mean(p))**2)
print(SSf)

SSo = np.sum((p - y_pred)**2)
print(SSo)

Msf = SSf / df1
print(Msf)

Mso = SSo / df2
print(Mso)

F = Msf / Mso
print(F)

# Оценка значимости отдельных коэффициентов. Критерий Стьюдента
# Установим уровень значимости  α =0,05.

print(stats.t.ppf(1-0.025,6))

#  sb и s0 - стандартные ошибки коэффициентов

sb = np.sqrt(Mso / np.sum((s - np.mean(s))**2))
print(sb)

s0 = np.sqrt((Mso * np.sum(s**2)) / (n * sum ((s - np.mean(s))**2)))
print(s0)

t0 = b0 / s0 #критерий Стьюдента для коэффициента b0
print(t0)
tb = b1 / sb #критерий Стьюдента для коэффициента b1
print(tb)

# логистическая регрессия
# Логистическая регрессия применяется, когда 𝑦 является бинарной переменной (0 или 1). 
# Т.е. с помощью этого метода мы можем решить задачу бинарной классификации.

x1 = 120
x2 = 40
x3 = 1

modl = -0.18839 + 0.01115 * x1 - 0.00279 * x2 + 0.16286 * x3
e = 2.71828
sigmoid = 1 / (1+ e**(-modl))
print(sigmoid)

