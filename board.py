from pieces import *


def find_loc(x, y):
    new_x = ((x) * 110) + 20
    new_y = ((y) * 110) + 20
    return (new_x, new_y)

columnKey = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7}
rowKey = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}

class Board:
    def __init__(self):
        self.board = [
            [Rook(-1), Knight(-1), Bishop(-1), Queen(-1),
             King(-1), Bishop(-1), Knight(-1), Rook(-1)],
            [Pawn(-1), Pawn(-1), Pawn(-1), Pawn(-1),
             Pawn(-1), Pawn(-1), Pawn(-1), Pawn(-1)],
            [EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(),
             EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace()],
            [EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(),
             EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace()],
            [EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(),
             EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace()],
            [EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(),
             EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace()],
            [Pawn(1), Pawn(1), Pawn(1), Pawn(1),
             Pawn(1), Pawn(1), Pawn(1), Pawn(1)],
            [Rook(1), Knight(1), Bishop(1), Queen(1),
             King(1), Bishop(1), Knight(1), Rook(1)]
        ]

    def printBoard(self):
        for row in self.board:
            for column in row:
                print(column, "", end="")
            print("")

    def parseMove(self, start):
        if len(start) == 2:
            sx = columnKey[start[0]]
            sy = rowKey[start[1]]
            return (sy, sx)
        else:
            raise ValueError(start)

    def movePiece(self, start, end):
        (sx, sy) = start
        (ex, ey) = end
        self.board[ey][ex] = self.board[sy][sx]
        self.board[sy][sx] = EmptySpace()

    def checkWin(self):
        wKing = False
        bKing = False
        for y in range(8):
            for x in range(8):
                if isinstance(self.board[y][x], King):
                    if self.board[y][x].side == 1:
                        wKing = True
                    else:
                        bKing = True
        if wKing and bKing:
            return ""
        if wKing and not bKing:
            return "The white side has won!"
        if bKing and not wKing:
            return "The black side has won!"



    def translate(self, a1notation):
        try:
            x = self.columnKey[a1notation[0].lower()]
            y = self.rowKey[a1notation[1]]
            return (x, y)
        except BaseException:
            raise MoveException(a1notation)

    def __getitem__(self, key):
        (x, y) = self.translate(key)
        return self.board[y][x]

    def __setitem__(self, key, value):
        (x, y) = self.translate(key)
        self.board[y][x] = value
