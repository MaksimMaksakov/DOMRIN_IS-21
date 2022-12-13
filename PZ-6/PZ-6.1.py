#Дан список ненулевых целых чисел размера N. Проверить, чередуются ли в нем положительные и отрицательные числа.
# Если чередуются, то вывести 0,
# если нет, то вывести порядковый номер первого элемента, нарушающего закономерность.
array_len = int(input("N: "))
array = []
for i in range(array_len):
    array.append(int(input(str(i) + " = ")))

k = 0
for i in range(len(array) - 1):
    if array[i] < 0 and array[i + 1] >= 0:
        continue
    elif array[i] >= 0 and array[i + 1] < 0:
        continue
    else:
        k = i + 1
        break
print(k)
