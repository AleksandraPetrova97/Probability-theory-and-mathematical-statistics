# 3. Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

from math import factorial

def bernulli(n, k, p):
    return factorial(n)/(factorial(k)*factorial(n-k))\
        *(p**k)*(1-p)**(n-k)

answer = bernulli(144,70,0.5)

print(f'Вероятность равна - {round(answer,4)}')

print(f'Вероятность в процентах равна - {round(answer*100,2)}%')