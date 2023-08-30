import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter # Asignamos la letra al atributo 'letter' de la ficha
        self.value = value # Asignamos el valor al atributo 'value' de la ficha


class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A', 1), # Creamos una ficha con letra 'A' y valor 1
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
        ]
        random.shuffle(self.tiles) # Barajamos (mezclamos) las fichas de manera aleatoria

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop()) # Tomamos una ficha de la bolsa y la añadimos a la lista 'tiles'
        return tiles # Devolvemos la lista de fichas tomadas

    def put(self, tiles):
        self.tiles.extend(tiles) # Agregamos las fichas proporcionadas de nuevo a la bolsa

