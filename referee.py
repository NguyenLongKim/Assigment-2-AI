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
                c = 'X'
            elif e == -1:
                c = 'O'
            print(c,end='   ')
        print()

def startGame(board):
    player = -1
    i = 0
    while (i<70):
        movement = None
        if player == -1:
            movement = move(board,player,2)
        else:
            movement = choice(generateMovements(board,player))
        updateBoard(board,player,movement)
        printBoard(board)
        print()
        player = - player
        i+=1
    
board = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, -1],
        [-1, 0, 0, 0, -1],
        [-1, -1, -1, -1, -1]]

printBoard(board)
print()

startGame(board)

