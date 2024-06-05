# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

import pickle
import random

class Matrix:
    def __init__(self, rows, cols, data):
        self.rows = rows
        self.cols = cols
        self.data = data

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for addition")
        result = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def sub(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы несовместимы для вычитания.")
        result = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j] - other.data[i][j]
        return result
    
    def mul(self, other):
        if self.cols != other.rows:
            raise ValueError("Матрицы несовместимы для умножения.")
        result = [[0 for _ in range(self.cols)] for _ in range(other.rows)]
        for i in range(self.cols):
            for j in range(other.rows):
                for k in range(self.rows):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return result

def save_def(matri, file):
    with open(file, 'wb') as f:
        pickle.dump(matri, f)


def load_def(file):
    with open(file, 'rb') as f:
        matr = pickle.load(f)

    return matr
    
matrix1 = [[random.randint(-5, 5) for i in range(2)] for i in range(2)]
matrix2 = [[random.randint(-5, 5) for i in range(2)] for i in range(2)]
matrix3 = [[random.randint(-5, 5) for i in range(2)] for i in range(2)]

print(f"Матрица 1: {matrix1}")
print(f"Матрица 2: {matrix2}")
print(f"Матрица 3: {matrix3}")

matrix1 = Matrix(len(matrix1[0]), len(matrix1), matrix1)
matrix2 = Matrix(len(matrix2[0]), len(matrix2), matrix2)
matrix3 = Matrix(len(matrix3[0]), len(matrix3), matrix3)

matrix_info = [matrix1, matrix2, matrix3]
for mat in matrix_info:
    save_def(mat, 'matrixes.pkl')
    matrixes = load_def('matrixes.pkl')
    print(f"Сумма матриц: {matrixes.add(matrixes)}")
    print(f"Разность матриц: {matrixes.sub(matrixes)}")
    print(f"Произведение матриц: {matrixes.mul(matrixes)}")