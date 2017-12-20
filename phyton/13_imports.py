"""Vamos a importar el modulo utils que hemos creado y otros mas"""

import utils #Lo ponemos asi porque este archivo y el de utils estan al mismo nivel
#Llamo al metodo
utils.lib_method()

#Voy a importar el modulo bombing entero
from libs import bombing
bombing.where_are_the_bombs()

#Otra manera de importar partes del modulo que me hagan falta
#Si es mas de una parte detras del import pongo lo que quiera separado por comas
from libs.bombing import where_are_the_bombs
where_are_the_bombs()

#Quiero llamar al metodo de otra manera cuando lo importo
from libs.bombing import where_are_the_bombs as where
where()

#Acceso directo a los metodos de un modulo//otra forma de importar el modulo entero
from libs.eating import *
eat_apples(5)
eat_pie('300g')