#Программа для подсчёта полных тонн в данном количестве килограмм

M = input("Введите массу в киллограммах: ")
try:
    M = int(M)
    tonnes = M // 1000
    if M < 0:
        print("Проверьте правильность введёных данных.")
    else:
        print("Количество полных тонн:", tonnes)

except:
    print("Что-то пошло не так!")




