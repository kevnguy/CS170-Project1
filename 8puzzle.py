import copy
from collections import deque

# goal state
goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# set of seen states
seen = []
        
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
        print(*row, sep=' ')

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
            move_up.cost = move_up.depth + getHeristic(move_up, heristic)
            seen.append(move_up.board)
            queue.append(move_up)
   
    move_down = moveDown(move_down)
    if move_down is not None:
        if move_down.board not in seen:
            move_down.parent = node
            move_down.cost = move_down.depth + getHeristic(move_down, heristic)
            seen.append(move_down.board)
            queue.append(move_down)

    move_left = moveLeft(move_left)
    if move_left is not None:
        if move_left.board not in seen:
            move_left.parent = node
            move_left.cost = move_left.depth + getHeristic(move_left, heristic)
            seen.append(move_left.board)
            queue.append(move_left)

    move_right = moveRight(move_right)
    if move_right is not None:
        if move_right.board not in seen:
            move_right.parent = node
            move_right.cost = move_right.depth + getHeristic(move_right, heristic)
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

def getHeristic(node, heristic) -> int:
    return 0

def printSolution(node) -> None:
    if not node.parent:
        printBoard(node)
        print()
        return
    else:
        printSolution(node.parent)
        printBoard(node)
        print()


def main():
    #printPuzzle(goal)
    start = [[1,2,3],
             [5,0,6],
             [4,7,8]]
    posZero = findZero(start)
    root = Node(start, posZero)
    res = search(root,0)

    printSolution(res)
    
if __name__ == "__main__":
    main()
