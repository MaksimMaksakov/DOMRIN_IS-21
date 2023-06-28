import numpy as np
import random
a = np.random.randint(10, size=(3, 3))
print(f'Начальная матрица:\n {a} \n')
q = a[0]
w = a[1]
e = a[2]
q = [q[0]**3, q[1], q[2]]
w = [w[0]**3, w[1], w[2]]
e = [e[0**3], e[1], e[2]]
print(f'Измененная матрица: \n {np.row_stack((q, w, e))}')