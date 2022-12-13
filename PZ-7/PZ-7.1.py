#Даны целые положительные числа N1 и N2 и строки S1 и S2. Получить из этих строк новую
# строку, содержащую первые
# N1 символов строки S1 и последние N2 символов строки S2 (в указанном порядке).
import random
ru_letters = u"абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
en_letters = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = u"0123456789"
letters = ru_letters + en_letters + digits
K1 = random.randrange(1,21)
N1 = random.randrange(1,K1+1)
S1 = ''.join(random.choice(letters) for _ in range(K1))
K2 = random.randrange(1,21)
N2 = random.randrange(1,K2+1)
S2 = ''.join(random.choice(letters) for _ in range(K2))
print("N1:",N1)
print("K1:",K1)
print("S1:",S1)
S1_length = len(S1)
print("Length of S1:",S1_length)
print()
print("N2:",N2)
print("K2:",K2)
print("S2:",S2)
S2_length = len(S2)
print("Length of S2:",S2_length)
S1_new = S1[:N1]
S1_new_length = len(S1_new)
print("\nNew S1:",S1_new)
print("Length of new S1:",S1_new_length)
S2_new = S2[-N2:]
S2_new_length = len(S2_new)
print("\nNew S2:",S2_new)
print("Length of new S2:",S2_new_length)
print("\nNew string:",S1_new+" "+S2_new)