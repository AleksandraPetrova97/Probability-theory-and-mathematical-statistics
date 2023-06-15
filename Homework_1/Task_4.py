# 4. В лотерее 100 билетов. Из них 2 выигрышных. 
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 

n=combinations(100, 2)
print(f'n = {n}')
m = 1
P = m/n

print(f'ответ = {round(P,4)}, 0,02%')