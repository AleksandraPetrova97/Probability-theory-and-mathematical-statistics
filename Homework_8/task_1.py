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

print(cov)
print(np.cov(zp,ks,ddof= 0)) #Смещенная ковариация

pirson = cov / np.std(zp, ddof= 0) * np.std(ks, ddof= 0) #коэффециент Пирсона
print(pirson)

print(np.corrcoef(zp,ks)) # Линейная зависимость есть, и она сильная

x = np.mean(zp)
t_x = stats.t.ppf(0.95,9)
sigma_x = np.std(zp,ddof=0)
n_x = np.sqrt(len(zp))
print((x - t_x) * (sigma_x / n_x), (x + t_x) * (sigma_x / n_x))

y = np.mean(ks)
t_y = stats.t.ppf(0.95,9)
sigma_y = np.std(ks,ddof=0)
n_y = np.sqrt(len(ks))
print((y - t_y) * (sigma_y / n_y), (y + t_y) * (sigma_y / n_y))

