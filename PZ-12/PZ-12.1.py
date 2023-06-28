N = 10  # пример четного числа
sequence = [5, 8, 12, 15, 17, 9, 20, 7, 11, 14]  # пример последовательности

second_half = sequence[N//2:]  # получение второй половины последовательности

sum_greater_than_10 = 0  # переменная для хранения суммы элементов, больших 10

for num in second_half:
    if num > 10:
        sum_greater_than_10 += num

print(sum_greater_than_10)  # вывод результата