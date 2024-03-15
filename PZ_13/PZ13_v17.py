#Cгенерировать матрицу на произвольное количество элементов,
#в которой задаётся преобразование от предыдущего элемента к следующему на произвольное значение
import random

matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]

print("Исходная матрица:")
for row in matrix:
    print(row)

transformed_matrix = [[row[i] * 2 for i in range(4)] for row in matrix]

print("\nПреобразованная матрица:")
for row in transformed_matrix:
    print(row)
