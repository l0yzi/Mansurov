# Дана строка, состоящая из русских слов, набранных заглавными буквами и разделённых пробелами
# (одним или несколькими). Вывести строку, содержащую эти же слова, разделённые одним пробелом и расположенные в алфавитном порядке.

original_string = "ДАНА СТРОКА СОСТОЯЩАЯ ИЗ РУССКИХ СЛОВ НАБРАННЫХ ЗАГЛАВНЫМИ БУКВАМИ"
words = original_string.split()  # Разбиваем строку на слова
sorted_words = sorted(words)  # Сортируем слова в алфавитном порядке
result_string = ' '.join(sorted_words)  # Объединяем отсортированные слова обратно в строку
print(result_string)