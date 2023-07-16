# Произвести вычисления как в пункте 2, но с вычислением intercept.
# Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно
# (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).

import numpy as np

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

def _mse_ab(a, b, x, y):
    return np.sum(((a+b*x)-y)**2)/len(x)

alpha = 5e-05
n = 10
b=0.1
a=0.1
mseab_min=_mse_ab(a,b,x,y)
i_min=1
b_min=b
a_min=a
   
for i in range(1000000):
    a-=alpha * (np.sum(((a+b*x)-y))/n)*2
    b-=alpha * (np.sum((a + b * x - y) * x)/n)*2
    if i%50000==0:
        print(f'Итерация #{i}, a={a}, b={b}, mse={_mse_ab(a, b, x, y)} ')
    if _mse_ab(a, b, x, y) > mseab_min:
        print(f'Итерация #{i_min}, a={a_min}, b={b_min}, mse={mseab_min},\nДостигнут минимум.')
        break

