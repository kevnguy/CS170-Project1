import copy
from collections import deque

# goal state
goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

goal = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,0]]

# set of seen states
seen = []

# Used to calculate Manhatten 
coordinates = {}
        
class Node:
    def __init__(self, board, posZero, parent=None) -> None:
        self.board = board
        self.loc_zero = posZero
        self.parent = parent
        if self.parent is not None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0
        self.cost = 0

def findZero(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                return i,j

def printBoard(puzzle) -> None:
    for row in puzzle.board:
        for col in row:
            print("{:^2}".format(col), end=' ')
        print()

def search(root, heristic) -> Node:
    """
    General search algorithm to find a solution if it exists
    """
    global seen
    expansions = 0
    queue = deque([root])
    seen.append(root.board)

    queue = QueueFunction(root, queue, heristic)

    while queue:
        #have to sort queue 
        #queue = deque(sorted(list(queue), key=lambda node: node.cost))
        front_node = queue.popleft()
        if(front_node.board == goal):
            print("Solution found at: depth = {}".format(front_node.depth))
            print("{} Nodes expanded".format(expansions))
            return front_node
        else:
            # update queue with queuing function
            print("Best state to expand with: g(n) = {} and f(n) = {}".format(front_node.depth, front_node.cost))
            printBoard(front_node)
            queue = QueueFunction(front_node, queue, heristic)
            expansions += 1
    else:
        print("No solution found") 

def QueueFunction(node, queue, heristic):
    """
    Queuing function used to expand node and update queue
    """
    global seen
    # 4 possible moves        
    move_up = Node(copy.deepcopy(node.board), copy.deepcopy(node.loc_zero), node)
    move_down = Node(copy.deepcopy(node.board), copy.deepcopy(node.loc_zero), node)
    move_left = Node(copy.deepcopy(node.board), copy.deepcopy(node.loc_zero), node)
    move_right = Node(copy.deepcopy(node.board), copy.deepcopy(node.loc_zero), node)

    # might need to fix cost 
    move_up = moveUp(move_up)
    if move_up is not None:
        if move_up.board not in seen:
            move_up.parent = node
            move_up.cost = move_up.depth + getHeuristic(move_up, heristic)
            seen.append(move_up.board)
            queue.append(move_up)
   
    move_down = moveDown(move_down)
    if move_down is not None:
        if move_down.board not in seen:
            move_down.parent = node
            move_down.cost = move_down.depth + getHeuristic(move_down, heristic)
            seen.append(move_down.board)
            queue.append(move_down)

    move_left = moveLeft(move_left)
    if move_left is not None:
        if move_left.board not in seen:
            move_left.parent = node
            move_left.cost = move_left.depth + getHeuristic(move_left, heristic)
            seen.append(move_left.board)
            queue.append(move_left)

    move_right = moveRight(move_right)
    if move_right is not None:
        if move_right.board not in seen:
            move_right.parent = node
            move_right.cost = move_right.depth + getHeuristic(move_right, heristic)
            seen.append(move_right.board)
            queue.append(move_right)
            
    return queue

def moveUp(node) -> Node:
    i,j =  node.loc_zero
    if i == 0:
        return None
    node.board[i][j], node.board[i - 1][j] = node.board[i - 1][j], node.board[i][j]
    node.loc_zero = (i-1,j)
    return node

def moveDown(node) -> Node:
    i,j =  node.loc_zero
    if i == len(node.board)-1:
         return None
    node.board[i][j], node.board[i + 1][j] = node.board[i + 1][j], node.board[i][j]
    node.loc_zero = (i+1,j)
    return node

def moveLeft(node) -> Node:
    i,j =  node.loc_zero
    if j == 0:
        return None
    node.board[i][j], node.board[i][j - 1] = node.board[i][j - 1], node.board[i][j]
    node.loc_zero = (i,j-1)
    return node

def moveRight(node) -> Node:
    i,j =  node.loc_zero
    if j == len(node.board[0])-1:
        return None
    node.board[i][j], node.board[i][j + 1] = node.board[i][j + 1], node.board[i][j]
    node.loc_zero = (i,j+1)
    return node

def getHeuristic(node, heristic) -> int:
    return 0

def misplacedTileHeuristic(node) -> int:
    cnt = 0
    for i in range(len(node.board)):
        for j in range(len(node.board[0])):
            if node.board[i][j] and node.board[i][j] != goal[i][j]:
                cnt+=1
    return cnt

def manhattanDistanceHeuristic(node) -> int:
    cnt = 0
    for i in range(len(node.board)):
        for j in range(len(node.board[0])):
            if node.board[i][j] and node.board[i][j] != goal[i][j]:
                x,y = coordinates.get(node.board[i][j])
                cnt+=abs(i-x) + abs(j-y)
    return cnt

def printSolution(node) -> None:
    if not node.parent:
        printBoard(node)
        print()
        return
    else:
        printSolution(node.parent)
        printBoard(node)
        print()

def generateCoordinates(root) -> None:
    global coordinates
    length = len(root.board)*len(root.board[0])
    keys = [0]*length
    keys[0:length-1] = list(range(1,length))
    points = []
    for i in range(len(root.board)):    
        for j in range(len(root.board[0])):
            points.append((i,j))
    coordinates = dict(zip(keys,points))

def generateGoal(root) -> None:
    global goal
    cnt = 1
    row = len(root.board)
    col = len(root.board[0])
    goal = [[0]*col for i in range(row)]
    for i in range(row):
        for j in range(col):
            goal[i][j] = (cnt%(row*col))
            cnt+=1

def main():
    start = [[1,2,3,4],
             [5,6,7,8],
             [0,9,10,11]]
    posZero = findZero(start)
    root = Node(start, posZero)
    generateCoordinates(root)
    generateGoal(root)
    print(misplacedTileHeuristic(root))
    print(manhattanDistanceHeuristic(root))
   
    res = search(root,0)

    printSolution(res)
    
if __name__ == "__main__":
    main()
