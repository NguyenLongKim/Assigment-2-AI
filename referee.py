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
    i = 1
    while (True):
        movement = None
        if player == -1:
            movement = move_mcts(board,player)
        else:
            movement = move_minimax(board,player)
        updateBoard(board,player,movement)
        print('state ' + str(i) +':')
        printBoard(board)
        print()
        if gameOver(board)!=0:
            break 
        player = -player
        i+=1
    
board = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, -1],
        [-1, 0, 0, 0, -1],
        [-1, -1, -1, -1, -1]]

print('State 0:')
printBoard(board)
print()

startGame(board)

