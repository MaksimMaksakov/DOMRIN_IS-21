#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Элементы первого и второго файлов:
#Элементы после сортировки:
#Количество элементов:
#Минимальный элемент кратный 2:
#Максимальный элемент кратный 5:

import random

f1 = open('file1.txt', 'w+')
f2 = open('file2.txt', 'w+')

for i in range(-6, 6):
    f1.write(f'{str(random.randrange(-6, 6))}\n')
    f2.write(f'{str(random.randrange(-15, 15))}\n')
f1.close()
f2.close()
f1 = open('file1.txt')
f2 = open('file2.txt')

read = f1.readlines()
read2 = f2.readlines()
n = []
for i in read:
    n.append(int(i.replace('\n', '')))

m = []
for i in read2:
    m.append(int(i.replace('\n', '')))
print(n, '\n', m)

all = n + m
poryadok = sorted(all)
lenth = len(all)
all1 = [i / 2 for i in all]
res = min(all1)

all2 = [i / 5 for i in all]
res2 = max(all2)
f3 = open("result.txt", 'w+')
f3.write(f'''Элементы первого и второго файлов: {all} 
Элементы после сортировки: {poryadok}
Количество элементов: {lenth}
Mинимальный элемент кратный 2: {int(res)}
Максимальный элемент кратный 5: {int(res2)}''')

f3.close()
f3 = open('result.txt')
print(f3.read())
