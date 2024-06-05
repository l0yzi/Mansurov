import tkinter as tk

# Создаем главное окно
window = tk.Tk()
window.title("Регистрация")
window.geometry("500x500")


# Верхняя часть: оранжевый фон с надписью "Регистрация"

top_frame = tk.Frame(window, bg="#FF8C00", height=100)
top_frame.pack(fill=tk.X)

tk.Label(top_frame, text="Регистрация", font=("Arial", 20, "bold"), bg="#FF8C00", fg="#ffe134").pack(side=tk.LEFT)
# Центральная часть: темно-серый фон с полями ввода
center_frame = tk.Frame(window, bg="#222536")
center_frame.pack(fill=tk.BOTH, expand=True)



# Поля ввода
tk.Label(center_frame, text="Имя:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=0, column=0, pady=[30, 5], padx=[180, 0])
tk.Entry(center_frame, width=35).grid(row=0, column=1, pady=[30, 5])

tk.Label(center_frame, text="Фамилия:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=1, column=0, padx=[150, 0])
tk.Entry(center_frame, width=35).grid(row=1, column=1, pady=5)

tk.Label(center_frame, text="Никнейм:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=2, column=0, padx=[150, 0])
tk.Entry(center_frame, width=35).grid(row=2, column=1, pady=5)


# Выпадающие списки для даты рождения
tk.Label(center_frame, text="Дата рождения:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=3, column=0, padx=[100, 0])


months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
days = [str(i) for i in range(1, 32)]
years = [str(i) for i in range(1900, 2023)]
country = ["Россия", "Бельгия", "Бразилия", "Нигерия"]

month_var = tk.StringVar(center_frame, value=months[0])
day_var = tk.StringVar(center_frame, value=days[0])
year_var = tk.StringVar(center_frame, value=years[0])
country_var = tk.StringVar(center_frame, value=country[0])



tk.StringVar(center_frame, value=months[0])
tk.OptionMenu(center_frame, month_var, *months).grid(row=3, column=1, sticky=tk.W, pady=5)


tk.StringVar(center_frame, value=days[0])
tk.OptionMenu(center_frame, day_var, *days).grid(row=3, column=1, sticky=tk.W, pady=5, padx=[90, 0])


tk.StringVar(center_frame, value=years[0])
tk.OptionMenu(center_frame, year_var, *years).grid(row=3, column=1, sticky=tk.W, pady=5, padx=[150, 0])

# Поле "Пол" с радиокнопками
tk.Label(center_frame, text="Пол:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=4, column=0, padx=[180, 0])

gender_var = tk.IntVar()
tk.Radiobutton(center_frame, text="Мужской", variable=gender_var, value=1).grid(row=4, column=1, sticky=tk.W, pady=5)
tk.Radiobutton(center_frame, text="Женский", variable=gender_var, value=2).grid(row=4, column=1, sticky=tk.W, pady=5, padx=[85, 0])


#Страна
tk.Label(center_frame, text="Страна:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=5, column=0, padx=[160, 0])

tk.StringVar(center_frame, value=country[0])
tk.OptionMenu(center_frame, country_var, *country).grid(row=5, column=1,pady=5, sticky=tk.W)



# Поля ввода для email, телефона, пароля и подтверждения пароля


tk.Label(center_frame, text="Email:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=6, column=0, padx=[170, 0])
tk.Entry(center_frame, width=35).grid(row=6, column=1, pady=5)

tk.Label(center_frame, text="Телефон:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=7, column=0, padx=[150, 0])
tk.Entry(center_frame, width=35).grid(row=7, column=1, pady=5)

tk.Label(center_frame, text="Пароль:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=8, column=0, padx=[160, 0])
tk.Entry(center_frame, width=35, show="*").grid(row=8, column=1, pady=5)

tk.Label(center_frame, text="Подтверждение пароля:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=9, column=0, padx=[40, 0])
tk.Entry(center_frame, width=35, show="*").grid(row=9, column=1, pady=5)

# Чекбокс и надпись
terms_var = tk.IntVar()
tk.Checkbutton(center_frame, text="Я согласен с условиями использования", variable=terms_var, fg="#ffe134", selectcolor="#222536", bg="#222536" ).grid(row=11, columnspan=2, padx=[150, 0])

# Нижняя строка: оранжевый фон с кнопками
# Нижняя строка: оранжевый фон с кнопками
bottom_frame = tk.Frame(window, bg="#FF8C00", height=200)
bottom_frame.pack(fill=tk.X)

cancel_button = tk.Button(bottom_frame, text="Отмена", bg="red", fg="white")
cancel_button.pack(side=tk.RIGHT, padx=10)
# Создаем зеленую кнопку регистрации
register_button = tk.Button(bottom_frame, text="Регистрация", bg="green", fg="white")
register_button.pack(side=tk.RIGHT, padx=10)

# Запуск главного цикла окна
window.mainloop()