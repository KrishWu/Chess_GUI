import pygame
from board import Board
from pieces import *

win = pygame.display.set_mode((890, 890))
run = True
pygame.display.set_caption("Chess for Less!")

board = pygame.image.load("./images/board.png")
wPawn = pygame.image.load("./images/white_pawn.png")
bPawn = pygame.image.load("./images/brown_pawn.png")
wRook = pygame.image.load("./images/white_rook.png")
bRook = pygame.image.load("./images/brown_rook.png")
wBishop = pygame.image.load("./images/white_bishop.png")
bBishop = pygame.image.load("./images/brown_bishop.png")
wKnight = pygame.image.load("./images/white_knight.png")
bKnight = pygame.image.load("./images/brown_knight.png")
wQueen = pygame.image.load("./images/white_queen.png")
bQueen = pygame.image.load("./images/brown_queen.png")
wKing = pygame.image.load("./images/white_king.png")
bKing = pygame.image.load("./images/brown_king.png")

coolPieces = [Pawn, Rook, Knight, Bishop, Queen, King]


def find_loc(x, y):
    new_x = ((x) * 110) + 20
    new_y = ((y) * 110) + 20
    return new_x, new_y


def place_board(boardyy):
    # Board
    win.blit(board, (0, 0))
    for y in range(8):
        for x in range(8):
            if isinstance(boardyy.board[x][y], ChessPiece):
                if isinstance(boardyy.board[x][y], Pawn):
                    if boardyy.board[x][y].side == 1:
                        win.blit(wPawn, find_loc(y, x))
                    else:
                        win.blit(bPawn, find_loc(y, x))
                if isinstance(boardyy.board[x][y], Rook):
                    if boardyy.board[x][y] == 1:
                        win.blit(wRook, find_loc(y, x))
                    else:
                        win.blit(bRook, find_loc(y, x))
                if isinstance(boardyy.board[x][y], Knight):
                    if boardyy.board[x][y] == 1:
                        win.blit(wKnight, find_loc(y, x))
                    else:
                        win.blit(bKnight, find_loc(y, x))
                if isinstance(boardyy.board[x][y], Bishop):
                    if boardyy.board[x][y] == 1:
                        win.blit(wBishop, find_loc(y, x))
                    else:
                        win.blit(bBishop, find_loc(y, x))
                if isinstance(boardyy.board[x][y], Queen):
                    if boardyy.board[x][y] == 1:
                        win.blit(wQueen, find_loc(y, x))
                    else:
                        win.blit(bQueen, find_loc(y, x))
                if isinstance(boardyy.board[x][y], King):
                    if boardyy.board[x][y] == 1:
                        win.blit(wKing, find_loc(y, x))
                    else:
                        win.blit(bKing, find_loc(y, x))
                pygame.display.update()


if __name__ == "__main__":
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        place_board()
        pygame.display.update()
    pygame.quit()
