# Вариант 17 Задача 2
# Описать функцию PowerA3(A), вычисляющую третью степень числа A
# С помощью этой функции найти третьи степени пяти данных чисел.
try:
    def PowerA3(A):
        return A ** 3
    one = int(input("Введите первое число: "))
    two = int(input("Введите второе число: "))
    three = int(input("Введите третье число: "))
    four = int(input("Введите четвёртое число: "))
    five = int(input("Введите пятое число: "))
    numbers = [one, two, three, four, five]
    results = []

    for num in numbers:
        result = PowerA3(num)
        results.append(result)

    print("Третьи степени чисел: ", results)
except ValueError:
    print("Проверьте правильность введённых данных!")













