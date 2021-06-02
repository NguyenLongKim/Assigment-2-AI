from common import *

class SupportMNM:
    previousBoard = None


def move_minimax(board, player):
    maxDepth = 4
    # alpha = -16, beta = 16 according to the heuristic function
    bestMovement = minimax(board,player,0,maxDepth,-16,16,SupportMNM.previousBoard)[1]
    tmpBoard = board
    updateBoard(tmpBoard,player,bestMovement)
    SupportMNM.previousBoard = tmpBoard
    return bestMovement






        

