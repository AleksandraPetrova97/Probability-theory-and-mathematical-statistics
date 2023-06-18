# 2. Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
# Какова вероятность, что ни одна из них не перегорит в первый день? 
# Какова вероятность, что перегорят ровно две?

from math import factorial,exp

#решение под а

def Poisson(p,n,m):
    lamb = p*n
    return lamb**m/factorial(m)*exp(-lamb)
answer = Poisson(0.0004,5000,0)
print(f'Вероятность равна - {round(answer,4)}')
print(f'Вероятность в процентах равна - {round(answer*100,2)}%')

print()
#решение под б

def Poisson(p,n,m):
    lamb = p*n
    return lamb**m/factorial(m)*exp(-lamb)
answer = Poisson(0.0004,5000,1)
print(f'Вероятность равна - {round(answer,4)}')
print(f'Вероятность в процентах равна - {round(answer*100,2)}%')
