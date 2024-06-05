
class Note:
    def __init__(self, text, iscompleted):
        self.text = text
        self.iscompleted = iscompleted
        self.count=0

    def upcount(self, int):
        self.count+=int

    def reset_count(self):
        self.count=0

note1 = Note("Задача 1", True)
print(note1.__dict__)
note1.upcount(3)
print(note1.__dict__)
note1.reset_count()
print(note1.__dict__)