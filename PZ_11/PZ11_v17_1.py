#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и
#отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#a)Исходные данные.
#b)Количество элементов.
#c)Произведение элементов.
#d)Количество пар, для которых произведение элементов делится на 3 (элементы пар в последовательности являются соседями).
import random
file = open('text files/text.txt', 'w')
numbers = [random.randint(-6, 6) for a in range(12)]
file.write(str(numbers))
file.close()

file = open('text files/text.txt', 'r')
data = file.read()
elements = [num for num in data.split(', ')]
count = len(elements)

multiplication = 1
for num in numbers:
    multiplication *= num

pars = sum(1 for i in range(len(numbers) - 1) if (numbers[i] * numbers[i + 1]) % 3 == 0)

f1 = open('text files/text2.txt', 'w')
f1.write(f"Исходные данные: {numbers}\n")
f1.write(f"Количество элементов: {count}\n")
f1.write(f"Произведение элементов: {multiplication}\n")
f1.write(f"Количество пар, для которых произведение элементов делится на 3: {pars}\n")
f1.close()

print('Содержимое текстового файла (исходные данные):', numbers)
print('Количество элементов:', count)
print('Произведение элементов:', multiplication)
print('Количество пар, у которых произведение элементов делится на 3:', pars)
