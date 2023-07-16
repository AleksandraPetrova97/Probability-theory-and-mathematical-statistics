# Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy 
# Полученные значения должны быть равны. Найдите коэффициент корреляции Пирсона 
# с помощью ковариации и среднеквадратичных отклоненийдвух признаков,
# а затем с использованием функций из библиотек numpy и pandas.

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

cov = np.mean(zp*ks) - np.mean(zp) * np.mean(ks) #Ковариация в ручную

print(f'Ковариация в ручную: {cov}')
print(f'Ковариация смещенная: {np.cov(zp,ks,ddof= 0)}') #Смещенная ковариация

pirson = cov / (np.std(zp, ddof= 0) * np.std(ks, ddof= 0)) #коэффециент Пирсона
print(f'Коэффециент Пирсона: {pirson}')

print(f'Линейная зависимость и сила зависимости: {np.corrcoef(zp,ks)}') # Линейная зависимость есть, и она сильная

x = np.mean(zp)
t_x = stats.t.ppf(0.95,9)
sigma_x = np.std(zp,ddof=0)
n_x = np.sqrt(len(zp))
print(f' Доверительный интервал у среднего значения заработной платы: {x - t_x * sigma_x / n_x, x + t_x * sigma_x / n_x}')

y = np.mean(ks)
t_y = stats.t.ppf(0.95,9)
sigma_y = np.std(ks,ddof=0)
n_y = np.sqrt(len(ks))
print(f' Доверительный интервал у среднего значения кредитного скоринга: {y - t_y * sigma_y / n_y, y + t_y * sigma_y / n_y}')

plt.scatter(zp, ks)
plt.title('Experiment')
plt.xlabel('wages')
plt.ylabel('credit scoring')
plt.tight_layout()
plt.show()
#  по графику можно сделать вывод, что чем больше заработная плата, тем больше значение кредитного скоринга


