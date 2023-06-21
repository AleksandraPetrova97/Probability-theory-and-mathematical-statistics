# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
# Какова вероятность того, что 3 мяча белые?

from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 

# благоприятные исходы в первой корзине
m_1 = combinations(5, 2) 
m_2 = combinations(5, 1) * combinations(3, 1)
m_3 = combinations(5, 0) * combinations(3, 2)

# благоприятные исходы во второй корзине
m_4 = combinations(5, 1) * combinations(7, 3)
m_5 = combinations(5, 2) * combinations(7, 2)
m_6 = combinations(5, 3) * combinations(7, 1)


n_1 = combinations(8, 2) #общий исход в первой корзине
n_2 = combinations(12, 4) #общий исход во второй корзине

P = (m_1/n_1 * m_4/n_2) + (m_2/n_1 * m_5/n_2) + (m_3/n_1 * m_6/n_2)
 
print(f' Вероятность равна - {round(P*100,2)}%')
