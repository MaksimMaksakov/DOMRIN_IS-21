#Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
#площади, длины окружности и диаметра.
import math
from random import randint


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def ploshad(self):
        return math.pi * self.radius**2

    def dlina(self):
        return self.radius * 2 * math.pi

    def diametr(self):
        return self.radius * 2


bbb = Circle(randint(5, 10))
print(bbb.__dict__)
print(f'\nПлощадь: {bbb.ploshad()}\n')
print(f'Длина: {bbb.dlina()}\n')
print(f'Диаметр: {bbb.diametr()}\n')
