"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, two_level_list):
        self.tlist = two_level_list

    def __str__(self):
        st = []
        for i in range(len(self.tlist)):
            for j in range(len(self.tlist[i])):
                st.append(str(self.tlist[i][j]))
                st.append(' ')
            st.append('\n')
        st1=''.join(st)
        return st1

    def __add__(self, other):
        sum_matrix = []
        end_matrix = []
        print(f'результат сложения матриц: ')
        for i in range(len(self.tlist)):
            for j in range(len(self.tlist[i])):
                sum_matrix.append(self.tlist[i][j] + other.tlist[i][j])
            end_matrix.insert(i, sum_matrix.copy())
            sum_matrix.clear()

        return Matrix(end_matrix)


matrix_one = Matrix([[1, 2, 3],
                     [2, 3, 4],
                     [2, 3, 4]])
matrix_two = Matrix([[7, 6, 5],
                     [7, 8, 9],
                     [2, 3, 4]])

print(matrix_one)
print(matrix_two)

print(matrix_two + matrix_one)

