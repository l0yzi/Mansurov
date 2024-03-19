import re
with open('experience.txt', 'r', encoding='utf-8') as file:
    data = file.read()

pattern = r'\d+.*'
matches = re.findall(pattern, data)

for match in matches:
    print(match)

count = len(matches)
print(f'Общее количество элементов стажа работы: {count}')