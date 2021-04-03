"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
"""


class Cell:
    def __init__(self, sub_cell: int):
        self.sub_cell = sub_cell

    def __str__(self):
        return f'Клетка с количеством ячеек: {self.sub_cell}'

    def __add__(self, other):
        return Cell(self.sub_cell + other.sub_cell)

    def __sub__(self, other):
        if self.sub_cell - other.sub_cell > 0:
            return Cell(self.sub_cell - other.sub_cell)
        else:
            return f'Клетка слишком мала для вычитания'

    def __mul__(self, other):
        return Cell(self.sub_cell * other.sub_cell)

    def __truediv__(self, other):
        return Cell(self.sub_cell // other.sub_cell)

    def make_order(self, amount_row_cell: int):
        st = ''
        for i in range(self.sub_cell // amount_row_cell):
            #st += '*' * amount_row_cell + '\\n' # Вернет строку идентичную примеру в задании при вызове print()
            st += '*' * amount_row_cell + '\n' # Вернет строку с переносами при вызове функции print()
        st += '*' * (self.sub_cell % amount_row_cell)
        # st=str('\n'.join([''.join(['*' for j in range(self.sub_cell)]))
        return st


a = Cell(15)
b = Cell(7)
c = Cell(3)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(c - b)

print(a.make_order(4))
