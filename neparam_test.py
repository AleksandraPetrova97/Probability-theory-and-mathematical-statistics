import numpy as np
import scipy.stats as stats

x1 = np.array([47,90,75,74.5,85,93])
x2 = np.array([58,60,77,67,73.5,89])

# Тест Манна- Уитни в Python
print(stats.mannwhitneyu(x1,x2))

# Критерий Уилкоксона 

print(x2 - x1)
print(stats.wilcoxon(x1,x2))



