#Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
#Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
#"Человек". Каждый класс должен иметь метод, который выводит информацию о
#поле объекта
class Chel:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Man(Chel):

    def returns(self):
        return self.gender


class Woman(Chel):
    def returns(self):
        return self.gender


krut = Man('ДЭН', 52, 'Мужчина')
lame = Woman('АНТОНИна', 8, 'Женщина')
print(krut.__dict__)
print(krut.returns())
print(lame.__dict__)
print(lame.returns())
