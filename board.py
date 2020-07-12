from pieces import *


def find_loc(x, y):
    new_x = ((x) * 110) + 20
    new_y = ((y) * 110) + 20
    return (new_x, new_y)


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
