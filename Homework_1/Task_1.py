#1. Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 

# Решаем под а

m=combinations(13, 4)
print(f'm = {m}')

n=combinations(52, 4)
print(f'n = {n}')

P=m/n

print(f'Ответ части а = {round(P,4)}, 0,26%')  

# Решаем под б

n=combinations(52, 4)
print(f'n = {n}')

m =combinations(48,4)
print(f'm = {m}')

P = 1 - (m/n)

print(f'Ответ части б = {round(P,4)}, 28,13%')