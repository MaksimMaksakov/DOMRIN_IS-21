#Даны числа х, у. Проверить истинность высказывания: «Точка с координатами (X, У)
# лежит в четвертой координатной четверти».
x = input("x=")
while type(x) != int:
    try:
        x = int(x)
    except ValueError:
        print("НЕПРАВИЛЬНЫЙ ВВОД")
        x = input("x=")
y = input("y=")
while type(y) != int:
    try:
        y = int(y)
    except ValueError:
        print("НЕПРАВИЛЬНЫЙ ВВОД")
        y = input("y=")
if x > 0:
    if y < 0:
        print("True")
    else:
        print("False")