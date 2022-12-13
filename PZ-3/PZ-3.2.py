#даны целые числа а, b, с. Проверить истинность высказывания:
# «Существует треугольник со сторонами а, b, с»
a = input("первая сторона треугольника=")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("НЕПРАВИЛЬНЫЙ ВВОД")
        a = input("a=")
b = input("вторая сторона треугольника=")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("НЕПРАВИЛЬНЫЙ ВВОД")
        b = input("b=")
c = input("третья сторона треугольника=")
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print("НЕПРАВИЛЬНЫЙ ВВОД")
        c = input("c=")
if a < b+c and b<a+c and c<a+b :
       print("Треугольник существует")
else:
     print("Треугольник не существует")