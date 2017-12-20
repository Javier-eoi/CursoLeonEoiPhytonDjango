"""
Ejemplos para trabajar con tuplas. Objeto inmutable, menos pesado que una lista e inmodificable
"""

TUP = (1, 2, 3, 4, 5, "seis")

print(TUP)
print(TUP[0])
print(TUP[4])
print(TUP[2:5])
print(TUP[:3])
print(TUP[2:])

size = len(TUP)
print('tamaño de la TUPa:', size)

# concatenar dos TUPas
TUP += ('siete' , 8, True, False)
print(TUP)

SUMA = (3 + 2 ) - 1
print(SUMA)

T2 = (3,)
print(T2)
print(type(T2))