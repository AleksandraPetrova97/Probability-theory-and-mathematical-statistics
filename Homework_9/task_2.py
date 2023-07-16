# Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).

import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

def _mse(b, x, y):
    return np.sum((b*x-y)**2)/len(x)

print(_mse(2.62, zp, ks))

def mse_(b, y = ks, x = zp, n = 10):
    return np.sum((b*x - y)**2)/n

alpha = 1e-6
b = 0.1
n = 10
mse_min=_mse(b,zp,ks)
i_min = 1
b_min = b

for i in range(1000):
    b -= alpha * (2/n) * np.sum((b * zp - ks) * zp)
    if i % 100 == 0:
        print('Iteranion = {i}, b = {b}, mse = {mse}'.format(i = i, b = b, mse = mse_(b)))     
    if _mse(b,zp,ks) > mse_min:
        print(f'Iteranion = {i_min}, b = {b_min}, mse = {mse_min},\n Минимум достигнут.')
        break
    else:
        mse_min = _mse(b,zp,ks)
        i_min=i
        b_min=b 




   