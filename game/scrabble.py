from game.board import Board  # Importamos la clase Board desde el módulo board
from game.player import Player  # Importamos la clase Player desde el módulo player
from game.models import BagTiles  # Importamos la clase BagTiles desde el módulo models

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()  # Creamos una instancia de la clase Board y la asignamos al atributo 'board'
        self.bag_tiles = BagTiles()  # Creamos una instancia de la clase BagTiles y la asignamos al atributo 'bag_tiles'
        self.players = []  # Creamos una lista vacía 'players' para almacenar los jugadores del juego
        for _ in range(players_count):
            self.players.append(Player())  # Creamos una instancia de la clase Player y la agregamos a la lista 'players'

