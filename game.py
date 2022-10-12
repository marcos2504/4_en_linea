

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
                
                    
        


class TestCuatroEnLinea(unittest.TestCase):

    def test_create_board(self):
        cuatro = CuatroEnLinea()
        self.assertEqual(len(cuatro.board), 8)
        self.assertEqual(len(cuatro.board[0]), 8)

    def test_change_turn(self):
        cuatro = CuatroEnLinea()
        cuatro.change_turn()
        self.assertEqual(cuatro.turn,2)

    def test_column_no_validate(self):
        cuatro= CuatroEnLinea()
        with self.assertRaises(ColumnNoValidate):
            cuatro.insert_ficha(9)
        with self.assertRaises(ColumnNoValidate):
            cuatro.insert_ficha(-1)


    def test_inset_ficha_turn_0(self):
        cuatro= CuatroEnLinea()
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(2)
        self.assertEqual(cuatro.board[-1][1],'1')
        self.assertEqual(cuatro.board[-2][1],'2')
        self.assertEqual(cuatro.board[-3][1],'1')
        self.assertEqual(cuatro.board[-4][1],'2')
        self.assertEqual(cuatro.board[-5][1],'1')
        self.assertEqual(cuatro.board[-6][1],'2')
        self.assertEqual(cuatro.board[-7][1],'1')
        self.assertEqual(cuatro.board[-8][1],'2')
        self.assertEqual(cuatro.board[-1][2],'1')
    
    def test_column_is_full(self):
        cuatro= CuatroEnLinea()
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        with self.assertRaises(ColumnIsfull):
            cuatro.insert_ficha(1)

      

    def test_winner_verify_horizontal(self):
        cuatro= CuatroEnLinea()
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(2)
        cuatro.insert_ficha(2)
        cuatro.insert_ficha(3)
        cuatro.insert_ficha(3)
        cuatro.insert_ficha(4)
        self.assertTrue(cuatro.winner())
        

    def test_no_winner_verify_horizontal(self):
        cuatro= CuatroEnLinea()
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(2)
        self.assertFalse(cuatro.winner())
    
    def test_no_winner_2_verify_horizontal(self):
        cuatro= CuatroEnLinea()
        self.assertFalse(cuatro.winner())

    def test_no_winner_3_verify_horizontal(self):
        cuatro= CuatroEnLinea()
        cuatro.insert_ficha(5)
        self.assertFalse(cuatro.winner())

    def test_winner_verify_vertically(self):
        cuatro= CuatroEnLinea()
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(2)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(2)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(3)
        cuatro.insert_ficha(1)
        self.assertTrue(cuatro.winner())
        

    def test_no_winner_verify_vertically(self):
        cuatro= CuatroEnLinea()
        cuatro.insert_ficha(1)
        self.assertFalse(cuatro.winner())
    
    def test_no_winner_2_verify_vertically(self):
        cuatro= CuatroEnLinea()
        self.assertFalse(cuatro.winner())

    def test_no_winner_3_verify_vertically(self):
        cuatro= CuatroEnLinea()
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(2)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(2)
        cuatro.insert_ficha(1)
        self.assertFalse(cuatro.winner())

    def test_winner_verify_diagonally(self):
        cuatro= CuatroEnLinea()
        cuatro.insert_ficha(0)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(2)
        cuatro.insert_ficha(2)
        cuatro.insert_ficha(3)
        cuatro.insert_ficha(3)
        cuatro.insert_ficha(3)
        cuatro.insert_ficha(2)
        cuatro.insert_ficha(0)
        cuatro.insert_ficha(3)
        self.assertTrue(cuatro.winner())
    def test_no_winner_3_verify_diagonally(self):
        cuatro= CuatroEnLinea()
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        self.assertFalse(cuatro.winner())
    def test_no_winner_4_verify_diagonally(self):
        cuatro= CuatroEnLinea()
        cuatro.insert_ficha(6)
        cuatro.insert_ficha(7)
        cuatro.insert_ficha(7)
        self.assertFalse(cuatro.winner())

    def test_winner_verify_diagonally_down(self):
        cuatro= CuatroEnLinea()
        cuatro.insert_ficha(0)
        cuatro.insert_ficha(0)
        cuatro.insert_ficha(0)
        cuatro.insert_ficha(0)
        cuatro.insert_ficha(0)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(1)
        cuatro.insert_ficha(2)
        cuatro.insert_ficha(2)
        cuatro.insert_ficha(2)
        cuatro.insert_ficha(3)
        self.assertTrue(cuatro.winner())
    
    def test_draw(self):
        InLine = CuatroEnLinea()
        for i in range(3):
            for x in range(8):
                InLine.insert_ficha(x)
        for x in range(2):
            InLine.insert_ficha(1)
            InLine.insert_ficha(2)
            InLine.insert_ficha(5)
            InLine.insert_ficha(0)
            InLine.insert_ficha(3)
            InLine.insert_ficha(6)
            InLine.insert_ficha(7)
            InLine.insert_ficha(4)
        for i in range(3):
            for x in range(8):
                InLine.insert_ficha(x)
        self.assertEqual(InLine.draw(),True)
        
if __name__ == '__main__':
    unittest.main()
        