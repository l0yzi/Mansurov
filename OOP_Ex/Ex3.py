class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1
    @staticmethod
    def total_people():
        return(f'Создано {Person.count} объектов')

bob=Person('bob')
Mark=Person('mark')
print(Person.total_people())