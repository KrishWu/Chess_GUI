import pygame
from board import Board
from pieces import *

coolPieces = [Pawn, Rook, Knight, Bishop, Queen, King]


def find_loc(x, y):
    new_x = ((x) * 110) + 20
    new_y = ((y) * 110) + 20
    return (new_x, new_y)


def place_board():
    # Board
    win.blit(board, (0, 0))
    for y in range(8):
        for x in range(8):
            if isinstance(Board.board[x, y], ChessPiece):
                if isinstance(Board.board[x, y], Pawn):
                    if Board.board[x, y].side == 1:
                        win.blit(wPawn, find_loc(x, y))
                    else:
                        win.blit(bPawn, find_loc(x, y))
                if isinstance(Board.board[x, y], Rook):
                    if Board.board[x, y] == 1:
                        win.blit(wRook, find_loc(x, y))
                    else:
                        win.blit(bRook, find_loc(x, y))
                if isinstance(Board.board[x, y], Knight):
                    if Board.board[x, y] == 1:
                        win.blit(wKnight, find_loc(x, y))
                    else:
                        win.blit(bKnight, find_loc(x, y))
                if isinstance(Board.board[x, y], Bishop):
                    if Board.board[x, y] == 1:
                        win.blit(wBishop, find_loc(x, y))
                    else:
                        win.blit(bBishop, find_loc(x, y))
                if isinstance(Board.board[x, y], Queen):
                    if Board.board[x, y] == 1:
                        win.blit(wQueen, find_loc(x, y))
                    else:
                        win.blit(bQueen, find_loc(x, y))
                if isinstance(Board.board[x, y], King):
                    if Board.board[x, y] == 1:
                        win.blit(wKing, find_loc(x, y))
                    else:
                        win.blit(bKing, find_loc(x, y))



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

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    place_board()
    pygame.display.update()
pygame.quit()
