import random
from common import *

class SupportMNM:
    previousBoard = None

def minimax(board, player, depth, maxDepth, alpha, beta, previousBoard):
    '''
    Return a tuple (best heuristic value, best movement)
    '''
    if depth == maxDepth:
        return (heuristic(board,player),None)
    else:
        movements = generateMovements(board,player,previousBoard)
        if len(movements) == 0:
            return (heuristic(board,player),None)
        bestMovement = None
        for movement in movements:
            tmpBoard = copyBoard(board)

            # update board when player execute the move
            updateBoard(tmpBoard,player,movement)

            # get negative of best heuristic value of opponent after player execute the move
            newValue = -minimax(tmpBoard,-player,depth+1, maxDepth, -beta, -alpha, board)[0]

            if newValue>alpha:
                alpha = newValue
                bestMovement = movement

            # cutoff  
            if alpha>=beta:
                return (alpha,bestMovement)

        return (alpha,bestMovement)

def move_minimax(board, player):
    maxDepth = random.choice([1,2,3,4])
    # alpha = -16, beta = 16 according to the heuristic function
    bestMovement = minimax(board,player,0,maxDepth,-16,16,SupportMNM.previousBoard)[1]
    tmpBoard = board
    updateBoard(tmpBoard,player,bestMovement)
    SupportMNM.previousBoard = tmpBoard
    return bestMovement






        

