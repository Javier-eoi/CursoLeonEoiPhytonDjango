"""
Trabajando con clases y POO
"""

class Thing:
    pass

thing = Thing()

#constructor sin argumentos o parámetros
class Fruit:
    def __init__(self):  #el primer parametro de clase en phyton es siempre self
        print('objeto fruta')

fruit = Fruit()

#argumentos del constructor
class CustomFruit:
    COUNTER = 0
    """ Esta clase no vale para mucho, para escribir comentarios"""
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.juices = 0
        CustomFruit.COUNTER += 1
    
    def __str__(self):
        return 'Soy fruta, me llamo {} y mi color es {}.\nHay {} frutas en total'\
            .format(self.name, self.color, CustomFruit.COUNTER) # la barra sirve para colocar una sentencia en otra linea

    def make_juice(self,count):
        for n in range(count):
            print('haciendo zumo de ', self.name)
            self.juices +=1



custom = CustomFruit('Pera', 'verde')
print(custom)

c2 = CustomFruit('Limón', 'amarillo')
print(c2)
c2.make_juice(4)
print('Zumos hechos', custom2.juices)

