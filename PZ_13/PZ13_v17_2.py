#В матрице найти сумму элементов первых двух строк
import random

matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")

for row in matrix:
    print(row)

sum_first_two_rows = sum(sum(matrix[i]) for i in range(2))
print("\nСумма элементов первых двух строк:", sum_first_two_rows)