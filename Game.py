class Game:
    """Class that holds inputed states and prints solution"""
    def __init__(self,start, heuristic, output) -> None:
        self.start = start
        self.heuristic = heuristic
        self.output = output 

    def printSolution(self,node) -> None:
        """Takes in node and prints path to root"""
        if node.parent is None:
            print("Solution")
            node.printBoard()
            print()
            return
        else:
            self.printSolution(node.parent)
            node.printBoard()
            print()

if __name__ == "__main__":
    pass

