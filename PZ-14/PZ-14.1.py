import re

f1 = open('Dostoevsky.txt', 'r', encoding='UTF-8').read()
f = re.findall(r'Достоевск[а-я]+', f1)
print(f)