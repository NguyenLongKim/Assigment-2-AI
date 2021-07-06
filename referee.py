from minimax import move_minimax
from common import updateBoard, gameOver, generateMovements, copyBoard
from random import choice

def startGame(board):
    previousBoard = None
    player = -1
    i = 1
    while (True):
        possibleMovements = generateMovements(board,player,previousBoard)
        movement = None
        if player == -1:
            movement = choice(possibleMovements)
        else:
            movement = move_minimax(board,player)
        if movement in possibleMovements:
            previousBoard = copyBoard(board)
            updateBoard(board,player,movement)
            print('state ' + str(i) + ':')
            printBoard(board)
            print()
            if gameOver(board)!=0:
                break 
            player = -player
            i+=1    
        else:
            print("Illegal movement")
            print("Possible movements: ",possibleMovements)
            print("Your movement",movement)
            break

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

board = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, -1],
        [-1, 0, 0, 0, -1],
        [-1, -1, -1, -1, -1]]

print('State 0:')
printBoard(board)
print()

startGame(board)






