import copy
from collections import deque

class Node:
    """
    Class that represents the puzzle board
    """
    def __init__(self, board, zeroPos=None, parent=None) -> None:
        self.board = board
        self.parent = parent
        if self.parent is not None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0
        if zeroPos is None:
            self.findZero()
        else:
            self.loc_zero = zeroPos
        self.cost = 0

    def findZero(self):
        """ 
        Helper used to locate blankspace (0) in given puzzle
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    self.loc_zero = (i,j)

    def printBoard(self) -> None:
        """
        Helper used to print the puzzle board
        """
        for row in self.board:
            for col in row:
                print("{:^2}".format(col), end=' ')
            print()

    """
    Helper functions to expand states - 4 possible moves
    """
    def moveUp(self):
        i,j =  self.loc_zero
        if i == 0:
            return None
        self.board[i][j], self.board[i - 1][j] = self.board[i - 1][j], self.board[i][j]
        self.loc_zero = (i-1,j)
        return self

    def moveDown(self):
        i,j =  self.loc_zero
        if i == len(self.board)-1:
            return None
        self.board[i][j], self.board[i + 1][j] = self.board[i + 1][j], self.board[i][j]
        self.loc_zero = (i+1,j)
        return self

    def moveLeft(self):
        i,j =  self.loc_zero
        if j == 0:
            return None
        self.board[i][j], self.board[i][j - 1] = self.board[i][j - 1], self.board[i][j]
        self.loc_zero = (i,j-1)
        return self

    def moveRight(self):
        i,j =  self.loc_zero
        if j == len(self.board[0])-1:
            return None
        self.board[i][j], self.board[i][j + 1] = self.board[i][j + 1], self.board[i][j]
        self.loc_zero = (i,j+1)
        return self


class Game:
    """
    Class that holds inputed states and prints solution
    """
    def __init__(self,start, heuristic) -> None:
        self.start = start
        self.heuristic = heuristic

    def printSolution(self,node) -> None:
        """
        Helper function to print puzzle solution
        """
        if node.parent is None:
            node.printBoard()
            print()
            return
        else:
            self.printSolution(node.parent)
            node.printBoard()
            print()


class Evaluater:
    """
    Class to perform search on the game state
    """
    def __init__(self, Game) -> None:
        self.start = Game.start
        self.heuristic = Game.heuristic
        self.generateCoordinates()
        self.generateGoal()
        self.queue = deque()
        self.seen = []

    def generateCoordinates(self) -> None:
        """
        Helper function that generates a dict for positions in a solved 
        board. Used to calculate the Manhatten distance heuristic
        """
        length = len(self.start.board)*len(self.start.board[0])
        keys = [0]*length
        keys[0:length-1] = list(range(1,length))
        points = []
        for i in range(len(self.start.board)):    
            for j in range(len(self.start.board[0])):
                points.append((i,j))
        self.coordinates = dict(zip(keys,points))

    def generateGoal(self) -> None:
        """
        Helper function to generates goal state based on the user inputed puzzle dimensions
        """
        cnt = 1
        row = len(self.start.board)
        col = len(self.start.board[0])
        self.goal = [[0]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                self.goal[i][j] = (cnt%(row*col))
                cnt+=1

    def search(self) -> Node:
        """
        General search algorithm to find a solution if it exists
        """
        expansions = 0
        self.queue = deque([self.start])
        self.seen.append(self.start.board)

        while self.queue:
            if self.heuristic:
                self.queue = deque(sorted(list(self.queue), key=lambda node: (node.cost,node.depth)))
            front_node = self.queue.popleft()
            if(front_node.board == self.goal):
                print("Solution found at: depth = {}".format(front_node.depth))
                print("{} Nodes expanded".format(expansions))
                return front_node
            else:
                # update queue with queuing function
                print(("Best state to expand with: g(n) = {} h(n) = {} and f(n) = {}"
                        .format(front_node.depth, front_node.cost-front_node.depth, front_node.cost)))
                front_node.printBoard()
                self.queue = self.QueueFunction(front_node)
                expansions += 1
        else:
            print("No solution found") 

    def QueueFunction(self, node):
        """
        Queuing function used to expand node and update queue
        """
        # 4 possible moves        
        move_up = Node(copy.deepcopy(node.board), node.loc_zero, node)
        move_down = Node(copy.deepcopy(node.board), node.loc_zero, node)
        move_left = Node(copy.deepcopy(node.board), node.loc_zero, node)
        move_right = Node(copy.deepcopy(node.board), node.loc_zero, node)

        # might need to fix cost 
        move_up.moveUp()
        if move_up is not None:
            if move_up.board not in self.seen:
                move_up.parent = node
                move_up.cost = move_up.depth + self.getHeuristic(move_up)
                self.seen.append(move_up.board)
                self.queue.append(move_up)

        move_down.moveDown()
        if move_down is not None:
            if move_down.board not in self.seen:
                move_down.parent = node
                move_down.cost = move_down.depth + self.getHeuristic(move_down)
                self.seen.append(move_down.board)
                self.queue.append(move_down)

        move_left.moveLeft()
        if move_left is not None:
            if move_left.board not in self.seen:
                move_left.parent = node
                move_left.cost = move_left.depth + self.getHeuristic(move_left)
                self.seen.append(move_left.board)
                self.queue.append(move_left)

        move_right.moveRight()
        if move_right is not None:
            if move_right.board not in self.seen:
                move_right.parent = node
                move_right.cost = move_right.depth + self.getHeuristic(move_right)
                self.seen.append(move_right.board)
                self.queue.append(move_right)
                
        return self.queue

    def misplacedTileHeuristic(self, node) -> int:
        """
        Helper function to calculate misplaced tile heuristic
        """
        cnt = 0
        for i in range(len(node.board)):
            for j in range(len(node.board[0])):
                if node.board[i][j] and node.board[i][j] != self.goal[i][j]:
                    cnt+=1
        return cnt

    def manhattanDistanceHeuristic(self, node) -> int:
        """
        Helper function to calculate manhattan distance heuristic
        """
        cnt = 0
        for i in range(len(node.board)):
            for j in range(len(node.board[0])):
                if node.board[i][j] and node.board[i][j] != self.goal[i][j]:
                    x,y = self.coordinates.get(node.board[i][j])
                    cnt+=abs(i-x) + abs(j-y)
        return cnt

    def getHeuristic(self, node) -> int:
        """
        Helper function to return the correct heuristic value from game state
        """
        if self.heuristic == 1:
            return self.misplacedTileHeuristic(node)
        elif self.heuristic == 2:
            return self.manhattanDistanceHeuristic(node)
        return 0

def main():
    """
    Main function
    """
    start = [[7,1,2],
             [4,8,5],
             [6,3,0]]
    root = Node(start)
    heuristic = 2
    newGame = Game(root, heuristic)
    evaluate = Evaluater(newGame)
    solution = evaluate.search()

    if solution is not None: newGame.printSolution(solution)
    
if __name__ == "__main__":
    main()