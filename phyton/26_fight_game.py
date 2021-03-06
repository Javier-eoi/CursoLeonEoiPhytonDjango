from colorama import init, Fore, Back, Style
from libs import swapi_client
import msvcrt
init()

class Player:
    def __init__(self, player_id, name, gender, power, lives, gems=0):
        self.player_id = player_id
        self.name = name
        self.gender = gender
        self.power = power
        self.lives = lives
        self.gems = gems

class FightGame:
    DEFAULT_LIVES = 2
    DEFAULT_POWER = 10

    def __init__(self, author):
        self.author = author
        self.swapi = swapi_client.Swapi()
        self.players = [] #lista de jugadores vacia, para rellenarla
        self.last_player_id = 0

    def run(self):   
        print(Fore.CYAN, """_____________       ___     __      ________                       
\_   _____/|__| ____ |  |___/  |_   /  _____/_____    _____   ____  
 |    __)  |  |/ ___\|  |  \   __\ /   \  ___\__  \  /     \ / __ \ 
 |   |     |  / /_/  |   Y  \  |   \    \_\  \/ __ \|  Y Y  \  ___/ 
 |___|     |__\___  /|___|__/__|    \________/_____/\__|_|__/\___>
             /_____/                                      by {}""".format(self.author))
        print(Fore.WHITE)
        self.__get_players()
        print('pulsa 0 para obtener ayuda')

        while True:
            option = msvcrt.getch()
            print(option)

            if option == b'\x1b':  #b'\x1b' es la teclas ESC
                break
            if option == b'0':
                self.__menu()
            elif option == b'1':
                self.__add_player()
            elif option == b'2':
                self.__status()
            elif option == b'3':
                self.__fight()
            
    
    def __menu(self):
        print("\n\nAyuda:\n")
        print("0. Mostrar ayuda")
        print("1. Añadir jugador")
        print("2. Status")   
        print(Fore.RED + "3. Luchar")
        print(Fore.WHITE + "C. Clear")
        print("Esc. Salir\n")
    
    def __add_player(self):
        print('add player')
    
    def __status(self):
        for p in self.players:
            print(p.player_id, p.name, p.gender, p.power, p.lives, p.gems)
    
    def __fight(self):
        print('fight')

    def __get_players(self):
        print('obteniendo jugadores desde la api de star wars...')
        people = self.swapi.get_people()
        for person in people:        
            self.last_player_id += 1
            player = Player(
                player_id = self.last_player_id,
                name = person[0],
                gender = person[1],
                power = FightGame.DEFAULT_POWER,
                lives = FightGame.DEFAULT_LIVES
            )
            self.players.append(player)
        print('lista de jugadores prepara')
        self.__status()

FightGame('Javi').run()
"""
Es lo mismo que lo de arriba
game = FightGame('Javi')
game.run()
"""