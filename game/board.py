from game.cell import Cell  # Importamos la clase Cell desde el módulo cell

class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]  # Creamos una matriz 2D de celdas, cada una con multiplicador 1 y sin multiplicador_type
            for _ in range(15)  # Creamos 15 filas
        ]

    def calculate_word_value(self,word):
        sum=0
        m=1

        for aux in word:
            if aux.active==False:
                aux.multiplier=1
            if aux.multiplier_type=="letter":
                sum+=aux.letter.value*aux.multiplier
                
            else:
                sum+=aux.letter.value
                m=aux.multiplier*m
                    

        return sum*m
