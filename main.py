
from game import *

class main:
    def __init__(self):
        self.cuatro= CuatroEnLinea()
        

    def create_board(self):
        print("\n")
        for r in range(8):
            print(f"  ({r+1}) ", end="")
        print("\n")

        for r in range(8):
            print('|', end="")
            for c in range(8):
                print(f"  {self.cuatro.board[r][c]}  |", end="")
            print("\n")

        print(f"{'-' * 52}\n")

    def run(self):
        game_over= False
        while game_over == False:
                self.create_board()
                columna = input(f"TURNO JUGADOR {self.cuatro.turn}- ELIJA UNA COLUMNA (1-8): ")
                try:
                    self.cuatro.insert_ficha(int(columna)-1)
                    if self.cuatro.winner or self.cuatro.draw():
                        self.create_board()
                    
                    if self.cuatro.winner() or self.cuatro.draw():
                        game_over = True
                except ColumnNoValidate:
                    print('COLUMNA NO VALIDA ELIJA OTRA')
                except ColumnIsfull:
                    print('COlUMNA LLENA ELIJA OTRA')
        self.cuatro.change_turn()
        if self.cuatro.winner():
            print(f'GANADOR JUGADOR {self.cuatro.turn}')
        elif self.cuatro.draw():
            print('El juego temino en EMPATE')

main().run()



