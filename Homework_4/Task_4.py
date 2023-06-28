# 4. Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.

import scipy.stats as stats

def z_value(height):
    return (height-174)/8

# больше 182 см
a = (stats.norm.cdf(z_value(182))) 
print(f' Вероятность, что больше 182 см = {round(1-a,4)}')
# больше 190 см
a = (stats.norm.cdf(z_value(190))) 
print(f' Вероятность, что больше 190 см = {round(1-a,4)}')
# от 166 см до 190 см
a = (stats.norm.cdf(z_value(166))) 
b = (stats.norm.cdf(z_value(190)))
print(f' Вероятность, что от 166 см до 190 см = {round(b-a,4)}')
# от 166 см до 182 см
a = (stats.norm.cdf(z_value(166))) 
b = (stats.norm.cdf(z_value(182)))
print(f' Вероятность, что от 166 см до 182 см = {round(b-a,4)}')
# от 158 см до 190 см
a = (stats.norm.cdf(z_value(158))) 
b = (stats.norm.cdf(z_value(190)))
print(f' Вероятность, что от 158 см до 190 см = {round(b-a,4)}')
# не выше 150 см или не ниже 190 см
a = (stats.norm.cdf(z_value(150))) 
b = (stats.norm.cdf(z_value(190)))
print(f' Вероятность, что не выше 150 см или не ниже 190 см = {round((1-b)+a,4)}')
# не выше 150 см или не ниже 198 см
a = (stats.norm.cdf(z_value(150))) 
b = (stats.norm.cdf(z_value(198)))
print(f' Вероятность, что не выше 150 см или не ниже 198 см = {round((1-b)+a,4)}')
# ниже 166 см
a = (stats.norm.cdf(z_value(166)))
print(f' Вероятность, что ниже 166 см = {round(a,4)}')
