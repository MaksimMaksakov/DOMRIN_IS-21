#Дано целое число N (> 1). Вывести наибольшее из целых чисел К, для которых сумма
# 1+2+...K
# будет меньше или равна N, и саму эту сумму.

import random
N = random.randrange(2,200)
print('N = ', N)
K = 1
S = 1
while S <= N:
    K += 1
    S += K
    print("K = {0}, S = {1}".format(K,S))
S -= K
K -= 1
print()
print("K = {0}, S = {1}".format(K,S))