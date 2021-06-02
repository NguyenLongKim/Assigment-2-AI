from minimax import move_minimax
from monte_carlo import move_mcts
from common import updateBoard, gameOver


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
    while (True):
        movement = None
        if player == -1:
            movement = move_minimax(board,player)
        else:
            movement = move_mcts(board,player)
        updateBoard(board,player,movement)
        printBoard(board)
        print()
        if gameOver(board)!=0:
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

