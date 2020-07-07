import unittest
import pieces
import main

if __name__ == "__main__":
    unittest.main()


class ChessTest(unittest.TestCase):

    def testTranslate(self):
        g = main.Game()
        g.boardy.printBoard()
        self.assertEqual((0, 7), g.translate("a1"))
        self.assertRaises(
            pieces.MoveException,
            g.translate,
            "99999999999999999999999")
        self.assertIsInstance(g.boardy["a2"], pieces.Pawn)
        self.assertIsInstance(g.boardy["b3"], pieces.EmptySpace)
        g.boardy["b3"] = pieces.Pawn(1)
        self.assertIsInstance(g.boardy["b3"], pieces.Pawn)

    def testValid(self):
        g = main.Game()
        self.assertIsNone(g.isMoveValid((0, 6), (0, 4)))
        self.assertIsNone(g.isMoveValid((0, 6), (0, 5)))
        self.assertRaises(pieces.MoveException, g.isMoveValid, (0, 6), (0, 6))
        self.assertIsNone(g.isMoveValid((0, 6), (0, 4)))
        self.assertRaises(pieces.MoveException, g.isMoveValid, (0, 6), (1, 5))
        g.movePiece((0, 6), (0, 4))
        g.movePiece((0, 4), (0, 3))
        g.movePiece((0, 3), (0, 2))
        self.assertIsNone(g.isMoveValid((0, 2), (1, 1)))
        g.movePiece((0, 2), (1, 1))
        g.movePiece((1, 1), (0, 0))
        self.assertIsInstance(g.boardy.board[0][0], pieces.Queen)
        # move pawn to other side, capture a piece
        # move pawn to last row on the far side, switch to queen
        # try moving an empty space

    def testRook(self):
        g = main.Game()
        print("Lalallalalalal")
        g.boardy.printBoard()
        self.assertRaises(pieces.MoveException, g.isMoveValid, (0, 7), (0, 5))
        g.boardy['a2'] = pieces.EmptySpace()
        self.assertIsNone(g.isMoveValid((0, 7), (0, 5)))
