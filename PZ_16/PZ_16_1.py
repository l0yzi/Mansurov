# Создайте класс "Матрица", который имеет атрибуты количество строк и столбцов.
# Добавьте методы для сложения, вычитания и умножения матриц.
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
    
matrix1 = [[random.randint(-5, 5) for i in range(2)] for i in range(2)]
matrix2 = [[random.randint(-5, 5) for i in range(2)] for i in range(2)]

print(f"Матрица 1: {matrix1}")
print(f"Матрица 2: {matrix2}")

matrix1 = Matrix(len(matrix1[0]), len(matrix1), matrix1)
matrix2 = Matrix(len(matrix2[0]), len(matrix2), matrix2)
res_add = matrix1.add(matrix2)
print(f"Сумма матриц: {res_add}")
res_sub = matrix1.sub(matrix2)
print(f"Разность матриц: {res_sub}")
res_mul = matrix1.mul(matrix2)
print(f"Произведение матриц: {res_mul}")
