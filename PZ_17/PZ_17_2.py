# Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ 2-9



# PZ_4_1
# Дано целое число N(>0).
# Используя один цикл, найти сумму 1+1/(1!)+1/(2!)+1/(3!)+...+1/(N!)
# (выражение N! - N-факториал - обозначает произведение всех целых чисел от 1 до N: N! = 1-2-...-N)
# Полученное число является приближенным значением константы e=exp(1)



import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        N = int(entry.get())
        if N <= 0:
            raise ValueError("N должно быть больше 0")

        sum = 0
        factorial = 1
        for i in range(N + 1):
            sum += 1 / factorial
            label_progress.config(text=f"Итерация {i}: сумма = {sum:.6f}, факториал = {factorial}")
            factorial *= (i + 1)
            window.update()  # Обновляем окно для отображения прогресса выполнения вычислений

        label_result.config(
            text=f"Сумма равна: {sum:.6f}\nПриближенное значение константы e: {math.exp(1):.6f}"
        )
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

window = tk.Tk()
window.title("Вычисление суммы и приближения константы e")

tk.Label(window, text="Введите целое число N (>0):").pack(pady=5)
entry = tk.Entry(window)
entry.pack(pady=5)

button = tk.Button(window, text="Рассчитать", command=calculate)
button.pack(pady=5)

label_progress = tk.Label(window, text="")
label_progress.pack(pady=5)

label_result = tk.Label(window, text="")
label_result.pack(pady=5)

window.mainloop()
