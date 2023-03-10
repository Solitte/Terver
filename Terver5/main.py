from scipy import stats as s
import numpy as np
'''
Задача 1.
Когда используется критерий Стьюдента, а когда Z – критерий?
'''
print('Задача 1.')
print('Критерий Стьюдента используется, когда сигма генеральной совокупности не известна')
print('Z – критерий используется, когда сигма генеральной совокупности известна')
'''
Задача 2. 
Проведите тест гипотезы. Утверждается, что шарики для подшипников, изготовленные
автоматическим станком, имеют средний диаметр 17 мм.
Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из
n=100 шариков средний диаметр оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм.
'''
m0 = 17
xmean = 17.5
a = 0.05
d = 4
n = 100
tn = (xmean - m0) / (d / n)**0.5
tkr = s.norm.ppf(1 - a)
print('Задача 2.')
print(f'tn - {tn}, tkr - {tkr}')
if tn < tkr:
    print('Утверждение верно')
else:
    print('Утверждение неверно')

'''
Задача 3. 
Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья
составляет 200 г.
Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
Известно, что их веса распределены нормально.
Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна
99%? (Провести двусторонний тест.)
'''
n = 10
m0 = 200
a = 0.01
x = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
sum = 0
for i in range(len(x)):
      sum += x[i]
xmean = sum/len(x)
sum = 0
for i in range(len(x)):
      sum += (x[i] - xmean)**2
d = sum/(len(x) - 1)
tn = (xmean - m0) / (d / n)**0.5
tkr1 = s.t.ppf(a / 2, n-1)
tkr2 = s.t.ppf(1 - a / 2, n-1)
print('Задача 3.')
print(f'tn - {tn}, tkr1 - {tkr1}, tkr2 - {tkr2}')
if tkr1 < tn < tkr2:
    print('Утверждение верно')
else:
    print('Утверждение неверно')

'''
Задача 4. 
Есть ли статистически значимые различия между средним ростом
дочерей и матерей?
Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165
Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160, 163
'''
x = np.array([172, 177, 158, 170, 178,175, 164, 160, 169, 165])
y = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160, 163])
a = 0.05
tn = s.ttest_rel(x, y)
print('Задача 4.')
print(tn)
pvalue = tn[1]
if pvalue > a:
    print('Cтатистически значимых различий между средним ростом дочерей и матерей нет')
else:
    print('Cтатистически значимых различий между средним ростом дочерей и матерей есть')

