# Из предложенного текстового файла (text18-17.txt) вывести на экран его содержимое, количество букв в нижнем регистре.
# Сформировать новый файл, в который поместить текст в стихотворной форме предварительно поставив последнюю строку между первой и второй.

file = open('text files/text18-17.txt', 'r')
content = file.read()
print("Содержимое файла 'text18-17.txt':")
print(content)
file.close()

signs = [",", ".", ":", ";", "-", "—", "!"]
signs_count = sum(content.count(p) for p in signs)
print(f"Количество знаков препинания: {signs_count}")


file = open('text files/text18-17_v2.txt', 'w')
lines = content.split('\n')
new_poem = f"{lines[0]}\n{lines[-1]}\n{lines[1]}\n{lines[2]}\n{lines[3]}\n{lines[4]}\n{lines[5]}\n\n"
file.writelines(new_poem)
file.close()


file = open('text files/text18-17_v2.txt', 'r')
contents = file.read()
print(f"\n{contents}")
file.close()




