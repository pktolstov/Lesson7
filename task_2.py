"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def count_cloth(self):
        return


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def count_cloth(self):
        return f'расход ткани на пошив пальто: {round(self.size / 6.5 + 0.5, 2)}'


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def count_cloth(self):
        return f'расход ткани на пошив костюма: {round(self.height / 100 * 2 + 0.3, 2)}'


c = Coat(50)
print(c.count_cloth)

s = Suit(178)
print(s.count_cloth)
