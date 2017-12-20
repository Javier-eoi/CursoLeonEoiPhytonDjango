from colorama import init, Fore, Back, Style
init()

print('hola')
print(Fore.BLUE, 'Soy una linea azul')
print(Fore.CYAN, 'Soy una linea cyan')
print(Back.RED + 'Soy una linea roja')
print(Style.RESET_ALL)
print(Fore.RED + 'Soy una linea blanca')