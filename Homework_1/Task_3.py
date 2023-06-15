# 3. В ящике имеется 15 деталей, из которых 9 окрашены. 
# Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?

from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 

n=combinations(15, 3)
print(f'n = {n}')

m=combinations(9, 3)
print(f'm = {m}')

P = m/n

print(f'ответ = {round(P,4)}, 18,46%')