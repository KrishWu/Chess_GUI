# -*- coding: utf-8 -*-

from termcolor import cprint
import os
from pieces import *
from board import Board


class Game:
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

    def __init__(self):
        self.boardy = Board()

    def translate(self, a1notation):
        try:
            x = self.columnKey[a1notation[0].lower()]
            y = self.rowKey[a1notation[1]]
            return (x, y)
        except BaseException:
            raise MoveException(a1notation)

    def isMoveValid(self, start, end):
        if start == end:
            raise MoveException(
                None, "The move you entered makes it so your piece does not move.")
        piece = self.boardy.board[start[1]][start[0]]
        piece.isMoveValid(self.boardy.board, start, end)

    # General game rules
    def movePiece(self, start, end):
        self.isMoveValid(start, end)
        (sx, sy) = start
        (ex, ey) = end
        self.boardy.movePiece(start, end)
        # when pawn makes it to other side and becomes queen
        if isinstance(self.boardy.board[ey][ex], Pawn):
            if (ey == 7 and self.boardy.board[ey][ex].side == -1) or (
                    ey == 0 and self.boardy.board[ey][ex].side == 1):
                self.boardy.board[ey][ex] = Queen(
                    self.boardy.board[ey][ex].side)

    def main(self):
        error = ""

        while True:
            os.system("clear")
            if error != "":
                cprint("Invalid move! " + error, "red")
                print("")
                error = ""

            # print("")
            self.boardy.printBoard()

            start = input("\nAt what X and Y is the piece you want to move?: ")
            # game.get_piece(start)

            destination = input(
                "At what X and Y do you want the piece to be?: ")

            try:
                (sx, sy) = self.translate(start)
                (ex, ey) = self.translate(destination)
            except Exception as e:
                error = "Invalid input notation."
                error = str(e)
                # os.system("clear")
                continue

            try:
                self.movePiece((sx, sy), (ex, ey))
            except MoveException as e:
                error = "Your move goes against chess rules. " + e.message
            # os.system("clear")


if __name__ == "__main__":
    gamey = Game()
    gamey.main()
    # import unittest
    # from test import *
    # unittest.main()
