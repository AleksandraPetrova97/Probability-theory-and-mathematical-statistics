import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# x = np.array([10,8, 13, 9,11,14, 6,4,12, 7,5])
# y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68 ])

# x= np.array([ 10,8, 13, 9,11,14, 6,4,12, 7,5 ])
# y2 = np.array([ 9.14, 8.14, 8.74,8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])

# x= np.array([ 10,8, 13, 9,11,14, 6,4,12, 7,5 ])
# y3 = np.array([7.46,6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])

# x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
# y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25,12.5, 5.56, 7.91, 6.89])

# x0= np.array([ 10, 8, 13, 9, 11, 14, 6, 4, 12, 7,5, 15, 16, 18 ])
# y0 = np.array([ 9.14, 8.14, 8.74,8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74, 6.5, 5, 2.9])

# print(np.corrcoef(x,y))
# print(np.corrcoef(x,y2))
# print(np.corrcoef(x,y3))
# print(np.corrcoef(x4,y4))
# print(np.corrcoef(x0,y0))

# plt.scatter(x,y)
# plt.show

# Провести двусторонний тест и ответить на вопрос, есть ли статистически значимые
# различия между средними 2х нормально распределенных генеральных совокупностей,
# представленных следующими независимыми выборками:

a = np.array([12, 10, 11, 19, 13, 11, 17, 15, 19, 14, 21, 18, 21, 11, 17, 14, 15, 17, 20, 19])
b = np.array([11, 13, 18, 15, 17, 18, 10, 21, 26, 15, 11, 12, 15, 17, 10, 18, 18, 12,21, 20])

# Уровень статистической значимости принять за 5%
# 1. Используйте функцию в Python:
# 2. Имея p-value из функции рассчитать наблюдаемое значение критерия.

print(stats.ttest_ind(a,b))
# print(np.corrcoef(a,b))

# print(stats.ttest_ind(a, b,alternative='greater', equal_var = True))

print(stats.t.ppf(0.975,19))
print(stats.t.ppf(1-0.8737549039369696/2,38))

# Некоторое изделие выпускается 2мя заводами. При этом объем продукции 2го завода в 3 раза
# превосходит объем продукции 1го. Доля брака у 1го -2%, у 2го -1%. Изделие выпущено
# заводами за одинаковый промежуток времени. Изделия перемешали и отправили в продажу.
# Какова вероятность, что приобретенное изделие со 2го завода, если оно бракованное

P_A = (1/4 * 0.02) + (3/4 * 0.01)
P_B = 3/4
P_AB = 0.01

print((P_AB * P_B)/P_A)