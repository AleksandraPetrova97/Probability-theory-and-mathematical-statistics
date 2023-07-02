# 3.Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170 
# Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175 
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.
import scipy.stats as stats
import numpy as np


a = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
b = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])

x_1 = np.mean(a)
x_2 = np.mean(b)
delta = x_1 - x_2
D_1 = np.var(a,ddof=1)
D_2 = np.var(b,ddof=1)
D = (D_1 + D_2)/2
SE = np.sqrt(D/len(a) + D/len(b))
t = stats.t.ppf(0.975,18)
print(delta - t * SE, delta + t * SE )

# делаем вывод, что принимаем гипотезу Н0, так как интервал проходит через 0