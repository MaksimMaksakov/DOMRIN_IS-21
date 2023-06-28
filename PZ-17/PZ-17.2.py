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


krut = Man('ДЭН', 52, 'Мужик')
lame = Woman('АНТОНИна', 8, 'Женщина')
print(krut.__dict__)
print(krut.returns())
print(lame.__dict__)
print(lame.returns())