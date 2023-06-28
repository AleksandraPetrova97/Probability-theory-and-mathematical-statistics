# 3.Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья составляет 200 г. 
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет: 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально. 
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%? 
# (Провести двусторонний тест.)

import scipy.stats as stats
import numpy as np

x = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])

x_1 = 200

print(np.mean(x))
print(np.std(x,ddof=1))

t = (np.mean(x) - x_1) / (np.std(x,ddof=1)/np.sqrt(len(x)))
print(t)

print(stats.t.ppf(0.995,9))

# посмотрела в таблице, где степени свободы при a = 0.01, степеней свободы 9, значение 3,250. 
# написала еще формулу и тут тоже 3,250
# двухсторонний тест, получется -1,065 входит в -3,250 и наоборот
# тогда получается гипотеза Н0