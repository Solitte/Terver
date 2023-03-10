from scipy import stats as s
import numpy as np
def H0(stats,alpha):
    print(f'{stats}, alpha={alpha}')
    if stats[1] > alpha:
        print('Статистических различий между группами нет')
    else:
        print('Статистические различия между группами есть')
'''
Задача 1. 
Даны две независимые выборки. Не соблюдается условие нормальности
x1 380,420, 290
y1 140,360,200,900
Сделайте вывод по результатам, полученным с помощью функции, имеются ли статистические различия между группами?
'''
x = np.array([380,420, 290])
y = np.array([140,360,200,900])
a = 0.05
print('Задача 1.')
H0(s.mannwhitneyu(x, y), a)

'''
Задача 2. 
Исследовалось влияние препарата на уровень давления пациентов. Сначала
измерялось давление до приема препарата, потом через 10 минут и через 30 минут. Есть
ли статистически значимые различия между измерениями давления? В выборках не соблюдается условие нормальности.
1е измерение до приема препарата: 150, 160, 165, 145, 155
2е измерение через 10 минут: 140, 155, 150, 130, 135
3е измерение через 30 минут: 130, 130, 120, 130, 125
'''
x = np.array([150, 160, 165, 145, 155])
y = np.array([140, 155, 150, 130, 135])
z = np.array([130, 130, 120, 130, 125])
a = 0.05
print('Задача 2.')
H0(s.friedmanchisquare(x, y, z), a)

'''
Задача 3. 
Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было. Есть
ли статистически значимые различия между измерениями давления?
'''
x = np.array([150, 160, 165, 145, 155])
y = np.array([140, 155, 150, 130, 135])
a = 0.05
print('Задача 3.')
H0(s.wilcoxon(x, y), a)

'''
Задача 4. 
Даны 3 группы учеников плавания. Не соблюдается условие нормальности.
В 1 группе время на дистанцию 50 м составляют:
56, 60, 62, 55, 71, 67, 59, 58, 64, 67
Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54
Есть ли статистически значимые различия между группами?
'''
x = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
y = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
z = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])
a = 0.05
print('Задача 4.')
H0(s.kruskal(x, y, z), a)

'''
Задача 5. 
Заявляется, что партия изготавливается со средним арифметическим 2,5 см. Проверить
данную гипотезу, если известно, что размеры изделий подчинены нормальному закону
распределения. Объем выборки 10, уровень статистической значимости 5%
2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34
'''
n = 10
m0 = 2.5
a = 0.05
x = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
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
print('Задача 5.')
print(f'tn - {tn}, tkr1 - {tkr1}, tkr2 - {tkr2}')
if tkr1 < tn < tkr2:
    print('Гипотеза верна')
else:
    print('Гипотеза неверна')
