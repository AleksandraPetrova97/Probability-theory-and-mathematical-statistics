# Измерены значения IQ выборки студентов, обучающихся в местных технических вузах: 131, 125, 115, 122, 131, 115, 107, 99, 125, 111. 
# Известно, что в генеральной совокупности IQ распределен нормально. 
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np
from scipy import stats


x = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])

M_x = np.mean(x)
sigma = np.std(x,ddof=1)
n = len(x)
t = stats.t.ppf(0.95, 9)

print(f'Доверительный интервал = {M_x - t * sigma / np.sqrt(n) , M_x + t * sigma / np.sqrt(n)} ')