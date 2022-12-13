#Даны два целых числа А и В (А < В).
# Вывести в порядке убывания все целые числа, расположенные между А и В (не включая числа А и В),
# а также количество N этих чисел.
import random
B = random.randrange(2,20)
A= random.randrange(1,B)
print('A = ', A)
print('B = ', B)
N = 0
for i in range(B-1, A, -1):
    print(i,end=' ')
    N += 1
print()
print("N = ", N)