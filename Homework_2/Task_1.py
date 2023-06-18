# 1. Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

from math import factorial

def bernulli(n, k, p):
    return factorial(n)/(factorial(k)*factorial(n-k))\
        *(p**k)*(1-p)**(n-k)

answer = bernulli(100,85,0.8)

print(f'Вероятность равна - {round(answer,4)}')

print(f'Вероятность в процентах равна - {round(answer*100,2)}%')
