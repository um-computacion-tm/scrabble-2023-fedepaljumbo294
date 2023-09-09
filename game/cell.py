from game.models import Tile  # Importamos la clase Tile desde el módulo models

class Cell:
    def __init__(self, multiplier=1, multiplier_type="letter",letter=None,active=True):
        self.multiplier = multiplier  # Asignamos el valor del multiplicador al atributo 'multiplier'
        self.multiplier_type = multiplier_type  # Asignamos el tipo de multiplicador al atributo 'multiplier_type'
        self.letter = letter  # Inicializamos el atributo 'letter' como None (sin letra)
        self.active = active
    def add_letter(self, letter:Tile):
        self.letter = letter  # Asignamos el objeto Tile proporcionado al atributo 'letter'

    def calculate_value(self):
        if self.letter is None:
            return 0  # Si no hay letra en la celda, el valor calculado es 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier  # Si el multiplicador es 'letter', calculamos el valor de la letra con el multiplicador
        else:
            return self.letter.value  # Si no, simplemente devolvemos el valor de la letra
