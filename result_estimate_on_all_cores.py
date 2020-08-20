#
# Непараметрическая оценка регрессиии на 4-х ядрах
#

import pylab, random, math

from utils import default_core as core, nonparametric_regression as regression

# имитационная модель
imit_model = lambda x: round(math.sin(x) + 3, 15)

# начальная точка, шаг, объём выборки
x0, dx, n = 1, 0.05, 200

# входы имитационной модели
x = [round(x0 + i * dx, 15) for i in range(n)]

# выходы имитационной модели
y = [imit_model(i) for i in x]

# выход модели с аддитивной помехой
y_e = [round(i + random.normalvariate(0, 1), 15) for i in y]

non_regr = regression.NonParametricEstimator(x=x, y=y_e, dx=dx)

# названия рассматриваемых ядерных функций
names_core = ['прямоугольное', 'треугольное', 'параболическое', 'кубическое']
# ядерные фукцнии
cores = [core.uniform_core, core.traingular_core, core.parabolic_core, core.cube_core]

for name_core, core in zip(names_core, cores):

    min_b = non_regr.find_beta(core=core)

    out_min = []

    for i in range(n):
        out_min.append(non_regr.f_n(i, min_b, core, True))

    pylab.plot(x, out_min, label=f'Регрессионная оценка, {name_core} ядро')

pylab.scatter(x, y, edgecolors=(0.5, 1.0, 0.0), s=10, label='Без помехи')
pylab.scatter(x, y_e, edgecolors=(0.5, 1.0, 0.0), s=20, label='С помехой')

pylab.ylabel("Y")
pylab.xlabel("X")
pylab.legend()
pylab.grid()
pylab.show()
