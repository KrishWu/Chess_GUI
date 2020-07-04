import pygame


def find_loc(x, y):
    new_x = ((x)*110)+20
    new_y = ((y)*110)+20
    return (new_x, new_y)


win = pygame.display.set_mode((890, 890))
run = True

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
    pygame.display.set_caption("Chess for Less!")
    # Board
    win.blit(board, (0, 0))
    # Pawns
    for i in range(8):
        win.blit(wPawn, find_loc(i, 6))
    for i in range(8):
        win.blit(bPawn, find_loc(i, 1))
    # Rooks
    win.blit(wRook, find_loc(0, 7))
    win.blit(wRook, find_loc(7, 7))
    win.blit(bRook, find_loc(0, 0))
    win.blit(bRook, find_loc(7, 0))
    # Bishops
    win.blit(wBishop, find_loc(2, 7))
    win.blit(wBishop, find_loc(5, 7))
    win.blit(bBishop, find_loc(2, 0))
    win.blit(bBishop, find_loc(5, 0))
    # Knights
    win.blit(wKnight, find_loc(1, 7))
    win.blit(wKnight, find_loc(6, 7))
    win.blit(bKnight, find_loc(1, 0))
    win.blit(bKnight, find_loc(6, 0))
    # Queens
    win.blit(wQueen, find_loc(3, 7))
    win.blit(bQueen, find_loc(3, 0))
    # Kings
    win.blit(wKing, find_loc(4, 7))
    win.blit(bKing, find_loc(4, 0))
    pygame.display.update()
pygame.quit()