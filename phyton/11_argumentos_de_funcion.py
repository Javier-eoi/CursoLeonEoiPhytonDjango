""" 
diferentes formas de usar argumentos 
"""
def hi(name):
    print('Hi', name)

#hi() #esto falla porque "name" es obligatorio

#valores por defecto de argumento
def f(n='uno'):
    print(n)

f()

def f2(one, two, three=3):
    print('one:', one, 'two:', two, 'three:', three)

#usar argumentos por orden
f2(45, 10, 22)

#usar argumentos como keywords
f2(two=90, one=23, three=89)

def dime_cosas_sucias(*args):
    print(args)
dime_cosas_sucias(20, 30, 90, True, False, 'Nasty')

def f3(name, *args):
    print('hola', name)
    print(args)

f3('Pedro', 20, 30, 90, True, False, 'Nasty')

t = ('Pedro', 20, 30, 90, True, False, 'Nasty')
f3('Diego', *t)

def f4(**kwars): #kwars significa argumentos clave, devuelve un diccionario
    print(kwars)

f4(c='uno', b='3', a='manolo', d=True)

o = {'c': 'uno', 'b': '3', 'a': 'manolo', 'f':True}
f4(**o)