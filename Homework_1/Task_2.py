# 2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно. 
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?


from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 

n=combinations(10, 3)
print(f'n = {n}')

# У нас только один блгоприятный исход поэтому m = 1
m = 1
P = m/n

print(f'ответ = {round(P,4)}, 0,83%')