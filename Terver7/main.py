from scipy import stats as s
import numpy as np
def H0(pv,alpha):
    print(f'{pv}, alpha={alpha}')
    if pv[1] > alpha:
        print('Статистических различий между группами нет')
    else:
        print('Статистические различия между группами есть')

x  = np.array([380,420, 290])
y = np.array([140,360,200,900])
a = 0.05
H0(s.mannwhitneyu(x, y), a)