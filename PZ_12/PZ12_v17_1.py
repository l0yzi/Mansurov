#В последовательности на n целых чисел умножить все элементы на последний/минимальный элемент
import random
seq_length = random.randint(3, 5)
sequence = [random.randint(2, 10) for _ in range(seq_length)]
def multiply_by_min(seq):
    min_element = min(seq)
    multiplied_by_min = [element * min_element for element in seq]
    return multiplied_by_min
def multiply_by_last(seq):
    last_element = seq[-1]
    multiplied_by_last = [element * last_element for element in seq]
    return multiplied_by_last

print("Исходная последовательность:", sequence)
print("Результат умножения на минимальный элемент:", multiply_by_min(sequence))
print("Результат умножения на последний элемент:", multiply_by_last(sequence))
