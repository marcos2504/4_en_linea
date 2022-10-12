

import unittest


class ColumnIsfull(Exception):
    pass
class ColumnNoValidate(Exception):
    pass

class CuatroEnLinea:
    def __init__(self):
        self.board = [[0 for _ in range(8)] 
        for _ in range(8)]
        self.turn = 1
        
    
    def change_turn(self):
        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2 :
            self.turn = 1 

    def calculate_row(self,column):
        row = -1
        while row >= -7:
                if self.board[row][column] == 0:
                    break
                else:
                    row -= 1
        return row


    def insert_ficha(self,col):
        
        if col>7 or col< 0:
            raise ColumnNoValidate()
        elif self.board[0][col] != 0:
            raise ColumnIsfull()
        
        else:
            if self.turn == 1:
                self.board[self.calculate_row(col)] [col]= '1'
                self.change_turn()
                  

            elif self.turn == 2:
                self.board[self.calculate_row(col)] [col]= '2'   
                self.change_turn()
        self.winner()
        self.draw()   

    def verify_horizontal(self,row,col):
        token= self.board[row][col]
        if not token:
            return False
        for delta_col in range(4):
            if (col+delta_col)> 7:
                return False
            elif self.board[row][(delta_col+col)] != token:
                return False 
        else:
                return True
    
    def verify_vertically(self,row,col):
        token= self.board[row][col]
        if not token:
            return False
        for delta_row in range(4):
            if (row+delta_row)> 7:
                return False
            elif self.board[delta_row+row][(col)] != token:
                return False 
        else:
                return True
    
    def verify_diagonally_up(self,row,col):
        token= self.board[row][col]
        if not token:
            return False
        for delta  in range (4):
            if row < 4 or col > 4:
                return False
            elif self.board[row-delta][col+delta] != token:
                return False 
        else:
                return True
    def verify_diagonally_down(self,row,col):
        token= self.board[row][col]
        if not token:
            return False
        for delta  in range (4):
            if row >4 or col > 4:
                return False
            elif self.board[row+delta][col+delta] != token:
                return False 
        else:
                return True


            
    def winner(self):
        for row in range(8):
            for col in range(8):
                if self.verify_horizontal(row,col):
                    return True
                if self.verify_vertically(row,col):
                    return True
                if self.verify_diagonally_up(row,col):
                    return True
                if self.verify_diagonally_down(row,col):
                    return True
        return False
    
    def draw(self):
        if not any( 0 in x for x in self.board):
            return True
                
                    
        


