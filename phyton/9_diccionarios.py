""" los diccionarios son similares a los objetos de JS"""
ALUMNO = {
    'nombre': 'Boni', 
    'edad': 2,
    'clase': 'Perro' 
}
print(ALUMNO['nombre'], ALUMNO['edad'], ALUMNO['clase'])

ALUMNO['edad'] = 18
print(ALUMNO)

ALUMNO['sexo'] = 'Varón'
print(ALUMNO)

del ALUMNO['sexo']
print(ALUMNO)


ALUMNO.clear()
print(ALUMNO)

del ALUMNO
print(ALUMNO)

