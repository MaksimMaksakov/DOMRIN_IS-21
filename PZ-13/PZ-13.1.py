def find_average(matrix):
    count = 0
    total = 0

    for row in matrix:
        for element in row:
            if element > 0:
                count += 1
                total += element

    if count == 0:
        return 0
    else:
        average = total / count
        return average


# Пример использования
matrix = [
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, 9]
]

average = find_average(matrix)
print("Среднее арифметическое положительных элементов:", average)