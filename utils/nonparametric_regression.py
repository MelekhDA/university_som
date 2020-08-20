from utils.default_core import parabolic_core

import math

__all__ = [
    'NonParametricEstimator'
]


class NonParametricEstimator:

    def __init__(self, x: list, y: list, dx: float, *args, **kwargs):
        assert len(x) == len(y), 'Lists x and y must match in length'

        self._x = x.copy()
        self._y = y.copy()
        self._dx = dx
        self._n = len(self._x)

    def find_beta(self, step: float = 1e-4, core=parabolic_core, *args, **kwargs) -> float:
        """Простой поиск минимального значения с шагом"""

        leftBorder = 0
        rightBorder = 1
        x = (leftBorder + rightBorder) / 2

        length = rightBorder - leftBorder

        while length > step:

            functionOfX = self.regression_estimate(x, core)

            y = leftBorder + length / 4
            z = rightBorder - length / 4

            functionOfY = self.regression_estimate(y, core)
            functionOfZ = self.regression_estimate(z, core)

            if functionOfY < functionOfX:
                rightBorder = x
                x = y
            else:
                if functionOfZ < functionOfX:
                    leftBorder = x
                    x = z
                else:
                    leftBorder = y
                    rightBorder = z

            length = math.fabs(rightBorder - leftBorder)

        return (leftBorder + rightBorder) / 2

    def regression_estimate(self, b: float, core, *args, **kwargs) -> float:
        """Оценка"""

        t_sum = 0
        for i in range(self._n):
            t_sum += (self._y[i] - self.f_n(i, b, core)) ** 2

        return t_sum / self._n

    def f_n(self, i: int, b: float, core=parabolic_core, cond: bool = False, *args, **kwargs):
        """
        Непараметрическая егрессионная оценка при фиксированном
        коэффициенте размытости (в качестве безразмерной величины): 0 <= b <= 1
        """

        sum_numerator = 0
        sum_denominator = 0

        for j in range(self._n):
            if i != j or cond:
                temp = core(b * (self._x[i] - self._x[j]) / self._dx)

                sum_numerator += self._y[j] * temp
                sum_denominator += temp

        return sum_numerator / sum_denominator
