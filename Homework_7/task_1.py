# Даны две  независимые выборки. Не соблюдается условие нормальности
# x1  380,420, 290
# y1 140,360,200,900
# Сделайте вывод по результатам, полученным с помощью функции

import scipy.stats as stats
import numpy as np

x1 = np.array([380 ,420, 290])
y1 = np.array([140, 360, 200, 900])

print(stats.mannwhitneyu(x1,y1))

# Делаем вывод, что статистически значимых различий нет, так как p.value > a