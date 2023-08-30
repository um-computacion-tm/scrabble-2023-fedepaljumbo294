from game.cell import Cell  # Importamos la clase Cell desde el módulo cell

class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]  # Creamos una matriz 2D de celdas, cada una con multiplicador 1 y sin multiplicador_type
            for _ in range(15)  # Creamos 15 filas
        ]

