# Измерены значения IQ выборки студентов, обучающихся в местных технических вузах: 131, 125, 115, 122, 131, 115, 107, 99, 125, 111. 
# Известно, что в генеральной совокупности IQ распределен нормально. 
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np
from scipy import stats


x = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])

M_x = np.mean(x)
sigma = np.std(x,ddof=1)
n = len(x)
print(n, M_x, sigma)

p = 0.95
alpha = 1 - p

t1 = stats.t.ppf(alpha / 2, df = n - 1)
t2 = stats.t.ppf(1 - alpha / 2, df = n - 1)

print(f'Доверительный интервал = {M_x + t1 * sigma / np.sqrt(n) , M_x + t2 * sigma / np.sqrt(n)} ')