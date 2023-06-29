#2.Составить генератор (yield), который выводит из строки только буквы.
def letters_generator(string):
    for char in string:
        if char.isalpha():
            yield char

# Пример использования:
string = "OBLA735!"
letters = letters_generator(string)

for letter in letters:
    print(letter)
