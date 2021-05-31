from minimax import *
from random import choice

def gameOver(board, player):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == player:
                return False
    return True

def printBoard(board):
    for row in board:
        for e in row:
            c = '-'
            if e == 1:
                c = 'O'
            elif e == -1:
                c = 'X'
            print(c,end='   ')
        print()

def startGame(board):
    player = -1
    previousBoardO = board
    while (True):
        movement = None
        if player == -1:
            movement = move(board,player)
        else:
            movement = choice(generateMovements(board,player,previousBoardO))
        updateBoard(board,player,movement)
        if player==1:
            previousBoardO = board
        printBoard(board)
        print()
        if gameOver(board,-player):
            break 
        player = - player
    
board = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, -1],
        [-1, 0, 0, 0, -1],
        [-1, -1, -1, -1, -1]]

printBoard(board)
print()

startGame(board)

