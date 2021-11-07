import copy
import heapq
from Node import Node

class Evaluater:
    """
    Class to perform search on the game state
    """
    def __init__(self, Game) -> None:
        self.start = Game.start
        self.heuristic = Game.heuristic
        self.generateCoordinates()
        self.generateGoal()
        self.queue = []
        self.seen = set()
        self.Searchdetails = Game.output

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
        max_queue = 0
        self.start.cost = self.getHeuristic(self.start)
        heapq.heappush(self.queue,self.start)
        self.seen.add(str(self.start.board))
        match self.heuristic:
            case 1:
                print("Searching with: A* with Misplaced Tile heuristic")
            case 2:
                print("Searching with: A* with Manhattan Distance heuristic")
            case _:
                print("Searching with: Uniform Cost Search")

        while self.queue:
            front_node = heapq.heappop(self.queue)
            if(front_node.board == self.goal):
                print("\nSolution found at depth",front_node.depth)
                print("Nodes expanded:", expansions)
                print("Max nodes in the queue:", max_queue)
                return front_node
            else:
                # update queue with queuing function
                if(self.Searchdetails):
                    print(("Best state to expand with: g(n) = {} h(n) = {} and f(n) = {}"
                        .format(front_node.depth, front_node.cost-front_node.depth, front_node.cost)))
                    front_node.printBoard()
                self.QueueFunction(front_node)
                if len(self.queue) > max_queue:
                    max_queue = len(self.queue)
                expansions += 1
        else:
            print("No solution found :(") 

    def QueueFunction(self, node):
        """
        Queuing function used to expand node and update queue
        """
        # 4 possible moves        
        move_up = Node(copy.deepcopy(node.board), node.loc_zero, node)
        move_down = Node(copy.deepcopy(node.board), node.loc_zero, node)
        move_left = Node(copy.deepcopy(node.board), node.loc_zero, node)
        move_right = Node(copy.deepcopy(node.board), node.loc_zero, node)

        move_up.moveUp()
        if move_up is not None:
            moveUpstr = str(move_up.board)
            if moveUpstr not in self.seen:
                move_up.parent = node
                move_up.cost = move_up.depth + self.getHeuristic(move_up)
                self.seen.add(moveUpstr)
                heapq.heappush(self.queue,move_up)

        move_down.moveDown()
        if move_down is not None:
            moveDownStr = str(move_down.board)
            if moveDownStr not in self.seen:
                move_down.parent = node
                move_down.cost = move_down.depth + self.getHeuristic(move_down)
                self.seen.add(moveDownStr)
                heapq.heappush(self.queue,move_down)

        move_left.moveLeft()
        if str(move_left) is not None:
            moveLeftStr = str(move_left.board)
            if moveLeftStr not in self.seen:
                move_left.parent = node
                move_left.cost = move_left.depth + self.getHeuristic(move_left)
                self.seen.add(moveLeftStr)
                heapq.heappush(self.queue,move_left)

        move_right.moveRight()
        if str(move_right) is not None:
            moveRightStr = str(move_right.board)
            if moveRightStr not in self.seen:
                move_right.parent = node
                move_right.cost = move_right.depth + self.getHeuristic(move_right)
                self.seen.add(moveRightStr)
                heapq.heappush(self.queue,move_right)
                
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
        match self.heuristic:
            case 1:
                return self.misplacedTileHeuristic(node)
            case 2:
                return self.manhattanDistanceHeuristic(node)
            case _:
                return 0

if __name__ == "__main__":
    pass