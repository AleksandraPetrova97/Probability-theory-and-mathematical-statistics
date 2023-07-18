# Провести дисперсионный анализ для определения того, есть ли различия среднего роста 
# среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов: 
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182. 
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180. 
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170. 

import numpy as np
from scipy import stats


football_players = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey_players = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

print(stats.f_oneway(football_players,hockey_players,weightlifters))
# по результату дисперсионного анализа статистически значимые различия есть 

# проведем проверку на нормальность

print(stats.shapiro(football_players))
print(stats.shapiro(hockey_players))
print(stats.shapiro(weightlifters))

# по тесту Шапиро выборки имеют нормальное распределение

# проведем проверку на равенство дисперсий
print(stats.bartlett(football_players, hockey_players, weightlifters))
# по результату p_value дисперсии равны

k = 3
n = len(football_players) + len(hockey_players) + len(weightlifters)

# посчитаем среднее по каждой выборке
mean_football = np.mean(football_players)
mean_hockey = np.mean(hockey_players)
mean_weightlifters = np.mean(weightlifters)

# объединим все выборки в одну, так как они разного размера используем функцию concatenate
all_teams = np.concatenate([football_players, hockey_players, weightlifters])
# среднее всех выборок
mean_generals = np.mean(all_teams)
print(mean_generals)

S_generals = np.sum((all_teams - mean_generals)**2)
print(S_generals)
S_f = np.sum((mean_football - mean_generals)**2) * len(football_players) \
        + np.sum((mean_hockey - mean_generals)**2) * len(hockey_players) \
        + np.sum((mean_weightlifters - mean_generals)**2) * len(weightlifters)

S_ost = np.sum((football_players - mean_football)**2) \
            + np.sum((hockey_players - mean_hockey)**2) \
            + np.sum((weightlifters - mean_weightlifters)**2)
print(S_f + S_ost)

D_f = S_f / (k - 1)

D_ost = S_ost / (n - k)

# критерий Фишера наблюдаемый
F_n = D_f / D_ost
print(F_n)

# критерий Фишера табличный
alpha = 0.05
k1 = k - 1
k2 = n - k

F_tabl = stats.f.ppf(1 - alpha, k1, k2)
print(F_tabl)
# делаем вывод: F_n > F_tabl, поэтому H0 отвергается, а это означает, 
# что статистически значимые различия в росте спортсменов разных видов спорта присутствуют