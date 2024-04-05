#Приложение БЮРО ПО ТРУДОУСТРОЙСТВУ для некоторой организации. БД должна содержать таблицу
#Работник со следующей структурой записи: фамилия, имя, отчество, возраст, пол, профессия, стаж работы.
import sqlite3 as sq

con = sq.connect('Employment_agency.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Worker (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Surname TEXT,
        Name TEXT,
        Middle_name TEXT,
        Age INTEGER,
        Gender TEXT,
        Profession TEXT,
        Work_exp INTEGER
    )
''')

employees = [
    ('Петров', 'Петр', 'Петрович', 35, 'Мужской', 'Инженер', 8),
    ('Сидорова', 'Анна', 'Ивановна', 28, 'Женский', 'Бухгалтер', 4),
    ('Козлов', 'Алексей', 'Сергеевич', 41, 'Мужской', 'Уборщица', 12),
    ('Иванова', 'Елена', 'Павловна', 33, 'Женский', 'HR-специалист', 6),
    ('Смирнов', 'Дмитрий', 'Александрович', 29, 'Мужской', 'Программист', 5),
    ('Кузнецова', 'Ольга', 'Дмитриевна', 38, 'Женский', 'Дизайнер', 10),
    ('Васильев', 'Максим', 'Николаевич', 45, 'Мужской', 'Администратор', 15),
    ('Павлов', 'Сергей', 'Игоревич', 31, 'Мужской', 'Тестировщик', 7),
    ('Морозова', 'Мария', 'Алексеевна', 27, 'Женский', 'Аналитик', 3),
    ('Николаев', 'Владимир', 'Петрович', 39, 'Мужской', 'Программист', 9)
]

# cursor.executemany('''
#     INSERT INTO Worker (Surname, Name, Middle_name, Age, Gender, Profession, Work_exp)
#     VALUES (?, ?, ?, ?, ?, ?, ?)
# ''', employees)


# Запросы
cursor.execute('SELECT * FROM Worker')
print("Все позиции в таблице:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Worker WHERE Profession = 'Программист'")
print("\nПрограммисты:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Worker WHERE Gender = 'Женский' AND Age < 30")
print("\nЖенщины младше 30 лет:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Worker WHERE Work_exp >= 10")
print("\nСотрудники со стажем работы 10 и более лет:")
for row in cursor.fetchall():
    print(row)

# update
cursor.execute("UPDATE Worker SET Surname = 'Пушкина' WHERE Work_exp = 10")
cursor.execute("UPDATE Worker SET Profession = 'Менеджер' WHERE Age > 40")
cursor.execute("UPDATE Worker SET Age = 31 WHERE Profession = 'Бухгалтер'")
con.commit()


cursor.execute("DELETE FROM Worker WHERE Age = 39")
cursor.execute("DELETE FROM Worker WHERE Surname = 'Петров'")
cursor.execute("DELETE FROM Worker WHERE Work_exp = 6")


cursor.execute('SELECT * FROM Worker')
print("\nВсе позиции в таблице после удаления:")
for row in cursor.fetchall():
    print(row)
con.close()
