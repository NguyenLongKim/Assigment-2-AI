def findTrap(board, player, previousBoard):
    '''
    Return tuple (start position, position of trap) if have a trap,
    otherwise return None
    '''
    if previousBoard == None:
        return None
    diff = []
    for i in range(len(board)):
        for j in range(len(board)):
            if previousBoard[i][j]!=board[i][j]:
                diff.append((i,j))
    if len(diff) == 2:
        trapPos = diff[0] if previousBoard[diff[0][0]][diff[0][1]]==-player else diff[1]
        pair = pairsOfOpponentWillBeCarried(board,player,trapPos)
        if len(pair)>0:
            pos = positionsCanMoveTo(board,trapPos,player)
            if len(pos)>0:
                return (pos[0],trapPos)
    return None


def positionsCanMoveTo(board, curPst, flag=0):
    '''
    Return a list of tuples which each tuple is a position where player can move from "curPst" to 
    Note: flag indicates that player can only move to postition has value = flag
    '''
    pst = []

    up = curPst[0]-1 if curPst[0]-1>=0 else None
    down = curPst[0]+1 if curPst[0]+1<5 else None
    left = curPst[1]-1 if curPst[1]-1>=0 else None
    right = curPst[1]+1 if curPst[1]+1<5 else None

    if up != None and board[up][curPst[1]]==flag:
        pst.append((up,curPst[1]))
    if down != None and board[down][curPst[1]]==flag:
        pst.append((down,curPst[1]))
    if left != None and board[curPst[0]][left]==flag:
        pst.append((curPst[0],left))
    if right != None and board[curPst[0]][right]==flag:
        pst.append((curPst[0],right))

    # if can move on cross
    if (curPst[0]+curPst[1])%2==0:
        if up!=None and left!=None and board[up][left]==flag:
            pst.append((up,left))
        if up!=None and right!=None and board[up][right]==flag:
            pst.append((up,right))
        if down!=None and left!=None and board[down][left]==flag:
            pst.append((down,left))
        if down!=None and right!=None and board[down][right]==flag:
            pst.append((down,right))

    return pst


def pairsOfOpponentWillBeCarried(board, player, desPst):
    '''
        Return a list of tuple which each tuple contains pair of position of opponent
        will be carried if player move to "desPst"
        Ex: list=[((x1,y1),(x2,y2))]
    '''
    rs = []
    
    up = desPst[0]-1 if desPst[0]-1>=0 else None
    down = desPst[0]+1 if desPst[0]+1<5 else None
    left = desPst[1]-1 if desPst[1]-1>=0 else None
    right = desPst[1]+1 if desPst[1]+1<5 else None

    if up != None and down!= None \
    and board[up][desPst[1]]==-player and board[down][desPst[1]]==-player:
        rs.append(((up,desPst[1]),(down,desPst[1])))

    if left != None and right!= None \
    and board[desPst[0]][left]==-player and board[desPst[0]][right]==-player:
        rs.append(((desPst[0],left),(desPst[0],right)))
    
    # if can carry opponents on cross
    if (desPst[0]+desPst[1])%2==0:
        if up != None and left!= None and down!=None and right!=None\
        and board[up][left]==-player and board[down][right]==-player:
            rs.append(((up,left),(down,right)))
        
        if up != None and right!= None and down!=None and left!=None\
        and board[up][right]==-player and board[down][left]==-player:
            rs.append(((up,right),(down,left)))
        
    return rs
    

def generateMovements(board, player, previousBoard):
    '''
    Return a list of tuple which each tuple represents a movement player can execute
    '''
    rs = []
    trap = findTrap(board, player, previousBoard)
    if trap != None:
        rs.append(trap)
        return rs
    else:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == player:
                    pstCanMoveTo = positionsCanMoveTo(board,(i,j))
                    for p in pstCanMoveTo:
                        rs.append(((i,j),p))
        return rs


def heuristic(board, player):
    rs = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==player:
                rs+=1
            elif board[i][j]==-player:
                rs-=1
    return rs


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


def updateBoard(board, player, movement):
    pairs = pairsOfOpponentWillBeCarried(board,player,movement[1])

    # move a chess-piece to the new position
    board[movement[0][0]][movement[0][1]] = 0
    board[movement[1][0]][movement[1][1]] = player

    # carry opponents
    for p in pairs:
        board[p[0][0]][p[0][1]] = player
        board[p[1][0]][p[1][1]] = player

    # surround opponents
    ij = [(i,j) for i in range(len(board)) for j in range(len(board)) if board[i][j]==-player]
    while len(ij)>0:
        newGroup = [ij.pop(0)]
        queue = [newGroup[0]]
        isSurrounded = True
        if len(positionsCanMoveTo(board,newGroup[0]))>0:
            isSurrounded = False
        while len(queue)>0:
            newPos = positionsCanMoveTo(board,queue.pop(0),-player)
            for pos in newPos:
                if pos not in newGroup: 
                    newGroup.append(pos)
                    queue.append(pos)
                    ij.remove(pos)
                    if isSurrounded and len(positionsCanMoveTo(board,pos))>0:
                        isSurrounded = False
        if isSurrounded:
            for pos in newGroup:
                board[pos[0]][pos[1]] = player


def copyBoard(board):
    '''
    deep copy
    '''
    rs = []
    for row in board:
        rs.append(row.copy())
    return rs


def gameOver(board):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board)):
            sum+=board[i][j]
    if sum==16:
        return 1
    elif sum==-16:
        return -1
    else:
        return 0