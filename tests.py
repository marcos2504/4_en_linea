import unittest
from game import *
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
        