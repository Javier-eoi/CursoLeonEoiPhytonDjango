"""
Generando numeros aleatorios
"""

import random

for n in range(10):
    print('entero aleatorio:', random.randint(0, 999999))

#numeros entre 0 y 1
for n in range(4):
    print(random.random())


L = ['oscar', 'lucia', 'jaime', 'pepe', 'cris', 'yolanda', 'manuel']
#elemento aleatorio de una lista
for n in range(8):
    print(random.choice(L))

#elementos aleatorios de una lista (puden llegar repetidos)
r = random.choices(L, k=2) #k es el numero de elementos que queremos
print(r)

# cambiar orden de los elementos de forma aleatoria
random.shuffle(L)
print(L)
random.shuffle(L)
print(L)

# a partir de una lista crear otra con elementos que no esten repetidos
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))