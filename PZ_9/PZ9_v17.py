#Дан словарь на 6 персон, найти и вывести их средний возраст.
#(Пример, {"Андрей": 32, "Виктор": 29, "Максим":18, ...}, среднее 26,33)
ages = {
    "Андрей": 32,
    "Виктор": 29,
    "Максим": 18,
    "Елена": 35,
    "Ольга": 30,
    "Ирина": 40
}

total_age = sum(ages.values())
num_people = len(ages)
average_age = total_age / num_people

print(ages)
print("Средний возраст:",average_age, "лет")