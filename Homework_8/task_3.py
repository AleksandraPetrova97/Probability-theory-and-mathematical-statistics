# Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности, равной 25 кв.см.
# Объем выборки равен 27, среднее выборочное составляет 174.2. 
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np
from scipy import stats


M_x = 174.2
n = 27
sigma = np.sqrt(25)
z = stats.norm.ppf(0.95)

print(f'Доверительный интервал: {M_x - z * sigma / np.sqrt(n) , M_x + z * sigma / np.sqrt(n)}')