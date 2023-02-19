import math
from math import factorial as f
def C(k, n):
    return f(n)/(f(k)*f(n-k))
def Bn(k,n,p):
    return C(k, n)*(p**k)*((1-p)**(n-k))
def Puas(m,n,p):
    return ((n*p)**m*math.e**(-n*p))/f(m)

'''
Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз.
Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
'''

print(f'Задача 1. Вероятность равна {round(Bn(85,100,0.8)*100,4)}%')

'''
Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. В жилом комплексе после 
ремонта в один день включили 5000 новых лампочек. Какова вероятность, что ни одна из них не перегорит в первый день?
Какова вероятность, что перегорят ровно две?
'''
print(f'Задача 2. а) Вероятность равна {round(Puas(0,5000,0.0004)*100,4)}%')
print(f'Задача 2. б) Вероятность равна {round(Puas(2,5000,0.0004)*100,4)}%')

'''
Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
'''
print(f'Задача 3. Вероятность равна {round(Bn(70,144,0.5)*100,4)}%')

'''
В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые? 
Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?
'''
print(f'Задача 4. а) Вероятность равна {round(Bn(2,2,0.7)*Bn(2,2,9/11)*100,4)}%')
print(f'Задача 4. б) Вероятность равна {round((Bn(1,2,0.7)*Bn(1,2,9/11)) + (Bn(2,2,0.7)*Bn(0,2,9/11)) + (Bn(0,2,0.7)*Bn(2,2,9/11))*100,4)}%')
print(f'Задача 4. в) Вероятность равна {round((1-Bn(2,2,0.3)*Bn(2,2,2/11))*100,4)}%')