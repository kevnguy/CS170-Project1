import copy
from collections import deque

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

seen = {}
        
class Node:
    def __init__(self, board, depth, parent=None) -> None:
        self.board = board
        self.depth = depth
        self.parent = parent
        if(self.parent != None):
            self.gcost = parent.gcost + 1
        else:
            self.gcost = 0

def printPuzzle(puzzle) -> None:
    for row in puzzle:
        print(*row, sep=' ')

def search(root, heristic) -> Node:
    """
    General search algorithm to find a solution if it exists
    """
    expansions = 0
    queue = deque([root])
    seen.add(root)

    while queue:
        front_node = queue.popleft()
        if(front_node.board == goal):
            print("Nodes expanded: {}", expansions)
            return front_node
        else:
            # update queue with queuing function
            queue = QueueFunction(front_node, queue, heristic)
            expansions += 1
    else:
        print("No solution found") 

#TODO
def QueueFunction(node, queue, heristic):
    pass
    """
    Queuing function used to expand node and update queue
    """


def main():
    printPuzzle(goal)

if __name__ == "__main__":
    main()
