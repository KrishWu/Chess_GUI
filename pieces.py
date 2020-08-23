import pdb


class MoveException(Exception):

    def __init__(self, a1notation, message="Invalid Move! :("):
        self.a1notation = a1notation
        self.message = message

    def __str__(self):
        return self.message


def sign(num):
    if num == 0:
        return 0
    elif num > 0:
        return 1
    elif num < 0:
        return -1


class ChessPiece:
    def __init__(self, side):
        # print("Chess Piece")
        self.side = side

    def isMoveValid(self, board, start, end):
        # print("ChessPiece.testMove()")
        (ex, ey) = end
        if not self.side * board[ey][ex].side <= 0:
            raise MoveException(
                None, "The piece can't move on another of the same side piece.")


class Pawn(ChessPiece):
    def __init__(self, side):
        super().__init__(side)
        # print("Pawn")

    def __str__(self):
        if self.side == -1:
            return "♟"
        else:
            return "♙"

    def isMoveValid(self, board, start, end):
        super().isMoveValid(board, start, end)
        (sx, sy) = start
        (ex, ey) = end
        bStart = board[sy][sx]
        bEnd = board[ey][ex]
        # pdb.set_trace()
        # print("Pawn.testMove()")
        if isinstance(bEnd, EmptySpace):
            # if bEnd == 0:
            # Check for start move
            if bStart.side < 0:
                if sy + 2 == ey and sx == ex and sy == 1:
                    if isinstance(board[sy + 1][sx], EmptySpace):
                        return True
            if bStart.side > 0:
                if sy - 2 == ey and sx == ex and sy == 6:
                    if isinstance(board[sy - 1][sx], EmptySpace):
                        return True
            # Check for normal move
            if sx == ex and ey == sy - bStart.side and bEnd.side == 0:
                return True
            raise MoveException(None, "The pawn had an invalid start move.")
        # Check for attack
        elif bStart.side * bEnd.side < 0:
            if bStart.side < 0 and sy + 1 == ey and abs(ex - sx) == 1:
                return True
            if bStart.side > 0 and sy - 1 == ey and abs(ex - sx) == 1:
                return True
            raise MoveException(None, "The pawn cannot jump multiple spaces when attacking invalid move.")
        else:
            raise MoveException(None, "The pawn had an invalid move.")


class Rook(ChessPiece):
    def __init__(self, side):
        super().__init__(side)
        # print("Rook")

    def __str__(self):
        if self.side == -1:
            return "♜"
        else:
            return "♖"

    def isMoveValid(self, board, start, end):
        super().isMoveValid(board, start, end)
        (sx, sy) = start
        (ex, ey) = end
        bStart = board[sy][sx]
        bEnd = board[ey][ex]
        # Check for normal move
        if sx == ex:
            maybe = sign(ey - sy)
            for y in range(sy + maybe, ey, maybe):
                if not isinstance(board[y][sx], EmptySpace):
                    raise MoveException(
                        None, "The rook cannot jump over another piece.")
            return True
        if ey == sy:
            maybe = sign(ex - sx)
            for i in range(sx + maybe, ex, maybe):
                if not isinstance(board[sy][i], EmptySpace):
                    raise MoveException(
                        None, "The rook cannot jump over another piece.")
            return True
        raise MoveException(None, "The rook must go in a strait line.")


class Knight(ChessPiece):
    def __init__(self, side):
        super().__init__(side)
        # print("Knight")

    def __str__(self):
        if self.side == -1:
            return "♞"
        else:
            return "♘"

    def isMoveValid(self, board, start, end):
        super().isMoveValid(board, start, end)
        (sx, sy) = start
        (ex, ey) = end
        bStart = board[sy][sx]
        bEnd = board[ey][ex]
        # Check for normal move
        moveList = [(1, 2), (-1, 2), (2, 1), (2, -1),
                    (-2, 1), (-2, -1), (-1, -2), (1, -2)]
        for item in moveList:
            try:
                if sx + item[0] == ex and sy + item[1] == ey:
                    return True
            except BaseException:
                pass
        raise MoveException(None, "The knight cannot land in that location")


class Bishop(ChessPiece):
    def __init__(self, side):
        super().__init__(side)
        # print("Bishop")

    def __str__(self):
        if self.side == -1:
            return "♝"
        else:
            return "♗"

    def isMoveValid(self, board, start, end):
        super().isMoveValid(board, start, end)
        (sx, sy) = start
        (ex, ey) = end
        bStart = board[sy][sx]
        bEnd = board[ey][ex]
        # Check for normal move
        try:
            slope = (float(sx) - ex) / (sy - ey)
        except ZeroDivisionError:
            raise MoveException(None, "The Bishop cannot move in a horizontally.")
        if abs(slope) == 1:
            if sx < ex and sy < ey:
                for i in range(1, ex-sx):
                    if not isinstance(board[sy+i][sx+i], EmptySpace):
                        raise MoveException(None, "The Bishop cannot jump over other pieces.")
            elif ex < sx and ey < sy:
                for i in range(1, sx-ex):
                    if not isinstance(board[sy+-i][sx+-i], EmptySpace):
                        raise MoveException(None, "The Bishop cannot jump over other pieces.")
            elif sx < ex and sy > ey:
                for i in range(1, ex-sx):
                    if not isinstance(board[sy+-i][sx+i], EmptySpace):
                        raise MoveException(None, "The Bishop cannot jump over other pieces.")
            elif sx > ex and sy < ey:
                for i in range(1, sx-ex):
                    if not isinstance(board[sy+i][sx-i], EmptySpace):
                        raise MoveException(None, "The Bishop cannot jump over other pieces.")
        else:
            raise MoveException(None, "The Bishop cannot land in that location")


class Queen(ChessPiece):
    def __init__(self, side):
        super().__init__(side)
        # print("Queen")

    def __str__(self):
        if self.side == -1:
            return "♛"
        else:
            return "♕"

    def isMoveValid(self, board, start, end):
        super().isMoveValid(board, start, end)
        # print("Queen.testMove()")
        (sx, sy) = start
        (ex, ey) = end
        bStart = board[sy][sx]
        bEnd = board[ey][ex]
        # Check for straight move
        if sx == ex:
            maybe = sign(ey - sy)
            for y in range(sy + maybe, ey, maybe):
                if not isinstance(board[y][sx], EmptySpace):
                    raise MoveException(
                        None, "The queen cannot jump over another piece.")
            return True
        if ey == sy:
            maybe = sign(ex - sx)
            for i in range(sx + maybe, ex, maybe):
                if not isinstance(board[sy][i], EmptySpace):
                    raise MoveException(
                        None, "The queen cannot jump over another piece.")
            return True
        try:
            slope = (float(sx) - ex) / (sy - ey)
        except ZeroDivisionError:
            raise MoveException(None, "The Queen cannot move in a horizontally.")
        if abs(slope) == 1:
            if sx < ex and sy < ey:
                for i in range(1, ex-sx):
                    if not isinstance(board[sy+i][sx+i], EmptySpace):
                        raise MoveException(None, "The Queen cannot jump over other pieces.")
            elif ex < sx and ey < sy:
                for i in range(1, sx-ex):
                    if not isinstance(board[sy+-i][sx+-i], EmptySpace):
                        raise MoveException(None, "The Queen cannot jump over other pieces.")
            elif sx < ex and sy > ey:
                for i in range(1, ex-sx):
                    if not isinstance(board[sy+-i][sx+i], EmptySpace):
                        raise MoveException(None, "The Queen cannot jump over other pieces.")
            elif sx > ex and sy < ey:
                for i in range(1, sx-ex):
                    if not isinstance(board[sy+i][sx-i], EmptySpace):
                        raise MoveException(None, "The Queen cannot jump over other pieces.")
        else:
            raise MoveException(None, "The Queen cannot land in that location")


class King(ChessPiece):
    def __init__(self, side):
        super().__init__(side)
        # print("King")

    def __str__(self):
        if self.side == -1:
            return "♚"
        else:
            return "♔"

    def isMoveValid(self, board, start, end):
        super().isMoveValid(board, start, end)
        (sx, sy) = start
        (ex, ey) = end
        bStart = board[sy][sx]
        bEnd = board[ey][ex]
        # Check for normal move
        moveList = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        if not isinstance(bEnd, King):
            for item in moveList:
                try:
                    if sx + item[0] == ex and sy + item[1] == ey:
                        for ite in moveList:
                            try:
                                if isinstance(board[ey + ite[0]][ex + ite[1]], King) and bStart.side != board[ey + ite[0]][ex + ite[1]].side:
                                    raise MoveException(None, "There is another King in proximity to this King's end square. This is an illegal move.")
                                # print(bStart.side, board[ex + ite[0]][ey + ite[1]].side) Backwards
                            except IndexError:
                                pass
                        return True
                except BaseException:
                    pass
            raise MoveException(None, "The King cannot land in that location.")
        raise MoveException(None, "The King cannot land in that location because the end space has a king.")


        #     for item in moveList:
        #         try:
        #             if not isinstance(board[sx + item[0], sy + item[1]], King):
        #                 if sx == ex and (sy + 1 == ey or sy - 1 == ey):
        #                     return True
        #                 elif sy == ey and (sx + 1 == ex or sx - 1 == ex):
        #                     return True
        #                 raise MoveException(
        #                     None, "The King cannot land in that location")
        #         except BaseException:
        #             pass
        #             raise MoveException(
        #                 None, "The King cannot land in that location")
        #     raise MoveException(None, "The King cannot land in that location")
        # else:
        #     raise MoveException(None, "The King cannot land in that location")


class EmptySpace:
    side = 0

    def __str__(self):
        return "x"

    def isMoveValid(self, board, start, end):
        raise MoveException(
            None, "You cannot move an empty space! How dumb are you.")
