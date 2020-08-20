from typing import Union
import math

__all__ = [
    'uniform_core', 'traingular_core',
    'parabolic_core', 'cube_core'
]


def uniform_core(z: Union[float, int]) -> Union[float, int]:
    """Равномерная ядерная фукнция"""

    if math.fabs(z) <= 1:
        return 0.5

    return 0


def traingular_core(z: Union[float, int]) -> Union[float, int]:
    """Треугольная ядерная функция"""

    if math.fabs(z) <= 1:
        return 1 - math.fabs(z)

    return 0


def parabolic_core(z: Union[float, int]) -> Union[float, int]:
    """Параболическая (Епанечникова) ядерная функция"""

    if math.fabs(z) <= 1:
        return 0.75 * (1 - z ** 2)

    return 0


def cube_core(z: Union[float, int]) -> Union[float, int]:
    """Кубическая ядерная функция"""

    if math.fabs(z) <= 1:
        return (1 + 2 * math.fabs(z)) * (1 - math.fabs(z)) ** 2

    return 0
