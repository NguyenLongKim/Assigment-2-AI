import random
import math
from common import *

class SupportMCTS:
    previousBoard = None


class Node:
    def __init__(self):
        self.board = None
        self.player = None
        self.parent = None
        self.children = None
        self.w = None
        self.n = None
        self.unvisited_movement = None
        self.creating_movement = None

    def isFullyExpanded(self):
        return len(self.unvisited_movement)==0

    def pickBestUCTChild(self):
        uct = 0
        best_uct_child = None
        for child in self.children:
            tmp_uct = child.w/child.n + 2*pow(math.log(self.n)/child.n,1/2)
            if tmp_uct>uct:
                best_uct_child = child
        return best_uct_child

    def pickUnVisitedChild(self):
        unvisited_movement = self.unvisited_movement.pop(0)
        tmpBoard = copyBoard(self.board)
        updateBoard(tmpBoard,self.player,unvisited_movement)
        child = Node()
        child.board = tmpBoard
        child.player = -self.player
        child.children = []
        child.w = 0
        child.n = 0
        child.parent = self
        child.unvisited_movement = generateMovements(child.board,child.player,self.board)
        child.creating_movement = unvisited_movement
        self.children.append(child)
        return child

    def pickBestMovement(self):
        n = 0
        best_child = None
        for child in self.children:
            if child.n > n:
                n = child.n
                best_child = child
        return best_child.creating_movement


def move_mcts(board, player):
    trap = findTrap(board,player,SupportMCTS.previousBoard)
    if trap!=None:
        return trap
    root = Node()
    root.board = board
    root.player = player
    root.parent = None
    root.children = []
    root.w = 0
    root.n = 0
    root.unvisited_movement = generateMovements(board,player,SupportMCTS.previousBoard)
    root.creating_movement = None
    best_movement = monte_carlo_tree_search(root)
    tmpBoard = copyBoard(board)
    updateBoard(tmpBoard,player,best_movement)
    SupportMCTS.previousBoard = tmpBoard
    return best_movement


def monte_carlo_tree_search(root:Node):
    i = 0
    while (i<100):
        leaf = traverse(root)
        simulation_result = rollout(leaf)
        backpropagate(leaf,simulation_result)
        i+=1
    return root.pickBestMovement()


def traverse(node:Node):
    tmpNode = node
    while tmpNode.isFullyExpanded():
        tmpNode = tmpNode.pickBestUCTChild()
    return tmpNode.pickUnVisitedChild()


def rollout(node:Node):
    board = copyBoard(node.board)
    previousBoard = None
    player = node.player
    while True:
        flag = gameOver(board)
        if flag!=0:
            return flag
        movement = random.choice(generateMovements(board,player,previousBoard))
        previousBoard = copyBoard(board)
        updateBoard(board,player,movement)   
        player = -player


def backpropagate(node:Node, simulation_result):
    tmpNode = node
    while tmpNode != None:
        tmpNode.n+=1
        if tmpNode.player == simulation_result:
            tmpNode.w+=1
        tmpNode = tmpNode.parent

    
# board = [[1, 1, 1, 1, 1],
#         [1, 0, 0, 0, 1],
#         [1, 0, 0, 0, -1],
#         [-1, 0, 0, 0, -1],
#         [-1, -1, -1, -1, -1]]


# printTree(move(board,1))