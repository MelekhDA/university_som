#
# Непараметрическая оценка регрессиии
#

import pylab, random, math

from utils import default_core, nonparametric_regression as regression

# имитационная модель
imit_model = lambda x: round(math.sin(x) + 3, 15)
# ядерная функция
core = default_core.cube_core

# начальная точка, шаг, объём выборки
x0, dx, n = 1, 0.05, 150

# входы имитационной модели
x = [round(x0 + i * dx, 15) for i in range(n)]

# выходы имитационной модели
y = [imit_model(i) for i in x]

# выход модели с аддитивной помехой
y_e = [round(i + random.normalvariate(0, 5), 15) for i in y]

non_regr = regression.NonParametricEstimator(x=x, y=y, dx=dx)

min_b = non_regr.find_beta()

opt_result = []

for i in range(n):
    opt_result.append(non_regr.f_n(i, min_b, core, True))

# имитац. модель
pylab.scatter(x, y, edgecolors=(0.5, 1.0, 0.0), s=10, label='Без помехи')
pylab.scatter(x, y_e, edgecolors=(0.5, 1.0, 0.0), s=20, label='С помехой')
# регрессионная оценка
pylab.plot(x, opt_result, color='black', label='Регрессионная оценка')

#
# оценка регрессии при b = {0, 1}
#

out_min_b_1 = []

for i in range(n):
    out_min_b_1.append(non_regr.f_n(i, 1, core, True))

pylab.plot(x, out_min_b_1, color='r', label='Регрессионная оценка при b = 1')

out_min_b_0 = []
for i in range(n):
    out_min_b_0.append(non_regr.f_n(i, 0, core, True))

pylab.plot(x, out_min_b_0, color='b', label='Регрессионная оценка при b = 0')

pylab.ylabel("Y")
pylab.xlabel("X")
pylab.legend()
pylab.grid()
pylab.show()
