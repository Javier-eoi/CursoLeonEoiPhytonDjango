"""
ejemplo del uso de expresiones regulares
"""

import re #regular expressions

phone = '605133587 # esto es un numero de telefono'

# borrar comentario
number = re.sub(r'#.*$','',phone) # buscar asterisco, todo lo que viene detras lo sustituyes por '' (como no hay nada se borra)
print('Telefono: ', number)

#borrrar cualquier cosa que no sean digitos
number = re.sub(r'\D','',phone)
print('Telefono: ', number)
